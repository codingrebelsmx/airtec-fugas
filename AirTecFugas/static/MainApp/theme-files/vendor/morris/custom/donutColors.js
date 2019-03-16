// Morris Donut
Morris.Donut({
	element: 'donutColors',
	data: [
		{value: 70, label: 'foo'},
		{value: 15, label: 'bar'},
		{value: 10, label: 'baz'},
		{value: 5, label: 'A really really long label'}
	],
	backgroundColor: '#ffffff',
	labelColor: '#666666',
	colors:['#cbac7b', '#e5e8f2', '#ff5661'],
	resize: true,
	hideHover: "auto",
	gridLineColor: "#585e6f",
	formatter: function (x) { return x + "%"}
});