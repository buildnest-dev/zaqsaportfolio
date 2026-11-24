// ZAQSA server — no dependencies. Node 18+.  Run: ADMIN_USER=x ADMIN_PASS=y node server.js
const http=require('http'),fs=require('fs'),path=require('path'),crypto=require('crypto');
const ROOT=path.join(__dirname,'public'),DB=process.env.DATA_FILE||path.join(__dirname,'enquiries.jsonl');
const {ADMIN_USER,ADMIN_PASS,NOTIFY_WEBHOOK,PORT=3000}=process.env;
const MIME={'.html':'text/html; charset=utf-8','.css':'text/css','.js':'text/javascript','.png':'image/png','.jpg':'image/jpeg','.xml':'application/xml','.txt':'text/plain'};
const hits=new Map(); // ip -> timestamps (5 enquiries / 10 min)
const limited=ip=>{const n=Date.now(),a=(hits.get(ip)||[]).filter(t=>n-t<6e5);a.push(n);hits.set(ip,a);return a.length>5};
const read=(f)=>fs.existsSync(f)?fs.readFileSync(f,'utf8').split('\n').filter(Boolean).map(l=>JSON.parse(l)):[];
const save=rows=>fs.writeFileSync(DB,rows.map(r=>JSON.stringify(r)).join('\n')+(rows.length?'\n':''));
const send=(res,c,b,t='application/json')=>{res.writeHead(c,{'Content-Type':t,'X-Content-Type-Options':'nosniff','Referrer-Policy':'strict-origin-when-cross-origin'});res.end(typeof b==='string'||Buffer.isBuffer(b)?b:JSON.stringify(b))};
const body=req=>new Promise((ok,no)=>{let d='';req.on('data',c=>{d+=c;if(d.length>2e4){no();req.destroy()}});req.on('end',()=>{try{ok(JSON.parse(d))}catch{no()}})});
const eq=(a,b)=>{const x=Buffer.from(a),y=Buffer.from(b);return x.length===y.length&&crypto.timingSafeEqual(x,y)};
const authed=req=>{if(!ADMIN_USER||!ADMIN_PASS)return null;const h=req.headers.authorization||'';if(!h.startsWith('Basic '))return false;const [u,...p]=Buffer.from(h.slice(6),'base64').toString().split(':');return eq(u,ADMIN_USER)&&eq(p.join(':'),ADMIN_PASS)};
const clean=(v,n)=>String(v||'').replace(/[\u0000-\u001f]/g,' ').trim().slice(0,n);
const SERVICES=['Website Development','Mobile App Development','AI & Automation','Custom Software / CRM','Digital Marketing','IT Consulting','Other'];
const csv=rows=>['id,at,status,name,company,email,phone,service,budget,contactMethod,details'].concat(rows.map(r=>[r.id,r.at,r.status,r.name,r.company,r.email,r.phone,r.service,r.budget,r.contactMethod,r.details].map(v=>'"'+String(v||'').replace(/"/g,'""').replace(/^([=+\-@])/,"'$1")+'"').join(','))).join('\n');
const ADMIN=`<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>ZAQSA Admin</title><style>body{font:14px system-ui;background:#0A0C14;color:#EEF0FF;margin:0;padding:20px}table{border-collapse:collapse;width:100%}td,th{border-bottom:1px solid #273244;padding:8px;text-align:left;vertical-align:top}select,a{background:#111827;color:#EEF0FF;border:1px solid #273244;padding:6px;border-radius:6px}</style><h2>Enquiries</h2><p><select id=f><option value="">All services</option></select> <a href=/api/admin/export.csv>Export CSV</a></p><table id=t></table><script>
const esc=s=>String(s||'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));let rows=[];
async function load(){rows=await(await fetch('/api/admin/enquiries')).json();const s=[...new Set(rows.map(r=>r.service))];f.innerHTML='<option value="">All services</option>'+s.map(x=>'<option>'+esc(x)+'</option>').join('');draw()}
function draw(){t.innerHTML='<tr><th>Date<th>Name<th>Contact<th>Service / Budget<th>Details<th>Status</tr>'+rows.filter(r=>!f.value||r.service===f.value).map(r=>'<tr><td>'+esc(r.at.slice(0,16).replace('T',' '))+'<td>'+esc(r.name)+'<br>'+esc(r.company)+'<td>'+esc(r.email)+'<br>'+esc(r.phone)+'<br>'+esc(r.contactMethod)+'<td>'+esc(r.service)+'<br>'+esc(r.budget)+'<td>'+esc(r.details)+'<td><select onchange="st(\\''+r.id+'\\',this.value)">'+['new','contacted','closed'].map(x=>'<option'+(x===r.status?' selected':'')+'>'+x+'</option>').join('')+'</select>').join('')}
async function st(id,status){await fetch('/api/admin/status',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({id,status})});load()}
f.onchange=draw;load()</script>`;
http.createServer(async(req,res)=>{
  const url=new URL(req.url,'http://x'),p=decodeURIComponent(url.pathname),ip=(req.headers['x-forwarded-for']||req.socket.remoteAddress||'').split(',')[0].trim();
  try{
    if(p==='/api/enquiry'&&req.method==='POST'){
      if(limited(ip))return send(res,429,{ok:false,error:'Too many requests'});
      const d=await body(req).catch(()=>null);if(!d)return send(res,400,{ok:false});
      if(d.website)return send(res,200,{ok:true}); // honeypot: pretend OK, store nothing
      const r={id:crypto.randomUUID(),at:new Date().toISOString(),status:'new',name:clean(d.name,100),company:clean(d.company,120),email:clean(d.email,150),phone:clean(d.phone,30),service:clean(d.service,60),budget:clean(d.budget,40),contactMethod:clean(d.contactMethod,20),details:clean(d.details,3000)};
      if(r.name.length<2||!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(r.email)||r.phone.replace(/\D/g,'').length<10||!SERVICES.includes(r.service)||r.details.length<10||d.consent!==true)return send(res,422,{ok:false,error:'Invalid input'});
      fs.appendFileSync(DB,JSON.stringify(r)+'\n'); // stored first; only then report success
      if(NOTIFY_WEBHOOK)fetch(NOTIFY_WEBHOOK,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({text:`New ZAQSA enquiry: ${r.name} (${r.service}) ${r.email}`})}).catch(()=>{});
      return send(res,200,{ok:true});
    }
    if(p==='/admin'||p.startsWith('/api/admin/')){
      const a=authed(req);
      if(a===null)return send(res,503,'Admin disabled: set ADMIN_USER and ADMIN_PASS','text/plain');
      if(!a){res.setHeader('WWW-Authenticate','Basic realm="ZAQSA Admin"');return send(res,401,'Login required','text/plain')}
      if(p==='/admin')return send(res,200,ADMIN,'text/html; charset=utf-8');
      if(p==='/api/admin/enquiries')return send(res,200,read(DB).reverse());
      if(p==='/api/admin/export.csv'){res.setHeader('Content-Disposition','attachment; filename=enquiries.csv');return send(res,200,csv(read(DB)),'text/csv')}
      if(p==='/api/admin/status'&&req.method==='POST'){const d=await body(req),rows=read(DB),r=rows.find(x=>x.id===d.id);if(!r||!['new','contacted','closed'].includes(d.status))return send(res,400,{ok:false});r.status=d.status;save(rows);return send(res,200,{ok:true})}
    }
    let f=path.normalize(path.join(ROOT,p));if(!f.startsWith(ROOT))return send(res,403,'Forbidden','text/plain');
    if(fs.existsSync(f)&&fs.statSync(f).isDirectory())f=path.join(f,'index.html');
    if(!fs.existsSync(f))return send(res,404,'<h1>404</h1><a href="/">Home</a>','text/html');
    res.setHeader('Cache-Control',f.includes('assets')?'public,max-age=86400':'no-cache');
    send(res,200,fs.readFileSync(f),MIME[path.extname(f)]||'application/octet-stream');
  }catch(e){send(res,500,{ok:false})}
}).listen(PORT,()=>console.log('ZAQSA on http://localhost:'+PORT));
