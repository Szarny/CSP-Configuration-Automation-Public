<?php
$user = $_GET["user"] ?? "unknown user";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>ALL</title>
        <script src="./script.js"></script>
        <script src="./xhr_jquery.js"></script>
        <script src="./xhr_react.js"></script>
        <script src="./inner_outer_html.js"></script>
        <script src="./document_write_writeln.js"></script>
        <script src="./eval.js"></script>
        <script src="./Function.js"></script>
        <link rel="stylesheet" href="./style.css"></link>
        <style>#target-inline { color: blue; }</style>
    </head>
    <body>
        <p>Hello, <?php echo $user; ?>!</p>
        <a href="javascript: console.log('[javascript scheme]')">javascript scheme</a>

        <p id="p-tag"></p>
        <div id="div-tag"></div>

        <p style="color: red;">This text is styled by style attribute</p>
        <p id="target-inline">This text is styled by inline css</p>
        <p id="target-external">This text is styled by external css</p>

        <script>console.log("[inline script]");</script>
    </body>
</html>