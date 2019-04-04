var point = null;
var svgPanZoomInstance = null;
var svgDrawInstance = null;
var svgId = "";
var listFugas = new Array();
var currentLeak = null;
var overLeak = false;
var leakImages = new Array();
var currentImageIndex = 0;
var timer;
var counter = 0;

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
            var circle = svgDrawInstance.circle(2);
            circle.move(fuga.punto_x, fuga.punto_y);
            circle.fill(GetColor(fuga.categoria, fuga.estatus));
            circle.addClass('punto-fuga');
            circle.attr('id', 'fuga-circle-' + fuga.id);
        }

        function HandleClickFugaPoint(obj, event) {
            overLeak = true;
            SetCurrentLeak(obj);
            $("div.custom-menu-copy").remove();
            $("div.menu-actions-copy").remove();
            var html = $("#context-menu-fugas").html();
            var menuObj = $(html);
            var x = event.pageX;
            var y = event.pageY;
            if (x === undefined || y === undefined) {
                x = event.touches[event.touches.length - 1].pageX;
                y = event.touches[event.touches.length - 1].pageY;
            }
            menuObj.addClass('menu-actions-copy');
            menuObj.appendTo("body").css(
                {
                    top: y + "px",
                    left: x + "px",
                    display: "block",
                    position: "absolute"
                });
        }

        $('.punto-fuga').on('touchstart', function (ev) {
            HandleClickFugaPoint(this, ev);
        });
        $(".punto-fuga").click(function (ev) {
            HandleClickFugaPoint(this, ev);
        });

        //$(".punto-fuga").hover(function (event) {
        //    SetCurrentLeak(this);

        //});
    }

    function GetColor(categoria, estatus) {
        if (estatus === 2)//estatus corregida
            return '#00FF00';
        var color = '#FF0000';//categoria 1
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

    //$("#SVGContainer").taphold(function (event) {
    //    event.preventDefault();
    //    SetPointLeak(event);
    //});
    //$("#SVGContainer").doubletap( function (event) {
    //    SetPointLeak(event);
    //});

    //var counter = 0,
    //    timer;

    //$("#resumen-fugas").on('touchstart', function (ev) {
    //    timer = setInterval(function () {
    //        counter++;
    //        $('#div-preuba').text('touched ' + counter);
    //        if (counter === 2)
    //            alert('ora perro');
    //    }, 250); // 250ms interval
    //    return false;
    //});
    //$("#resumen-fugas").on('touchend', function (ev) {
    //    clearInterval(timer);
    //    counter = 0;
    //    return false;
    //});

    $("#SVGContainer").on('touchstart', function (ev) {
        if (event.touches.length === 1) {
            timer = setInterval(function () {
                counter++;
                //$('#div-preuba').text('touched' + counter);
                if (counter === 2)
                    SetPointLeak(ev);
            }, 250); // 250ms interval
        } else
            console.log('Nel perro ' + event.touches.length);
        return false;
    });
    $("#SVGContainer").on('touchend', function (ev) {
        console.log('Touchend ' );
        clearInterval(timer);
        counter = 0;
        return false;
    });
    //$('#SVGContainer').on("mousedown", function (event) {
    //    var mouseE = event;
    //    timer = setTimeout(function () {
    //        SetPointLeak(mouseE);
    //    }, 1 * 1000);
    //}).on("mouseup mouseleave", function () {
    //    clearTimeout(timer);
    //});

    $("#SVGContainer").on("contextmenu", function (event) {
        console.log('context menu');
        event.preventDefault();
        SetPointLeak(event);
    });

    function SetPointLeak(event) {
        $("div.custom-menu-copy").remove();
        $("div.menu-actions-copy").remove();
        var html = $("#context-menu").html();
        var contextMenuObj = $(html);
        contextMenuObj.addClass('custom-menu-copy');
        var x = event.pageX;
        var y = event.pageY;
        if (x === undefined || y === undefined) {
            x = event.touches[event.touches.length - 1].pageX;
            y = event.touches[event.touches.length - 1].pageY;
        }
        contextMenuObj.appendTo("body").css(
            {
                top: y + "px",
                left: x + "px",
                display: "block"
            });

        var svg = document.getElementById(svgId);
        point = svg.createSVGPoint();
        point.x = x;
        point.y = y;
        point = point.matrixTransform(svg.getScreenCTM().inverse());
        console.log("x: " + point.x + " y:" + point.y);
    }

    function UpdateLeakColor() {
        $('#fuga-circle-' + currentLeak.id).fill('#00FF00');
    }

    $("div.custom-menu").bind("contextmenu", function (event) {
        event.preventDefault();
    });

    $("#SVGContainer").bind("click", function (event) {
        console.log('svgcontainer click');
        $("div.custom-menu-copy").remove();
        if (!overLeak)
            $("div.menu-actions-copy").remove();
        overLeak = false;
    });

    $(document).on("click", "div.custom-menu-copy", function () {
        console.log("x: " + point.x + " y:" + point.y);
        window.location = '/fuga/create/' + point.x + '/' + point.y + '/';
    });

    $(document).on("click", "li.btn-action-detalles", function () {
        $("div.menu-actions-copy").remove();
        $.get('/fuga/corregida/' + currentLeak.id + '/', function (data, status) {
            $("#modal-fuga-body").empty().append(data);
            InitForm("idFormCorregirUpdateFuga", null, function () {
                $LoadingBlockUI.fadeIn(750);
                window.location = "/mapa-fugas/";
            });
        });
    });

    $(document).on("click", "li.btn-action-reparada", function () {
        console.log("Marcar como reparada fuga id: " + currentLeak.id);
        $("div.menu-actions-copy").remove();
    });

    $(document).on("click", "li.btn-action-images", function () {
        console.log("Mostrar imagenes fuga id: " + currentLeak.id);
        $("div.menu-actions-copy").remove();
        $.get('/fuga/imagenes/' + currentLeak.id + '/', function (data, status) {
            LoadImagesModal(data);
        });
        //'/imagen-fuga/detail/<pk_imagen_fuga>/'
    });

    function LoadImagesModal(images) {
        leakImages = images;
        ShowImagesModal();
        //$.each(images, function (index, item) {
        //    console.log(item.url);
        //    $.get(item.url, function (data, status) {
        //        leakImages.push(data);
        //        if (leakImages.length === images.length)
        //            ShowImagesModal();
        //    });
        //});
    }

    function ShowImagesModal() {
        currentImageIndex = 0;
        if (leakImages.length > 0) {
            $("#img-dynamic").attr('src', leakImages[currentImageIndex].url);
            $("#modal-images").removeClass('d-none');
        }
    }
    $('#change-image-left').click(function () {
        if (currentImageIndex > 0)
            currentImageIndex--;
        else
            currentImageIndex = leakImages.length - 1;
        $("#img-dynamic").attr('src', leakImages[currentImageIndex].url);
    });

    $('#change-image-right').click(function () {
        if (currentImageIndex < leakImages.length - 1)
            currentImageIndex++;
        else
            currentImageIndex = 0;
        $("#img-dynamic").attr('src', leakImages[currentImageIndex].url);
    });

    $("#close-image-modal").click(function () {
        $("#modal-images").addClass('d-none');
    });
});