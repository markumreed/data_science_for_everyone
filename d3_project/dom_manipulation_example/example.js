function main() {
	// d3 code goes here
	// text Method
	// d3.select("p")
	// 	.text("This is a paragraph!")
	// append Method
	// d3.select("body").append("p")
	// 	.text("Yay! Third paragraph!")
	//  insert Method
	// d3.select("div").insert("p")
	// 	.text("HERE IS MY NEW PARAGRAPH!!!!!")
	// remove Method
	// d3.select("p").remove()
	// html Method
	// d3.select("p").html("<em>We changed the paragraph</em>");
	// attr Method 
	// d3.select("p").attr("class", "error")
	// property Method
	// d3.selectAll("input").property("checked", true)
	// style Method
	// d3.select("p").style("color", "aqua");
	// classed Method
	d3.select("p").classed("error", true)
}