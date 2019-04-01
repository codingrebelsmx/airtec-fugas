var pt = null;
var svgId = 'svg72055';
$(document).ready(function () {
    var point = { x: 0, y: 0 };
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
        svgId = $(data).find('svg')[0].id;
        InitSVGControls();
    });

    function InitSVGControls() {
        var svgPlanta = new SVGPanZoom($('#' + svgId)[0], {
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
        point.x = event.pageX;
        point.y = event.pageY;
        var svg = document.getElementById(svgId);
        pt = svg.createSVGPoint();
        pt.x = event.pageX;
        pt.y = event.pageY;
        pt = pt.matrixTransform(svg.getScreenCTM().inverse());
        console.log("x: " + pt.x + " y:" + pt.y);

    });

    $("div.custom-menu").bind("contextmenu", function (event) {
        event.preventDefault();
    });

    $("#SVGContainer").bind("click", function (event) {
        $("div.custom-menu-copy").remove();
    });


    $(document).on("click", "div.custom-menu-copy", function (event) {
        console.log("x: " + pt.x + " y:" + pt.y);
        window.location = '/fuga/create/' + pt.x + '/' + pt.y + '/';
    });
});