/* ========================================================
   Charts & Interactivity — Mayo Clinic Case Study
   Data sourced from: Fierce Healthcare (Feb 2024),
   Microsoft News (Sept 28, 2023), Mayo Clinic Platform
   press releases, National Academies of Sciences (2023)
   ======================================================== */

const NAVY = '#0A2240';
const RED  = '#C8102E';
const GRAY = '#9CA3AF';

Chart.defaults.font.family = "'Inter', system-ui, sans-serif";
Chart.defaults.color = '#6B7280';

/* ── 1. Platform Growth ─────────────────────────────── */
(function() {
  const ctx = document.getElementById('chartGrowth');
  if (!ctx) return;

  /* Verified data points only — point-in-time observations */
  const labels = ['Early 2022', 'Mid 2022', 'May 2023', 'June 2024'];

  new Chart(ctx, {
    type: 'line',
    data: {
      labels,
      datasets: [
        {
          label: 'Solution Developers',
          data: [4, 11, null, 81],
          borderColor: NAVY,
          backgroundColor: 'rgba(10,34,64,0.08)',
          borderWidth: 2.5,
          pointRadius: 5,
          pointBackgroundColor: NAVY,
          fill: true,
          tension: 0.3,
          spanGaps: true,
        },
        {
          label: 'Institutional Partners',
          data: [1, 1, 4, 9],
          borderColor: RED,
          backgroundColor: 'rgba(200,16,46,0.07)',
          borderWidth: 2.5,
          pointRadius: 5,
          pointBackgroundColor: RED,
          fill: true,
          tension: 0.3,
        },
      ],
    },
    options: {
      responsive: true,
      interaction: { mode: 'index', intersect: false },
      plugins: {
        legend: {
          position: 'top',
          labels: { usePointStyle: true, pointStyleWidth: 10, padding: 16, font: { size: 12 } }
        },
        tooltip: {
          callbacks: {
            footer: () => 'Source: Mayo Clinic press releases; National Academies (2023)',
          }
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          grid: { color: '#F3F4F6' },
          title: { display: true, text: 'Count', font: { size: 11 } }
        },
        x: { grid: { display: false } }
      }
    }
  });
})();

/* ── 2. Patient Lives Network ───────────────────────── */
(function() {
  const ctx = document.getElementById('chartLives');
  if (!ctx) return;

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['2022 (US Only)', 'May 2023 (+3 International)', 'June 2024'],
      datasets: [{
        label: 'Patient Lives in Network (Millions)',
        data: [1.3, 27, 56],
        backgroundColor: [
          'rgba(10,34,64,0.5)',
          'rgba(10,34,64,0.7)',
          'rgba(10,34,64,0.92)',
        ],
        borderColor: NAVY,
        borderWidth: 1.5,
        borderRadius: 4,
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: ctx => ` ${ctx.raw}M patient lives`,
            footer: () => 'Source: Mayo Clinic Platform press releases; National Academies (2023)',
          }
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          grid: { color: '#F3F4F6' },
          title: { display: true, text: 'Millions of Patient Lives', font: { size: 11 } }
        },
        x: { grid: { display: false } }
      }
    }
  });
})();

/* ── 3. AI Healthcare Market ────────────────────────── */
(function() {
  const ctx = document.getElementById('chartMarket');
  if (!ctx) return;

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['2023\n(Actual)', '2024\n(Est.)', '2025\n(Proj.)', '2026\n(Proj.)', '2027\n(Proj.)', '2028\n(Proj.)', '2029\n(Proj.)', '2030\n(Proj.)'],
      datasets: [{
        label: 'Market Size ($B)',
        data: [22.45, 30.9, 42.6, 58.7, 80.9, 111.4, 153.5, 208.2],
        backgroundColor: [
          'rgba(10,34,64,0.85)',  /* 2023 actual */
          ...Array(7).fill('rgba(200,16,46,0.45)'), /* projections */
        ],
        borderColor: [NAVY, ...Array(7).fill(RED)],
        borderWidth: 1.5,
        borderRadius: 4,
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: ctx => ` $${ctx.raw}B`,
            footer: (items) => {
              const yr = items[0].label.split('\n')[0];
              return yr === '2023'
                ? 'Actual market size'
                : 'Industry projection — ~37.5% CAGR assumed';
            },
          }
        },
        annotation: {}
      },
      scales: {
        y: {
          beginAtZero: true,
          grid: { color: '#F3F4F6' },
          title: { display: true, text: 'USD Billions', font: { size: 11 } }
        },
        x: { grid: { display: false } }
      }
    }
  });
})();

/* ── 4. IBM Watson vs Mayo Radar ────────────────────── */
(function() {
  const ctx = document.getElementById('chartRadar');
  if (!ctx) return;

  new Chart(ctx, {
    type: 'radar',
    data: {
      labels: [
        'Data Diversity',
        'Governance Depth',
        'Explainability',
        'Clinical Validation',
        'Outcome Measurement',
        'Regulatory Alignment'
      ],
      datasets: [
        {
          label: 'IBM Watson Health (2011–2022)',
          data: [2, 1, 1, 2, 1, 2],
          borderColor: '#DC2626',
          backgroundColor: 'rgba(220,38,38,0.12)',
          borderWidth: 2,
          pointBackgroundColor: '#DC2626',
          pointRadius: 4,
        },
        {
          label: 'Mayo Clinic Platform (2024)',
          data: [4, 5, 3, 4, 4, 5],
          borderColor: NAVY,
          backgroundColor: 'rgba(10,34,64,0.12)',
          borderWidth: 2,
          pointBackgroundColor: NAVY,
          pointRadius: 4,
        }
      ]
    },
    options: {
      responsive: true,
      scales: {
        r: {
          min: 0, max: 5,
          ticks: { stepSize: 1, font: { size: 10 } },
          pointLabels: { font: { size: 11.5 }, color: '#374151' },
          grid: { color: '#E5E7EB' },
        }
      },
      plugins: {
        legend: {
          position: 'bottom',
          labels: { usePointStyle: true, padding: 16, font: { size: 12 } }
        },
        tooltip: {
          callbacks: {
            footer: () => 'Scale: 1=Weak … 5=Strong (qualitative assessment based on case evidence)'
          }
        }
      }
    }
  });
})();

/* ── Smooth scroll offset for sticky nav ───────────── */
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const target = document.querySelector(a.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    const offset = 64;
    window.scrollTo({ top: target.offsetTop - offset, behavior: 'smooth' });
  });
});
