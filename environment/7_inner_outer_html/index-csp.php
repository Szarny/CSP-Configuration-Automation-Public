<?php
$user = $_GET["user"] ?? "unknown user";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>inner/outerHTML</title>
        <meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' http://localhost:8080 'sha256-llIEnPoqBHAkMW9ma2Fyh9gMKWEcYXva3SbAAxHpyYs=' 'strict-dynamic'; style-src 'self'; connect-src 'self'; base-uri 'none'">
        <script integrity="sha256-llIEnPoqBHAkMW9ma2Fyh9gMKWEcYXva3SbAAxHpyYs=" src="./script.js"></script>
    </head>
    <body>
        <p>Hello, <?php echo $user; ?>!</p>
        <p id="p-tag"></p>
        <div id="div-tag"></div>
    </body>
</html>