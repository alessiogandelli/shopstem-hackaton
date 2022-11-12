



anychart.onDocumentReady(function () {
    //anychart.data.loadJsonFile("https://raw.githubusercontent.com/alessiogandelli/shopstem-hackaton/main/src/dashboard/got_graph.json", function (data) {

    // create a chart from the loaded data
    //var chart = anychart.graph(data);




    var data = {
        "nodes": [
            {
                "id": "ingresso", "x": 0, "y": 0, "normal": { "height": 40, "fill": "#ffa000", "stroke": null }
            },
            {
                "id": "pantaloni uomo", "x": 0, "y": 100, "normal": { "height": 20, "fill": "#ffa000", "stroke": null }
            },
            {
                "id": "pantaloni donna", "x": 100, "y": 100, "normal": { "height": 50, "fill": "#ffa000", "stroke": null }
            },
            {
                "id": "magliette uomo", "x": 0, "y": 200, "normal": { "height": 10, "fill": "#ffa000", "stroke": null }
            },
            {
                "id": "magliette donna", "x": 100, "y": 200, "normal": { "height": 20, "fill": "#ffa000", "stroke": null }
            },
            {
                "id": "bambino", "x": 200, "y": 300, "normal": { "height": 40, "fill": "#ffa000", "stroke": null }
            },
            {
                "id": "scarpe uomo", "x": 0, "y": 300, "normal": { "height": 70, "fill": "#ffa000", "stroke": null }
            },
            {
                "id": "scarpe donna", "x": 100, "y": 300, "normal": { "height": 10, "fill": "#ffa000", "stroke": null }
            },
            {
                "id": "scarpe bambino", "x": 200, "y": 300, "normal": { "height": 100, "fill": "#ffa000", "stroke": null }
            },
            {
                "id": "accessori", "x": 100, "y": 0, "normal": { "height": 30, "fill": "#ffa000", "stroke": null }
            },
            {
                "id": "uscita", "x": 200, "y": 0, "normal": { "height": 70, "fill": "#ffa000", "stroke": null }
            }
        ],
        "edges": [
            {
                "from": "ingresso",
                "to": "pantaloni uomo"
            },
            {
                "from": "ingresso",
                "to": "accessori", normal: {
                    "stroke": {
                        "color": "#ffa000",
                        "thickness": "8",

                        "lineJoin": "round"
                    }
                },
                hovered: {
                    stroke: {
                        color: "#ffa000",
                        thickness: "4",
                        dash: "10 5",
                        lineJoin: "round"
                    }
                },
                selected: { stroke: "4 #ffa000" }
            
            },
        {
            "from": "pantaloni uomo",
            "to": "accessori"
            },
        {
            "from": "pantaloni uomo",
            "to": "maglie uomo", "normal": { "thickness": 70, "fill": "#ffa000" }
        },
        {
            "from": "accessori",
            "to": "pantaloni donna"
            },
        {
            "from": "pantaloni donna",
            "to": "magliette donna"
            },
        {
            "from": "magliette uomo",
            "to": "scarpe uomo",


        },
        {
            "from": "magliette donna",
            "to": "bambino"
            },
        {
            "from": "magliette donna",
            "to": "scarpe bambino"
            },
        {
            "from": "magliette donna",
            "to": "scarpe donna"
            },
        {
            "from": "scarpe donna",
            "to": "scarpe uomo"
            },
        {
            "from": "scarpe donna",
            "to": "bambino"
            },
        {
            "from": "scarpe donna",
            "to": "scarpe bambino"
            },
        {
            "from": "bambino",
            "to": "scarpe bambino"
            },
        {
            "from": "scarpe bambino",
            "to": "uscita"
            }


        ]
    };


    // set the title
    var chart = anychart.graph();
    chart.data(data);
    chart.title().enabled(true).text('Fixed layout');
    chart.nodes().labels().enabled(true);
    var layout = chart.layout();

    layout.type('fixed');

    chart.container('container').draw();

});

