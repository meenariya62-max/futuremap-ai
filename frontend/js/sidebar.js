function renderSidebar(activePage) {
  const pages = [
    { href: 'dashboard.html', icon: '⊞', label: 'Dashboard' },
    { href: 'predict.html', icon: '⚡', label: 'Career Predict' },
    { href: 'compare.html', icon: '⚖️', label: 'Compare Careers' },
    { href: 'analysis.html', icon: '📊', label: 'Skill Analysis' },
    { href: 'history.html', icon: '🕓', label: 'History' },
    { href: 'resources.html', icon: '📚', label: 'Resources' },
    { href: 'profile.html', icon: '👤', label: 'Profile' },
  ];

  const user = JSON.parse(localStorage.getItem('fm_user') || '{"name":"User","email":""}');

  return `
    <div class="sidebar-logo">
      <a class="logo-mark" href="dashboard.html" style="text-decoration:none;display:flex;align-items:center;gap:12px">
        <div class="logo-icon">🗺️</div>
        <span class="logo-text">Future<span>Map</span> AI</span>
      </a>
    </div>
    <nav class="sidebar-nav">
      <div class="nav-section-label">Main</div>
      ${pages.map(p => `
        <a href="${p.href}" class="nav-item ${activePage === p.href ? 'active' : ''}">
          <span class="nav-icon">${p.icon}</span>
          ${p.label}
        </a>
      `).join('')}
    </nav>
    <div class="sidebar-footer">
      <div class="user-card" onclick="window.location='profile.html'">
        <div class="user-avatar" data-user-initials>${(user.name||'U')[0].toUpperCase()}</div>
        <div class="user-info">
          <div class="user-name" data-user-name>${user.name || 'User'}</div>
          <div class="user-role">Career Seeker</div>
        </div>
      </div>
      <button class="btn btn-ghost btn-sm btn-full" style="margin-top:8px" onclick="logout()">
        🚪 Sign Out
      </button>
    </div>
  `;
}

function logout() {
  localStorage.removeItem('fm_user');
  window.location.href = '/login.html';
}
