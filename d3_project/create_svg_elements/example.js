function main() {
	// d3 code goes here
	var width = 500
	var height = 500
	// Create SVG element
	var svg = d3.select('body').append('svg')
			.attr("width", width)
			.attr("height", height)
	// svg.append('line')
	// 	.attr('x1', 100)
	// 	.attr('x2', 400)
	// 	.attr('y1', 40)
	// 	.attr('y2', 400)
	// 	.style('stroke', 'navy')

	// svg.append('rect')
	// 	.attr('x', 0)
	// 	.attr('y', 0)
	// 	.attr('width',100)
	// 	.attr('height', 200)
	// 	.style('fill','red')

	// svg.append('circle').attr('cx',250).attr('cy',50)
	// 	.attr('r', 40)
	// 	.attr('fill', 'red')
	// svg.append('ellipse').attr('cx',250).attr('cy',50)
	// .attr('rx', 150)
	// .attr('ry', 50)
	// .attr('fill', 'red')
	var g = svg.append('g')
			.attr('transform', function (d, i) {
				return 'translate(0,0)';
			})
	var circ  = g.append('circle')
	.attr('cx', 250)
	.attr('cy', 50)
	.attr('r', 150)
	.attr('fill', 'red')
	.attr('opacity', 0.5)

	g.append('text')
	.attr('x', 200)
	.attr('y', 50)
	.attr('stroke', 'black')
	.attr('font-family', 'sans-serif')
	.attr('font-size', '24px')
	.text('DANGER');
}