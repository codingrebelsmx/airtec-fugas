$( document ).ready(function() {
	$("#likes").circliful({
		animation: 1,
		animationStep: 5,
		foregroundBorderWidth: 7,
		backgroundBorderWidth: 5,
		percent: 78,
		fontColor: '#8f93a0',
		foregroundColor: '#cbac7b',
		backgroundColor: '#343747',
		multiPercentage: 1,
		percentages: [10, 20, 30],
	});
	$("#shares").circliful({
		animation: 1,
		animationStep: 5,
		foregroundBorderWidth: 7,
		backgroundBorderWidth: 5,
		percent: 65,
		fontColor: '#8f93a0',
		foregroundColor: '#cbac7b',
		backgroundColor: '#343747',
		multiPercentage: 1,
		percentages: [10, 20, 30],
	});
	$("#comments").circliful({
		animation: 1,
		animationStep: 5,
		foregroundBorderWidth: 7,
		backgroundBorderWidth: 5,
		percent: 85,
		fontColor: '#8f93a0',
		foregroundColor: '#cd7979',
		backgroundColor: '#343747',
		multiPercentage: 1,
		percentages: [10, 20, 30],
	});

});