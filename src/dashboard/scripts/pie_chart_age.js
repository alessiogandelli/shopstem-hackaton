anychart.onDocumentReady(function () {

    // create data
    var data = [
     {x: "<18", value: 127, 
     fill: "#f44336",
     hatchFill: "percent50"        
     },  
      {x: "18-25", value: 203, 
     fill: "#ff00a6",
     hatchFill: "percent50"        
      },
      {x: "26-40", value: 365, 
     fill: "#ffd966",
     hatchFill: "percent50"        
      },
      {x: "41-55", value: 482, 
     fill: "#0084ff",
     hatchFill: "percent50"        
      },
      {x: "50-70", value: 613, 
     fill: "#0b5394",
     hatchFill: "percent50"        
      },
      {x: ">70", value: 311, 
     fill: "#58f7cd",
     hatchFill: "percent50"        
      },
    ];

    // create a chart and set the data
    var chart = anychart.pie(data);

    // set the chart title
    chart.title("Pie Chart: Age Based");

    // set the container id
    chart.container("container");

    // initiate drawing the chart
    chart.draw();
});