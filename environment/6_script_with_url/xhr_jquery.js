var xhr_jquery = new XMLHttpRequest();
var url_jquery = "https://code.jquery.com/jquery-1.12.4.min.js";

xhr_jquery.onload = function() {
    if (xhr_jquery.readyState === 4) {
        if (xhr_jquery.status === 200) {
            console.log("[xhr_jquery result]", xhr_jquery.responseText);
        } else {
            console.error("[xhr_jquery result]\nfailed");
        }
    }
};

xhr_jquery.open("GET", url_jquery, true);
xhr_jquery.send(null);