$(document).ready(function () {

    var svgPlanta = new SVGPanZoom($('#svg72055')[0], {
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

    $("#svg72055")[0].setAttribute('width', '100%');
    $("#svg72055")[0].setAttribute('height', '80%');
    $('div.main-content').css('padding', 0);
    $('div.main-content').css('min-height', 0);
});