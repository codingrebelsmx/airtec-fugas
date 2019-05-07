// Bar Graph
$(function() {
	$("#barOne").sparkline([0,1,2,3,4,5,6,7,8,12,15,18,21,15,12,9,2], {
		type: 'bar',
		barColor: '#179978',
		barWidth: 6,
		height: 30,
	});
});

$(function(){
	$("#barTwo").sparkline([0,1,2,3,4,5,6,7,8,12,14,17,19,13,10,7,4], {
		type: 'bar',
		barColor: '#179978',
		barWidth: 6,
		height: 30,
	});
});