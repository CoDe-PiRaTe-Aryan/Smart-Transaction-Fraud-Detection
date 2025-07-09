document.addEventListener("DOMContentLoaded", () => {
  // Dummy data — Replace with actual data from backend if needed

  // Line Chart: Fraud over time (dummy steps)
  const lineCtx = document.getElementById('lineChart').getContext('2d');
  new Chart(lineCtx, {
    type: 'line',
    data: {
      labels: ['Step 1', 'Step 2', 'Step 3', 'Step 4', 'Step 5'],
      datasets: [
        {
          label: 'Fraudulent',
          data: [3, 4, 5, 2, 6],
          borderColor: 'red',
          fill: false
        },
        {
          label: 'Non-Fraudulent',
          data: [50, 60, 55, 70, 65],
          borderColor: 'green',
          fill: false
        }
      ]
    }
  });

  // Pie Chart: Transaction type distribution
  const pieCtx = document.getElementById('pieChart').getContext('2d');
  new Chart(pieCtx, {
    type: 'pie',
    data: {
      labels: ['TRANSFER', 'CASH_OUT'],
      datasets: [{
        data: [65, 35],
        backgroundColor: ['#4CAF50', '#FF9800']
      }]
    }
  });

  // Bar Chart: Fraud count by type
  const barCtx = document.getElementById('barChart').getContext('2d');
  new Chart(barCtx, {
    type: 'bar',
    data: {
      labels: ['TRANSFER', 'CASH_OUT'],
      datasets: [{
        label: 'Fraud Count',
        data: [25, 15],
        backgroundColor: 'crimson'
      }]
    }
  });
});
