// Denmark
$(function(){
	$('#mapDenmark').vectorMap({
		map: 'dk_mill',
		zoomOnScroll: false,
		regionStyle:{
			initial: {
				fill: '#179978',
			},
			hover: {
				"fill-opacity": 0.8
			},
			selected: {
				fill: '#ef2f1a'
			},
		},
		backgroundColor: '#ffffff',
	});
});