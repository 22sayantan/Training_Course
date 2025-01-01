document.addEventListener('DOMContentLoaded', function () {
  var ctx = document.getElementById('revenueChart').getContext('2d');
  var revenueChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
      datasets: [{
        label: 'Gross Sales',
        data: [120000, 150000, 180000, 200000, 220000, 50000, 270000, 150000, 320000, 350000, 200000, 400000],
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
});

document.addEventListener('DOMContentLoaded', function () {
  var ctx = document.getElementById('courses_popularity_chart').getContext('2d');
  var revenueChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['programming', 'python', 'flask', 'django', 'database', 'docker', 'React.js', 'Machine learning', 'Data Science', 'Artificial Intelligence', 'Cyber Security', 'Ethical Hacking'],
      datasets: [{
        label: 'Courses Popularity',
        data: [100, 150, 180, 200, 220, 50, 270, 150, 320, 350, 200, 400],
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
});

const total_members = document.getElementById('total_members');
const total_teachers = document.getElementById('total_teachers');
const total_staffs = document.getElementById('total_staff');

total_members.innerHTML = Number(total_teachers.innerHTML) + Number(total_staffs.innerHTML);


// calculate and display the total amount of Wages:::
let total_wages = document.getElementById('total_wages');
let total_gross_revenue = document.getElementById('total_gross_revenue');
let total_net_revenue = document.getElementById('total_net_revenue');

total_gross_revenue = total_gross_revenue.innerHTML;
total_net_revenue = total_net_revenue.innerHTML;

total_gross_revenue = total_gross_revenue.replace(/,/g,'');
total_gross_revenue = Number(total_gross_revenue.replace('$',''));
total_net_revenue = total_net_revenue.replace(/,/g,'');
total_net_revenue = Number(total_net_revenue.replace('$',''));

let total_wages_amount = 0;
total_wages_amount = total_gross_revenue - total_net_revenue;
total_wages_amount = total_wages_amount.toFixed(2).toString();
total_wages_amount = '$' + total_wages_amount.replace(/\B(?=(\d{3})+(?!\d))/g, ",");

total_wages.innerHTML = total_wages_amount;

// console.log(typeof(total_wages));