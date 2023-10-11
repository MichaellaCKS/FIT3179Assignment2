var specVis1 = "cloropeth.vg.json";
var specVis2 = "line.vg.json";

vegaEmbed('#choropeth', specVis1, {
    "actions": false
});

vegaEmbed('#line', specVis2, {
    "actions": false
}).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);