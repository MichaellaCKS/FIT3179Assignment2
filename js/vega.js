var specVis1 = "./js/cloropeth.vg.json";
var specVis2 = "./js/line.vg.json";
var specVis3 = "./js/bubble.vg.json";
var specVis4 = "./js/symbolmap.vg.json";
var specVis5 = "./js/treemap.vg.json";


vegaEmbed('#choropeth', specVis1, {
    "actions": false
});

vegaEmbed('#line', specVis2, {
    "actions": false
}).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

vegaEmbed('#bubble', specVis3, { "actions": false });

vegaEmbed('#symbol', specVis4, { "actions": false }).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

vegaEmbed('#treemap', specVis5, { "actions": false }).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);