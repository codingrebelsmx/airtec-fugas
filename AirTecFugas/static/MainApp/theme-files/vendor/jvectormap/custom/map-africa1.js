// Africa
$(function(){
	$('#mapAfrica').vectorMap({
		map: 'africa_mill',
		backgroundColor: '#ffffff',
		scaleColors: ['#179978'],
		zoomOnScroll:false,
		zoomMin: 1,
		hoverColor: true,
		series: {
			regions: [{
				values: gdpData,
				scale: ['#179978', '#102f73'],
				normalizeFunction: 'polynomial'
			}]
		},
	});
});