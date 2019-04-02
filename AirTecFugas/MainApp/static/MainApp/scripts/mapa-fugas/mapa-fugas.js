var point = null;
var svgPanZoomInstance = null;
var svgDrawInstance = null;
var svgId = "";

$(document).ready(function () {
    //var svg = document.getElementById("svg72055");
    //var pt = svg.createSVGPoint();
    //svg.addEventListener("mousedown", alert_click, false);
    //function alert_click(evt) {
    //    var cursorpt = cursorPoint(evt);
    //    console.log("(" + cursorpt.x + ", " + cursorpt.y + ")");
    //}
    //function cursorPoint(evt) {
    //    pt.x = evt.clientX;
    //    pt.y = evt.clientY;

    //        return pt.matrixTransform(svg.getScreenCTM().inverse());
    //}
    //$('#' + svgId).on("click", function (event) {
    //    var e = event.target;
    //    var dim = e.getBoundingClientRect();
    //    var x =  dim.left;
    //    var y =  dim.top;
    //    console.log("x: " + x + " y:" + y);
    //});

    $.get("/planta/plano/1/", function (data, status) {
        var svgObj = $(data).find('svg')[0];
        svgDrawInstance = SVG(svgObj);
        $("#SVGContainer").append(svgObj);
        svgId = svgObj.id;
        if (svgId === "") {
            svgId = "new-id-svg-planta";
            svgObj.id = svgId;
        }
        InitSVGControls();
        DrawLeaks();
    });

    function InitSVGControls() {
        svgPanZoomInstance = new SVGPanZoom($('#' + svgId)[0], {
            animationTime: 300,
            eventMagnet: $('#SVGContainer')[0],
            zoom: {
                factor: 0.25,
                minZoom: 1,
                maxZoom: 10,
                events: {
                    mouseWheel: true,
                    doubleClick: true,
                    pinch: true
                },
                callback: function callback(multiplier) { }
            },
            pan: {
                factor: 100,
                events: {
                    drag: true,
                    dragMouseButton: 1,
                    dragCursor: "move"
                },
                callback: function callback(coordinates) { }
            }
        });

        $("#" + svgId)[0].setAttribute('width', '100%');
        $("#" + svgId)[0].setAttribute('height', '80%');

        $("#zoom-in-button").click(function () {
            svgPanZoomInstance.zoomIn(null, 0.5);
        });

        $("#zoom-out-button").click(function () {
            svgPanZoomInstance.zoomOut(null, 0.5);
        });

        $("#reset-button").click(function () {
            svgPanZoomInstance.reset();
        });
    }

    function DrawLeaks() {
        //var fugas = [
        //    { x: 793.3054809570312, y: -84.39212036132812 },
        //    { x: 1036.989013671875, y: 244.66957092285156 },
        //    { x: 2315.8828125, y: 650.2158813476562 }];
        var fugas = [];
        for (var i = 0; i < fugas.length; i++) {
            var fuga = fugas[i];
            svgDrawInstance.circle(100).fill('#f06').move(fuga.x, fuga.y);
        }
    }
    $('div.main-content').css('padding', 0);
    $('div.main-content').css('min-height', 0);

    $("#SVGContainer").bind("contextmenu", function (event) {
        event.preventDefault();
        $("div.custom-menu-copy").remove();
        var html = $("#context-menu").html();
        var contextMenuObj = $(html);
        contextMenuObj.addClass('custom-menu-copy');
        contextMenuObj.appendTo("body").css(
            {
                top: event.pageY + "px",
                left: event.pageX + "px",
                display: "block"
            });

        var svg = document.getElementById(svgId);
        point = svg.createSVGPoint();
        point.x = event.pageX;
        point.y = event.pageY;
        point = point.matrixTransform(svg.getScreenCTM().inverse());
        console.log("x: " + point.x + " y:" + point.y);
    });

    $("div.custom-menu").bind("contextmenu", function (event) {
        event.preventDefault();
    });

    $("#SVGContainer").bind("click", function (event) {
        $("div.custom-menu-copy").remove();
    });


    $(document).on("click", "div.custom-menu-copy", function (event) {
        console.log("x: " + point.x + " y:" + point.y);
        window.location = '/fuga/create/' + point.x + '/' + point.y + '/';
    });
});