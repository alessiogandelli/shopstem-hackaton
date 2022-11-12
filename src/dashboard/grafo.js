



anychart.onDocumentReady(function () {
    //anychart.data.loadJsonFile("https://raw.githubusercontent.com/alessiogandelli/shopstem-hackaton/main/src/dashboard/got_graph.json", function (data) {

    // create a chart from the loaded data
    //var chart = anychart.graph(data);




    var data = {"nodes": [{"id": "Entrance", "x": 0, "y": 0, "fill": {"src": "imgs/log-in.png"}, "normal": {"height": 0.9141889902855461}}, {"id": "Pants Man", "x": 0, "y": 100, "fill": {"src": "imgs/pants m.png"}, "normal": {"height": 1.0}}, {"id": "Shirt Man", "x": 0, "y": 200, "fill": {"src": "imgs/shirt m.png"}, "normal": {"height": 0.542022372681778}}, {"id": "Shoes Man", "x": 0, "y": 300, "fill": {"src": "imgs/shoe m.png"}, "normal": {"height": 0.4447306446864881}}, {"id": "Pants Woman", "x": 100, "y": 100, "fill": {"src": "imgs/pants w.png"}, "normal": {"height": 0.5127808850946914}}, {"id": "Shirt Woman", "x": 100, "y": 200, "fill": {"src": "imgs/shirt w.png"}, "normal": {"height": 0.7143803355902266}}, {"id": "Shoes Woman", "x": 100, "y": 300, "fill": {"src": "imgs/shoe w.png"}, "normal": {"height": 0.6713767049357277}}, {"id": "Kids", "x": 300, "y": 300, "fill": {"src": "imgs/kids.png"}, "normal": {"height": 0.48400549504464724}}, {"id": "Shoes Kids", "x": 300, "y": 200, "fill": {"src": "imgs/shoe k.png"}, "normal": {"height": 0.4985526444902365}}, {"id": "Accessories", "x": 200, "y": 0, "fill": {"src": "imgs/accessories.png"}, "normal": {"height": 0.9745608870572073}}, {"id": "Exit", "x": 300, "y": 0, "fill": {"src": "imgs/log-out.png"}, "normal": {"height": 0.8125797272102836}}], "edges": [{"from": "Entrance", "to": "Pants Man", "normal": {"stroke": {"thickness": 0.9996389239935006}}}, {"from": "Entrance", "to": "Accessories", "normal": {"stroke": {"thickness": 1.0}}}, {"from": "Pants Man", "to": "Shirt Man", "normal": {"stroke": {"thickness": 0.8385990250947825}}}, {"from": "Pants Man", "to": "Accessories", "normal": {"stroke": {"thickness": 0.9200216645603899}}}, {"from": "Shirt Man", "to": "Shoes Man", "normal": {"stroke": {"thickness": 0.6956129265210327}}}, {"from": "Shoes Man", "to": "Shoes Woman", "normal": {"stroke": {"thickness": 0.5641812601552627}}}, {"from": "Pants Woman", "to": "Accessories", "normal": {"stroke": {"thickness": 0.8216284527893122}}}, {"from": "Pants Woman", "to": "Shirt Woman", "normal": {"stroke": {"thickness": 0.5822350604802311}}}, {"from": "Shirt Woman", "to": "Shoes Woman", "normal": {"stroke": {"thickness": 0.4872720707708973}}}, {"from": "Shirt Woman", "to": "Kids", "normal": {"stroke": {"thickness": 0.47300956851417225}}}, {"from": "Shirt Woman", "to": "Shoes Kids", "normal": {"stroke": {"thickness": 0.4264307636757537}}}, {"from": "Shoes Woman", "to": "Kids", "normal": {"stroke": {"thickness": 0.45242823614370825}}}, {"from": "Shoes Woman", "to": "Shoes Kids", "normal": {"stroke": {"thickness": 0.4112655714027803}}}, {"from": "Kids", "to": "Shoes Kids", "normal": {"stroke": {"thickness": 0.3997111391948005}}}, {"from": "Shoes Kids", "to": "Exit", "normal": {"stroke": {"thickness": 0.18089907925618343}}}]}    // set the title
    var chart = anychart.graph();
    chart.data(data);
    chart.title().enabled(true).text('Fixed layout');
    chart.nodes().labels().enabled(true);
    var layout = chart.layout();

    layout.type('fixed');

    chart.container('container').draw();

});

