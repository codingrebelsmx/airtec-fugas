// Europe
$(function(){
	$('#mapEurope').vectorMap({
		map: 'europe_mill',
		zoomOnScroll: false,
		series: {
			regions: [{
				values: gdpData,
				scale: ['#cbac7b', '#333333'],
				normalizeFunction: 'polynomial'
			}]
		},
		backgroundColor: '#3f4455',
	});
});