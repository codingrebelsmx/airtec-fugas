var chart9 = c3.generate({
	bindto: '#pieChart',
	data: {
		// iris data from R
		columns: [
			['Likes', 36],
			['Shares', 5],
		],
		type : 'pie',
		colors: {
			Likes: '#179978',
			Shares: '#ef2f1a'
		},
		onclick: function (d, i) { console.log("onclick", d, i); },
		onmouseover: function (d, i) { console.log("onmouseover", d, i); },
		onmouseout: function (d, i) { console.log("onmouseout", d, i); }
	}
});