

var serverUrlXZ = "http://15.15.11.141:6080/arcgis/rest/services/xiangzhen/MapServer/0";
var serverUrlCun = "http://15.15.11.141:6080/arcgis/rest/services/cun/MapServer/0";

require([ "../ArcGis4.7/esri/tasks/QueryTask", "../ArcGis4.7/esri/tasks/support/Query", "../ArcGis4.7/esri/geometry/Point"], 
function (QueryTask, Query, Point) {
    console.log('3333333333');

    var p = new Point({
        x:"111.46611", y:"27.93305"
    });

    var query = new Query({
        where:"CITY = '娄底市'",
        geometry: p,
        returnGeometry: true,
        outFields:'NAME'
    });

    var queryTaskXZ = new QueryTask({
        url:serverUrlXZ
    });
    queryTaskXZ.execute(query).then(function(results){
        console.log('查询完成----------------------');
        if(results.features.length>0){
            var dd = results.features[0].attributes['NAME'];
            console.log(dd);
        }
    });

    var queryTaskCun = new QueryTask({
        url:serverUrlCun
    });
    queryTaskCun.execute(query).then(function(results){
        console.log('查询完成----------------------');
        if(results.features.length>0){
            var dd = results.features[0].attributes['NAME'];
            console.log(dd);
        }
    });

    alert('ok!');
});