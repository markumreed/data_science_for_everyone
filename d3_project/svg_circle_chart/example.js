function main() {
	// d3 code goes here
	var width = 800
	var height = 800
	var data = [10, 15, 20, 25, 30, 35]
	var colors = ['#9C4F96', '#FF6355','#FBA949', '#FAE442', '#8BD448','#2AA8F2' ]
	
	var svg = d3.select('body')
			.append('svg')
			.attr('width',width )
			.attr('height', height);
	
	var group = svg.selectAll('g')
			.data(data)
			.enter().append('g')
			.attr('transform', function(d, i){
				return 'translate(0,0)';
			})
	group.append('circle')
		.attr('cx', function(d, i){
				return i * 100 + 50;
			})
		.attr('cy', function(d,i){
				return 100;
			})
		.attr('r', function(d){
				return d * 1.5;
			})
		.attr('fill', function(d, i){
				return colors[i];
			})
	group.append('text')
		.attr('x', function (d,i) {
			return i * 100 + 40;
		})
		.attr('y', 105)
		.attr('stroke', 'black')
		.attr('font-size', '20px')
		.attr('font-family', 'sans-serif')
		.text(function(d){
			return d;
		})

}