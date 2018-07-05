import * as array from 'd3-array';
import * as scale from 'd3-scale';
import * as selection from 'd3-selection';
import * as axis from 'd3-axis';

const data = [
  { name: 'user1', value: 4 },
  { name: 'user2', value: 8 },
  { name: 'user3', value: 15 },
  { name: 'user4', value: 67 },
  { name: 'user5', value: 23 },
  { name: 'user6', value: 57 },
  { name: 'user7', value: 50 },
  { name: 'user8', value: 53 },
  { name: 'user9', value: 42 },
  { name: 'user10', value: 16 },
];

const svg = selection.select('svg');
const margin = { top: 20, right: 20, bottom: 30, left: 40 };
const width = +svg.attr('width') - margin.left - margin.right;
const height = +svg.attr('height') - margin.top - margin.bottom;

const x = scale
  .scaleBand()
  .rangeRound([0, width])
  .padding(0.1);
const y = scale.scaleLinear().rangeRound([height, 0]);

x.domain(data.map(d => d.name));
y.domain([0, array.max(data, d => d.value)]);

const g = svg
  .append('g')
  .attr('transform', `translate(${margin.left}, ${margin.top})`);

g.append('g')
  .attr('class', 'axis axis--x')
  .attr('transform', `translate(0,${height})`)
  .call(axis.axisBottom(x));

g.append('g')
  .attr('class', 'axis axis--y')
  .call(axis.axisLeft(y).ticks(10))
  .append('text')
  .attr('transform', 'rotate(-90)')
  .attr('y', 6)
  .attr('dy', '0.71em')
  .attr('text-anchor', 'end')
  .attr('fill', 'black')
  .text('Count');

g.selectAll('.bar')
  .data(data)
  .enter()
  .append('rect')
  .attr('class', 'bar')
  .attr('x', d => x(d.name))
  .attr('y', d => y(d.value))
  .attr('width', x.bandwidth())
  .attr('height', d => height - y(d.value));

g.selectAll('.text')
  .data(data)
  .enter()
  .append('text')
  .attr('class', 'text')
  .attr('x', d => x(d.name) + x.bandwidth() / 2)
  .attr('y', d => y(d.value) + 3)
  .attr('dx', '0.75em')
  .attr('dy', '0.75em')
  .text(d => d.value);
