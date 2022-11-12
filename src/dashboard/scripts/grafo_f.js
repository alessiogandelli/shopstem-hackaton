



anychart.onDocumentReady(function () {
    anychart.data.loadJsonFile("https://raw.githubusercontent.com/alessiogandelli/shopstem-hackaton/main/src/graphs/graph_f.json", function (data) {

       // create a chart from the loaded data
       var chart = anychart.graph(data);


    
        // var data = {"nodes": [{"id": "Entrance", "x": 0, "y": 0, "fill": {"src": "imgs/log-in.png"}, "normal": {"height": 45.7094495142773}}, {"id": "Pants Man", "x": 0, "y": 100, "fill": {"src": "imgs/pants m.png"}, "normal": {"height": 50.0}}, {"id": "Shirt Man", "x": 0, "y": 200, "fill": {"src": "imgs/shirt m.png"}, "normal": {"height": 27.1011186340889}}, {"id": "Shoes Man", "x": 0, "y": 300, "fill": {"src": "imgs/shoe m.png"}, "normal": {"height": 22.236532234324404}}, {"id": "Pants Woman", "x": 100, "y": 100, "fill": {"src": "imgs/pants w.png"}, "normal": {"height": 25.63904425473457}}, {"id": "Shirt Woman", "x": 100, "y": 200, "fill": {"src": "imgs/shirt w.png"}, "normal": {"height": 35.71901677951133}}, {"id": "Shoes Woman", "x": 100, "y": 300, "fill": {"src": "imgs/shoe w.png"}, "normal": {"height": 33.568835246786385}}, {"id": "Kids", "x": 300, "y": 300, "fill": {"src": "imgs/kids.png"}, "normal": {"height": 24.20027475223236}}, {"id": "Shoes Kids", "x": 300, "y": 200, "fill": {"src": "imgs/shoe k.png"}, "normal": {"height": 24.927632224511825}}, {"id": "Accessories", "x": 200, "y": 0, "fill": {"src": "imgs/accessories.png"}, "normal": {"height": 48.728044352860366}}, {"id": "Exit", "x": 300, "y": 0, "fill": {"src": "imgs/log-out.png"}, "normal": {"height": 40.62898636051418}}], "edges": [{"from": "Entrance", "to": "Pants Man", "normal": {"stroke": {"thickness": 9.996389239935006}}}, {"from": "Entrance", "to": "Accessories", "normal": {"stroke": {"thickness": 10.0}}}, {"from": "Pants Man", "to": "Shirt Man", "normal": {"stroke": {"thickness": 8.385990250947824}}}, {"from": "Pants Man", "to": "Accessories", "normal": {"stroke": {"thickness": 9.200216645603899}}}, {"from": "Shirt Man", "to": "Shoes Man", "normal": {"stroke": {"thickness": 6.956129265210327}}}, {"from": "Shoes Man", "to": "Shoes Woman", "normal": {"stroke": {"thickness": 5.641812601552627}}}, {"from": "Pants Woman", "to": "Accessories", "normal": {"stroke": {"thickness": 8.216284527893121}}}, {"from": "Pants Woman", "to": "Shirt Woman", "normal": {"stroke": {"thickness": 5.8223506048023115}}}, {"from": "Shirt Woman", "to": "Shoes Woman", "normal": {"stroke": {"thickness": 4.872720707708973}}}, {"from": "Shirt Woman", "to": "Kids", "normal": {"stroke": {"thickness": 4.730095685141722}}}, {"from": "Shirt Woman", "to": "Shoes Kids", "normal": {"stroke": {"thickness": 4.264307636757537}}}, {"from": "Shoes Woman", "to": "Kids", "normal": {"stroke": {"thickness": 4.524282361437082}}}, {"from": "Shoes Woman", "to": "Shoes Kids", "normal": {"stroke": {"thickness": 4.112655714027803}}}, {"from": "Kids", "to": "Shoes Kids", "normal": {"stroke": {"thickness": 3.997111391948005}}}, {"from": "Shoes Kids", "to": "Exit", "normal": {"stroke": {"thickness": 1.8089907925618343}}}]}

        var chart = anychart.graph();
        chart.data(data);
        chart.title().enabled(true).text('Fixed layout');
        chart.nodes().labels().enabled(true);
        var nodes = chart.nodes();
        nodes.normal().stroke(null);
        
        var layout = chart.layout();
        layout.type('fixed');
        chart.container('container').draw();
 
    
});

});
