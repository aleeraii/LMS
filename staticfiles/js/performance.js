google.charts.load("current", { packages: ["corechart"] });
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
    var performanceData = google.visualization.arrayToDataTable([
        ['Task', 'Hours per Day'],
        ['Quiz', 2],
        ['Assignment', 2],
        ['Papers', 2],
    ]);
    var attendanceData = google.visualization.arrayToDataTable([
        ['Status', 'Numbers'],
        ['Absents', 11],
        ['Presents', 2],
        ['Leaves', 2],
    ]);


    var performanceChart = new google.visualization.PieChart(document.getElementById('performanceChart'));
    var attendanceChart = new google.visualization.PieChart(document.getElementById('attendanceChart'));
    performanceChart.draw(performanceData);
    attendanceChart.draw(attendanceData);
}
