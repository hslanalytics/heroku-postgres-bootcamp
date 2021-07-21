
// Create the data array for the plot
var tv_data = d3.json("api/tv.json")
//var tv_data = "/api/tv.json";

console.log(tv_data);

var x = tv_data.name

var y = tv_data.hours

var trace = {
    x: x,
    y: y,
    type: "bar"
};

var data = [trace];

// Define the plot layout
var layout = {
  title: "Hours of TV Watched by Students",
  xaxis: { title: "Name" },
  yaxis: { title: "Hours Watched"}
};

// Plot the chart to a div tag with id "bar-plot"
Plotly.newPlot("bar-plot", data, layout);
