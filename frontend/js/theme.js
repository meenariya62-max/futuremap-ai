// Theme toggle - Dark/Light mode
function initTheme() {
  const saved = localStorage.getItem('fm_theme') || 'dark';
  if (saved === 'light') {
    document.body.classList.add('light-mode');
    updateToggleIcon();
  }
}

function toggleTheme() {
  document.body.classList.toggle('light-mode');
  const isLight = document.body.classList.contains('light-mode');
  localStorage.setItem('fm_theme', isLight ? 'light' : 'dark');
  updateToggleIcon();
}

function updateToggleIcon() {
  const btn = document.getElementById('themeToggle');
  if (!btn) return;
  const isLight = document.body.classList.contains('light-mode');
  btn.textContent = isLight ? '🌙' : '☀️';
  btn.title = isLight ? 'Switch to Dark Mode' : 'Switch to Light Mode';
}

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  const btn = document.getElementById('themeToggle');
  if (btn) btn.addEventListener('click', toggleTheme);
});
