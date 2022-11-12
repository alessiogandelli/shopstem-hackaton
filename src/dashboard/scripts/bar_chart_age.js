anychart.onDocumentReady(function () {

    // create a data set
    var data = anychart.data.set([
      ["18-25", 90, 113],
      ["26-40", 182, 183],
      ["41-55", 315, 167],
      ["50-70", 211, 402],
      [">70", 183, 128]
    ]);

    // map the data
    var seriesData_1 = data.mapAs({x: 0, value: 1});
    var seriesData_2 = data.mapAs({x: 0, value: 2});

    // create a chart
    var chart = anychart.bar();

    chart.barsPadding(0)

    // create the first series, set the data and name
    var series1 = chart.bar(seriesData_1);
    series1.name("Males");

    // configure the visual settings of the first series
    series1.normal().fill("#0066cc", 0.3)
    series1.normal().fill("#0066cc", 0.3);
    series1.hovered().fill("#0066cc", 0.1);
    series1.selected().fill("#0066cc", 0.5);
    series1.normal().stroke("#0066cc", 1, "10 5", "round");
    series1.hovered().stroke("#0066cc", 2, "10 5", "round");
    series1.selected().stroke("#0066cc", 4, "10 5", "round");

    // create the second series, set the data and name
    var series2 = chart.bar(seriesData_2);
    series2.name("Females");

    // configure the visual settings of the second series
    series2.normal().fill("#cc0096", 0.3)
    series2.normal().fill("#cc0096", 0.3);
    series2.hovered().fill("#cc0096", 0.1);
    series2.selected().fill("#cc0096", 0.5);
    series2.normal().hatchFill("forward-diagonal", "#cc0096", 1, 15);
    series2.hovered().hatchFill("forward-diagonal", "#cc0096", 1, 15);
    series2.selected().hatchFill("forward-diagonal", "#cc0096", 1, 15);
    series2.normal().stroke("#cc0096");
    series2.hovered().stroke("#cc0096", 2);
    series2.selected().stroke("#cc0096", 4);

    // set the chart title
    chart.title("Bar Chart: Ages and Sex");

    // set the titles of the axes
    chart.xAxis().title("Age Group");
    chart.yAxis().title("n");

    // set the container id
    chart.container("container");

    // initiate drawing the chart
    chart.draw();
});
