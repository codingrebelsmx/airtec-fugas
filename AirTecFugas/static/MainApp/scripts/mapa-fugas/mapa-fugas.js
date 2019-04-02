var point = null;
var svgPanZoomInstance = null;
var svgDrawInstance = null;
var svgId = "";
var listFugas = new Array();
var currentLeak = null;
var overLeak = false;

$(document).ready(function () {

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
        GetLeaks();
        //dummy data
        //DrawLeaks();
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
                callback: function callback(multiplier) {
                    //console.log(multiplier);
                    //console.log(1 / multiplier);
                    //var scaleF = 1 / multiplier;
                    //$(".punto-fuga").each(function (index, item) {
                    //    if (scaleF > 0.4)
                    //        item.instance.scale(scaleF, scaleF);
                    //});
                }
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

    function GetLeaks() {
        $.get("/api/fuga/point-list/", function (data, status) {
            listFugas = data;
            DrawLeaks();
            SetLeaksInfo();
        });
    }

    function DrawLeaks() {
        //var listFugas = [//Dummy data
        //    { id: 1, x: 793.3054809570312, y: -84.39212036132812 },
        //    { id: 2, x: 1036.989013671875, y: 244.66957092285156 },
        //    { id: 3, x: 2315.8828125, y: 650.2158813476562 }];
        for (var i = 0; i < listFugas.length; i++) {
            var fuga = listFugas[i];
            var circle = svgDrawInstance.circle(4);
            circle.move(fuga.punto_x, fuga.punto_y);
            circle.fill(GetColor(fuga.categoria));
            circle.addClass('punto-fuga');
            circle.attr('id', 'fuga-circle-' + fuga.id);
        }

        $(".punto-fuga").click(function () {
            overLeak = true;
            SetCurrentLeak(this);
            $("div.menu-actions-copy").remove();
            var html = $("#context-menu-fugas").html();
            var menuObj = $(html);
            menuObj.addClass('menu-actions-copy');
            menuObj.appendTo("body").css(
                {
                    top: event.pageY + "px",
                    left: event.pageX + "px",
                    display: "block",
                    position: "absolute"
                });
        });

        //$(".punto-fuga").hover(function (event) {
        //    SetCurrentLeak(this);

        //});
    }

    function GetColor(categoria) {
        var color = "#FF0000";//categoria 1
        if (categoria === 2)
            color = '#FF4000';
        else if (categoria === 3)
            color = '#FFFF00';
        return color;
    }

    function SetLeaksInfo() {
        var countP = $.grep(listFugas, function (n, i) { return n.estatus === 1; });
        var countR = $.grep(listFugas, function (n, i) { return n.estatus === 2; });
        $("#total-fugas").text(listFugas.length);
        $("#fugas-reparadas").text(countR.length);
        $("#fugas-pendientes").text(countP.length);
    }

    function SetCurrentLeak(obj) {
        var fugaId = $(obj).attr('id').replace("fuga-circle-", "");
        currentLeak = $.grep(listFugas, function (n, i) {
            return n.id === parseInt(fugaId);
        })[0];
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
        if (!overLeak)
            $("div.menu-actions-copy").remove();
        overLeak = false;
    });

    $(document).on("click", "div.custom-menu-copy", function () {
        console.log("x: " + point.x + " y:" + point.y);
        window.location = '/fuga/create/' + point.x + '/' + point.y + '/';
    });

    $(document).on("click", "li.btn-action-reparada", function () {
        console.log("Marcar como reparada fuga id: " + currentLeak.id);
        $("div.menu-actions-copy").remove();
    });

    $(document).on("click", "li.btn-action-detalles", function () {
        console.log("Mostrar foto fuga id: " + currentLeak.id);
        $("div.menu-actions-copy").remove();
        $.get('/fuga/corregida/' + currentLeak.id + '/', function (data, status) {
            $("#modal-fuga").append(data);
            $("#modal-fuga").modal('show');
        });
    });

    $(document).on("click", "li.btn-action-termica", function () {
        console.log("Mostrar Imgane termica fuga id: " + currentLeak.id);
        $("div.menu-actions-copy").remove();
    });
});