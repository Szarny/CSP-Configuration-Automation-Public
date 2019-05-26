<?php
$user = $_GET["user"] ?? "unknown user";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>ALL</title>
        <meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' http://localhost:8080 'sha256-gZmBnd4RznX/R53Rxj7t8Swp7HDysCKvy25yYD5QGfE=' 'sha256-b0wIol3V1kTL/TiBO5xkMC3MCsxQSGY/u6kUedKpvh4=' 'sha256-rr+HAv/rvjCyw6HOiKuNCRhCMB7YDTSkVk9fiq2+U2k=' 'sha256-llIEnPoqBHAkMW9ma2Fyh9gMKWEcYXva3SbAAxHpyYs=' 'sha256-1NYcwZPUGTVgwxOoV8wIyICVCMhB3F9b3H22XnvuEVw=' 'sha256-1MV04PDgio8yygougSv5TFU7PFxDu8VCQImXHyG74Fo=' 'sha256-J0lqB2JO0WBQyPz9aU9JR2mQidzgyYbA2hhrvHmSniE=' 'sha256-uxVHDkI2VVxiLrjNPK9Qlg7amPkHZVarv+HgmvH7IUI=' 'strict-dynamic'; style-src 'self' http://localhost:8080 'sha256-ElVvUDmzQMQ0Zpm2d4kqokClNu/iwMX7CtA5SFsBs3E='; connect-src 'self' https://code.jquery.com; base-uri 'none'">        <script integrity="sha256-gZmBnd4RznX/R53Rxj7t8Swp7HDysCKvy25yYD5QGfE=" src="./script.js"></script>
        <script integrity="sha256-gZmBnd4RznX/R53Rxj7t8Swp7HDysCKvy25yYD5QGfE=" src="./script.js"></script>
        <script integrity="sha256-b0wIol3V1kTL/TiBO5xkMC3MCsxQSGY/u6kUedKpvh4=" src="./xhr_jquery.js"></script>
        <script integrity="sha256-rr+HAv/rvjCyw6HOiKuNCRhCMB7YDTSkVk9fiq2+U2k=" src="./xhr_react.js"></script>
        <script integrity="sha256-llIEnPoqBHAkMW9ma2Fyh9gMKWEcYXva3SbAAxHpyYs=" src="./inner_outer_html.js"></script>
        <script integrity="sha256-1NYcwZPUGTVgwxOoV8wIyICVCMhB3F9b3H22XnvuEVw=" src="./document_write_writeln.js"></script>
        <script integrity="sha256-1MV04PDgio8yygougSv5TFU7PFxDu8VCQImXHyG74Fo=" src="./eval.js"></script>
        <script integrity="sha256-J0lqB2JO0WBQyPz9aU9JR2mQidzgyYbA2hhrvHmSniE=" src="./Function.js"></script>
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