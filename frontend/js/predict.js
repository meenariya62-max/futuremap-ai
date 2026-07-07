function quickFill(skills) {
  document.getElementById('skillsInput').value = skills;
}

async function submitPrediction() {
  const name = document.getElementById('nameInput').value || 'User';
  const skills = document.getElementById('skillsInput').value.trim();
  if (!skills) { alert('Skills likho!'); return; }
  const btn = document.getElementById('predictBtn');
  btn.disabled = true;
  btn.innerHTML = '⏳ Analyzing...';
  document.getElementById('loadingState').style.display = 'block';
  document.getElementById('resultSection').style.display = 'none';
  try {
    const res = await fetch('/api/predict', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({name, skills})
    });
    const data = await res.json();
    document.getElementById('loadingState').style.display = 'none';
    renderResult(data);
    document.getElementById('resultSection').style.display = 'block';
  } catch(err) {
    document.getElementById('loadingState').style.display = 'none';
    alert('Backend error!');
  }
  btn.disabled = false;
  btn.innerHTML = '⚡ Analyze My Career';
}

function renderResult(data) {
  const icons = {'AI Engineer':'🤖','Data Scientist':'📊','Full Stack Developer':'💻','Backend Developer':'⚙️','Frontend Developer':'🎨','DevOps Engineer':'🔧','Data Analyst':'📈','NLP Engineer':'🧠','Computer Vision Engineer':'👁️','Android Developer':'📱','iOS Developer':'🍎','Cybersecurity Engineer':'🔐','Blockchain Developer':'⛓️','Cloud Architect':'☁️','Big Data Engineer':'🌊','UI/UX Designer':'✏️'};
  document.getElementById('careerEmoji').textContent = icons[data.recommended_career]||'💼';
  document.getElementById('recommendedCareer').textContent = data.recommended_career;
  document.getElementById('confidenceScore').textContent = data.confidence;
  document.getElementById('salaryRange').textContent = data.salary;
  document.getElementById('confRingPct').textContent = data.confidence;
  const colors=['rgba(108,99,255,0.12)','rgba(0,212,255,0.1)','rgba(0,229,160,0.1)'];
  const textColors=['#6c63ff','#00d4ff','#00e5a0'];
  document.getElementById('topMatches').innerHTML=data.top_matches.map((m,i)=>`
    <div class="career-match"><div class="career-match-info"><div class="career-match-icon" style="background:${colors[i]}">${icons[m.career]||'💼'}</div><div><div class="career-match-name">${m.career}</div><div class="career-match-sub">Match Score</div></div></div><div class="match-pct" style="color:${textColors[i]}">${m.confidence}%</div></div>`).join('');
  document.getElementById('missingSkills').innerHTML=data.missing_skills.length?data.missing_skills.map(s=>`<span class="tag tag-missing">📌 ${s}</span>`).join(''):'<span class="tag tag-match">✅ All skills present!</span>';
  const r=data.readiness_score||0;
  document.getElementById('readinessScore').textContent=r+'%';
  setTimeout(()=>{document.getElementById('readinessFill').style.width=r+'%';},100);
  document.getElementById('roadmapList').innerHTML=data.roadmap.map((s,i)=>`<li class="roadmap-item"><div class="roadmap-dot">${i+1}</div><div class="roadmap-text">${s}</div></li>`).join('');
  const ctx=document.getElementById('matchChart');
  if(window._chart)window._chart.destroy();
  window._chart=new Chart(ctx,{type:'doughnut',data:{labels:data.top_matches.map(m=>m.career),datasets:[{data:data.top_matches.map(m=>m.confidence),backgroundColor:['rgba(108,99,255,0.8)','rgba(0,212,255,0.7)','rgba(0,229,160,0.7)'],borderColor:['#6c63ff','#00d4ff','#00e5a0'],borderWidth:2}]},options:{responsive:true,plugins:{legend:{position:'bottom',labels:{color:'#8892b0'}}},cutout:'68%'}});
}
