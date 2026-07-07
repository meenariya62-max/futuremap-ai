async function runAnalysis(e) {
  e.preventDefault();
  const skills=document.getElementById('analyzeSkills').value.trim();
  if(!skills) return;
  const btn=document.getElementById('analyzeBtn');
  btn.disabled=true;
  btn.innerHTML='⏳ Analyzing...';
  try {
    const res=await fetch('/api/predict',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name:'Analysis',skills})});
    const data=await res.json();
    renderAnalysis(data);
    document.getElementById('analysisResult').style.display='block';
  } catch { alert('Backend error!'); }
  btn.disabled=false;
  btn.innerHTML='🔍 Run Analysis';
}

function renderAnalysis(data) {
  const r=data.readiness_score||0;
  document.getElementById('readinessPct').textContent=`${r}%`;
  setTimeout(()=>{document.getElementById('readinessFill').style.width=`${r}%`;},100);
  document.getElementById('missingList').innerHTML=data.missing_skills.length?data.missing_skills.map(s=>`<span class="tag tag-missing">📌 ${s}</span>`).join(''):'<span class="tag tag-match">✅ Great!</span>';
  document.getElementById('careerComp').innerHTML=data.top_matches.map((m,i)=>`<div class="progress-wrap"><div class="progress-header"><span>${m.career}</span><span>${m.confidence}%</span></div><div class="progress-bar"><div class="progress-fill ${['purple','green','orange'][i]}" style="width:0" data-target="${m.confidence}"></div></div></div>`).join('');
  setTimeout(()=>{document.querySelectorAll('[data-target]').forEach(el=>{el.style.width=el.getAttribute('data-target')+'%';});},200);
  const ctx=document.getElementById('gapChart');
  if(!ctx||!data.missing_skills.length) return;
  if(window._gapChart) window._gapChart.destroy();
  window._gapChart=new Chart(ctx,{type:'bar',data:{labels:data.missing_skills.slice(0,8),datasets:[{label:'Skill Gap',data:data.missing_skills.slice(0,8).map(()=>Math.floor(Math.random()*40+60)),backgroundColor:'rgba(255,79,163,0.6)',borderColor:'#ff4fa3',borderWidth:1,borderRadius:8}]},options:{indexAxis:'y',responsive:true,plugins:{legend:{labels:{color:'#8892b0'}}},scales:{x:{ticks:{color:'#8892b0',callback:v=>`${v}%`},grid:{color:'rgba(255,255,255,0.04)'},max:100},y:{ticks:{color:'#8892b0'},grid:{display:false}}}}});
}

document.addEventListener('DOMContentLoaded',()=>{
  const form=document.getElementById('analyzeForm');
  if(form) form.addEventListener('submit',runAnalysis);
});
