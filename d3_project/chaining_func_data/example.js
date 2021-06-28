function main() {
	// d3 code goes here
	// var datArr = [6,5,4,3,2,1,0]
	// d3.select("body")
	// 	.selectAll("p")
	// 	.data(datArr)
	// 	.text(function(d, i) {
	// 		console.log("d: " + d);
	// 		console.log("i: " + i);
	// 		return "Data point "+i+" is " + d;
	// 	});
	d3.select("body")
		.selectAll("p")
		.style("background", function(d, i){
		var text = this.innerText;

		if (text.indexOf("Warning")>=0){
			return "orange";
		} else if (text.indexOf("Danger")>=0) {
			return "red"
		}
	})
}