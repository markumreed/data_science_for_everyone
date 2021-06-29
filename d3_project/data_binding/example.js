function main() {
	// d3 code goes here
	// var myData = [1,2,3,4,5,6,7,8,9,10]
	// d3.select("body")
	// 	.selectAll("span")
	// 	.data(myData)
	// 	.enter() // Dynamically create placeholders
	// 	.append("span")
	// 	.style('color', function(d) {
	// 		if (d % 3 ===0){
	// 			return "red"
	// 		} else {
	// 			return "blue"
	// 		}
	// 	})
	// 	.text(function(d){ 
	// 		return d;
	// 	})


	// var mat = [
	// 	[1,2,3,4],
	// 	[5,6,7,8],
	// 	[9,10,11,12],
	// 	[13,14,15,16]
	// ];

	// var tr = d3.select("body")
	// 		.append("table")
	// 		.selectAll("tr")
	// 		.data(mat)
	// 		.enter()
	// 		.append("tr"); // create tr placeholder

	// var td = tr.selectAll("td")
	// 		.data(function(d){
	// 			return d;
	// 		})
	// 		.enter()
	// 		.append("td")
	// 		.style('color', function(d){
	// 			if (d % 2 === 0){
	// 				return 'red'
	// 			} else {
	// 				return 'blue'
	// 			}
	// 		})
	// 		.text(function(d){
	// 			return d;
	// 		})
	// var myData = ["Hello Everyone!"]
	// d3.select("body")
	// 	.selectAll("p")
	// 	.data(myData)
	// 	.text(function(d){
	// 		return d;
	// 	})
	// 	.exit()
	// 	.remove();
	d3.select("body")
		.select("p")
		.datum()
		.text(function (d, i){
			return 'His power is over ' + d;
		})
}