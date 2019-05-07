var chart12 = c3.generate({
	bindto: '#pieChart1',
	data: {
		// iris data from R
		columns: [
			['Mon', 219],
			['Tue', 167],
			['Wed', 115],
			['Thu', 87],
			['Fri', 60],
			['Sat', 30],
		],
		type : 'pie',
		colors: {
			Mon: '#0f8264',
			Tue: '#179978',
			Wed: '#24b38e',
			Thu: '#3dc7a4',
			Fri: '#53ceaf',
			Sat: '#e5e8f2',
		},
		onclick: function (d, i) { console.log("onclick", d, i); },
		onmouseover: function (d, i) { console.log("onmouseover", d, i); },
		onmouseout: function (d, i) { console.log("onmouseout", d, i); }
	},
});