const priceCtx = document.getElementById('priceChart').getContext('2d');
const volumeCtx = document.getElementById('volumeChart').getContext('2d');

const priceChart = new Chart(priceCtx, {
  type: 'line',
  data: {
    labels: [],
    datasets: [{
      label: 'Price (USD)',
      data: [],
      borderWidth: 1,
      borderColor: 'blue',
      tension: 0.4
    }]
  },
  options: {
    responsive: true,
    animation: false
  }
});

const volumeChart = new Chart(volumeCtx, {
  type: 'bar',
  data: {
    labels: [],
    datasets: [{
      label: 'Volume',
      data: [],
      backgroundColor: 'rgba(0, 255, 0, 0.5)'
    }]
  },
  options: {
    responsive: true,
    animation: false
  }
});

const evtSource = new EventSource('http://localhost:5000/stream');
evtSource.addEventListener('update', function(event) {
  const data = JSON.parse(event.data);
  const now = new Date().toLocaleTimeString();

  if (priceChart.data.labels.length > 20) {
    priceChart.data.labels.shift();
    priceChart.data.datasets[0].data.shift();
    volumeChart.data.labels.shift();
    volumeChart.data.datasets[0].data.shift();
  }

  priceChart.data.labels.push(now);
  priceChart.data.datasets[0].data.push(data.price);
  volumeChart.data.labels.push(now);
  volumeChart.data.datasets[0].data.push(data.volume);

  priceChart.update();
  volumeChart.update();
});
