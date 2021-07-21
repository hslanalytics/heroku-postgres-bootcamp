
// Create the data array for the plot
var data = "/api/tv";

// Define the plot layout
var layout = {
  title: "Hours of TV Watched by Students",
  xaxis: { title: "Name" },
  yaxis: { title: "Hours Watched"}
};

// Plot the chart to a div tag with id "bar-plot"
Plotly.newPlot("bar-plot", data, layout);
