window.onload = function(){
    var ptag = document.getElementById("p-tag");
    var divtag = document.getElementById("div-tag");
    
    ptag.innerHTML = "<p>this text is injected by innerHTML</p>";
    divtag.outerHTML = "<p>this text is injected by outerHTML</p>";
}
