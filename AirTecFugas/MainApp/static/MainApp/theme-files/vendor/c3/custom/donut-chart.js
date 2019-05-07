var chart10 = c3.generate({
	bindto: '#donutChart',
	data: {
		columns: [
			['Likes', 12],
			['Shares', 87],
			['Clicks', 51],
		],
		type : 'donut',
		colors: {
			Likes: '#179978',
			Shares: '#ef2f1a',
			Clicks: '#666f6d',
		},
		onclick: function (d, i) { console.log("onclick", d, i); },
		onmouseover: function (d, i) { console.log("onmouseover", d, i); },
		onmouseout: function (d, i) { console.log("onmouseout", d, i); }
	},
	donut: {
		title: "Clicks"
	},
});