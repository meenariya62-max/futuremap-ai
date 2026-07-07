function saveUser(user) { localStorage.setItem('fm_user',JSON.stringify(user)); }
function getUser() { try { return JSON.parse(localStorage.getItem('fm_user')); } catch { return null; } }
function logout() { localStorage.removeItem('fm_user'); window.location.href='/login.html'; }
function fillUserInfo(user) {
  document.querySelectorAll('[data-user-name]').forEach(el=>el.textContent=user.name||'User');
  document.querySelectorAll('[data-user-initials]').forEach(el=>el.textContent=(user.name||'U')[0].toUpperCase());
}

async function handleLogin(e) {
  e.preventDefault();
  const email=document.getElementById('email').value.trim();
  const password=document.getElementById('password').value;
  const btn=document.getElementById('loginBtn');
  const msgEl=document.getElementById('loginMsg');
  btn.disabled=true; btn.innerHTML='⏳ Signing in...';
  try {
    const res=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({email,password})});
    const data=await res.json();
    if(!res.ok) throw new Error(data.error||'Login failed');
    saveUser(data.user);
    showAlert(msgEl,'success','✅ Login successful!');
    setTimeout(()=>window.location.href='/dashboard.html',800);
  } catch(err) { showAlert(msgEl,'error',`❌ ${err.message}`); btn.disabled=false; btn.innerHTML='Sign In'; }
}

async function handleRegister(e) {
  e.preventDefault();
  const name=document.getElementById('name').value.trim();
  const email=document.getElementById('email').value.trim();
  const password=document.getElementById('password').value;
  const skills=document.getElementById('skills')?.value?.trim()||'';
  const btn=document.getElementById('registerBtn');
  const msgEl=document.getElementById('registerMsg');
  btn.disabled=true; btn.innerHTML='⏳ Creating...';
  try {
    const res=await fetch('/api/register',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name,email,password,skills})});
    const data=await res.json();
    if(!res.ok) throw new Error(data.error||'Failed');
    saveUser(data.user);
    showAlert(msgEl,'success','✅ Account created!');
    setTimeout(()=>window.location.href='/dashboard.html',800);
  } catch(err) { showAlert(msgEl,'error',`❌ ${err.message}`); btn.disabled=false; btn.innerHTML='Create Account'; }
}

function showAlert(el,type,msg) { if(!el) return; el.className=`alert alert-${type}`; el.textContent=msg; el.style.display='flex'; }

function demoLogin() { saveUser({name:'Demo User',email:'demo@futuremap.ai',id:0}); window.location.href='/dashboard.html'; }

function setActiveNav() {
  const page=window.location.pathname.split('/').pop()||'dashboard.html';
  document.querySelectorAll('.nav-item').forEach(link=>{
    if(link.getAttribute('href')===page) link.classList.add('active');
    else link.classList.remove('active');
  });
}

document.addEventListener('DOMContentLoaded',()=>{
  setActiveNav();
  const user=getUser();
  if(user) fillUserInfo(user);
  const loginForm=document.getElementById('loginForm');
  if(loginForm) loginForm.addEventListener('submit',handleLogin);
  const registerForm=document.getElementById('registerForm');
  if(registerForm) registerForm.addEventListener('submit',handleRegister);
});
