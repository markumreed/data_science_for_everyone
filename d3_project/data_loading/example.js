function main() {
	// d3 code goes here
	// [CSV, TSV] -> DSV, JSON, XML
	// , ; : | \t
	// d3.dsv(',','../data/profiles.csv', d3.autoType).then(
	// 	function (d) {
	// 		for (let index = 0; index < d.length; index++) {
	// 			const element = d[index];
	// 			console.log(element.name);
	// 			console.log(element.age);
	// 		}
	// 	}	
	// )
	// d3.json('../data/profiles.json').then(
	// 	function (d) {
	// 		console.log(d);
	// 	}
	// )
	// d3.xml('../data/profiles.xml').then(
	// 	function (d) {
	// 		console.log(d);
	// 	}
	// )
	d3.dsv(',','../data/profiles.csv').then(
		function (d) {
			for (let index = 0; index < d.length; index++) {
				const element = d[index];
				d3.select('body').selectAll('p')
					.data(d)
					.enter()
					.append('p')
					.text(function(d){
						return d.name + ', ' + d.company
					})
			}
		}
	)
}