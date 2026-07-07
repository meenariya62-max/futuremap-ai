async function loadDashboard() {
  await loadRecentHistory();
  await loadCareers();
  renderSalaryChart();
  renderSkillsRadar();
  animateStats();
}

async function loadRecentHistory() {
  const container = document.getElementById('recentPredictions');
  if (!container) return;
  try {
    const res = await fetch('/api/history');
    const history = await res.json();
    const recent = history.slice(0,5);
    if (!recent.length) {
      container.innerHTML = `<tr><td colspan="5" style="text-align:center;padding:24px;color:var(--text-muted)">No predictions yet. <a href="predict.html" style="color:var(--accent-primary)">Make one!</a></td></tr>`;
      return;
    }
    container.innerHTML = recent.map(h=>`<tr><td>${h.name}</td><td><div class="tags-wrap">${h.skills.split(',').slice(0,3).map(s=>`<span class="tag tag-skill">${s.trim()}</span>`).join('')}</div></td><td><span class="tag tag-match">🎯 ${h.recommended_career}</span></td><td style="color:#6c63ff;font-weight:700">${h.confidence}</td><td style="color:#8892b0;font-size:12px">${h.date}</td></tr>`).join('');
    const totalEl=document.getElementById('totalPredictions');
    if(totalEl) totalEl.textContent=history.length;
  } catch(e) {
    if(container) container.innerHTML=`<tr><td colspan="5" style="text-align:center;color:#4a5568;padding:24px">Start Flask backend to see data</td></tr>`;
  }
}

async function loadCareers() {
  try {
    const res = await fetch('/api/careers');
    const careers = await res.json();
    const container = document.getElementById('topCareers');
    if (!container) return;
    const icons={'AI Engineer':'🤖','Data Scientist':'📊','Full Stack Developer':'💻','Backend Developer':'⚙️','Frontend Developer':'🎨','DevOps Engineer':'🔧','Data Analyst':'📈','NLP Engineer':'🧠','Cloud Architect':'☁️','Blockchain Developer':'⛓️'};
    container.innerHTML=careers.slice(0,6).map(c=>`<div class="career-match"><div class="career-match-info"><div class="career-match-icon" style="background:rgba(108,99,255,0.1)">${icons[c.name]||'💼'}</div><div><div class="career-match-name">${c.name}</div><div class="career-match-sub">${c.salary}</div></div></div><div style="color:#00e5a0;font-size:12px;font-weight:600">HOT</div></div>`).join('');
  } catch(e) {}
}

function renderSalaryChart() {
  const ctx=document.getElementById('salaryChart');
  if(!ctx) return;
  if(window._salaryChart) window._salaryChart.destroy();
  window._salaryChart=new Chart(ctx,{type:'bar',data:{labels:['AI Eng','Data Sci','Full Stack','DevOps','Cloud','Blockchain'],datasets:[{label:'Min (LPA)',data:[8,6,5,7,10,7],backgroundColor:'rgba(108,99,255,0.6)',borderRadius:8},{label:'Max (LPA)',data:[25,22,20,22,30,28],backgroundColor:'rgba(0,212,255,0.5)',borderRadius:8}]},options:{responsive:true,plugins:{legend:{labels:{color:'#8892b0'}}},scales:{x:{ticks:{color:'#8892b0'},grid:{color:'rgba(255,255,255,0.04)'}},y:{ticks:{color:'#8892b0',callback:v=>`₹${v}L`},grid:{color:'rgba(255,255,255,0.04)'}}}}});
}

function renderSkillsRadar() {
  const ctx=document.getElementById('skillsRadar');
  if(!ctx) return;
  new Chart(ctx,{type:'radar',data:{labels:['Python','ML/AI','Web Dev','Cloud','Data','Security'],datasets:[{label:'Market Demand',data:[95,90,85,80,88,72],backgroundColor:'rgba(108,99,255,0.15)',borderColor:'#6c63ff',pointBackgroundColor:'#6c63ff',borderWidth:2}]},options:{responsive:true,scales:{r:{ticks:{display:false},grid:{color:'rgba(255,255,255,0.06)'},pointLabels:{color:'#8892b0',font:{size:12}}}},plugins:{legend:{labels:{color:'#8892b0'}}}}});
}

function animateStats() {
  document.querySelectorAll('[data-count]').forEach(el=>{
    const target=parseInt(el.getAttribute('data-count'));
    let count=0;
    const inc=Math.ceil(target/60);
    const timer=setInterval(()=>{count=Math.min(count+inc,target);el.textContent=count;if(count>=target)clearInterval(timer);},20);
  });
}

document.addEventListener('DOMContentLoaded', loadDashboard);
