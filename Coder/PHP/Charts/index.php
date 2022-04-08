<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chart by Kris</title>
</head>
    <!-- 
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script> 
    -->
   <script type="text/javascript" src="./JS/loader.js"></script> 

    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Year', 'Sales', 'Expenses', 'AAA'],
          ['2004',  1000,      400, 100],
          ['2005',  1170,      460,  442],
          ['2006',  660,       1120,   583],
          ['2007',  1030,      540,   400]
        ]);

        var options = {
          title: 'Company Performance',
          curveType: 'function',
          legend: { position: 'bottom' }
        };

        var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

        chart.draw(data, options);
      }
    </script>



<body>
  <div id="curve_chart" style="width: 900px; height: 500px"></div>
  
</body>
</html>