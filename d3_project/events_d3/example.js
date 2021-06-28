function main() {
	// d3 code goes here
	d3.selectAll("div")
		.on("mouseover", function(){
			d3.select(this)
				.style("background-color","firebrick")
		})
		.on("mouseout", function(){
			d3.select(this)
				.style("background-color", "navy")
		})
}