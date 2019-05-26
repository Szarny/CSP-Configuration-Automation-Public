var xhr_react = new XMLHttpRequest();
var url_react = "https://unpkg.com/react@16/umd/react.production.min.js";

xhr_react.onload = function() {
    if (xhr_react.readyState === 4) {
        if (xhr_react.status === 200) {
            console.log("[xhr_react result]", xhr_react.responseText);
        } else {
            console.error("[xhr_react result]\nfailed");
        }
    }
};

xhr_react.open("GET", url_react, true);
xhr_react.send(null);