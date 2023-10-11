var specVis1 = "https://raw.githubusercontent.com/MichaellaCKS/FIT3179Assignment2/main/js/cloropeth.vg.json";
var specVis2 = "https://raw.githubusercontent.com/MichaellaCKS/FIT3179Assignment2/main/js/line.vg.json";

vegaEmbed('#choropeth', specVis1, {
    "actions": false
});

vegaEmbed('#line', specVis2, {
    "actions": false
}).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);