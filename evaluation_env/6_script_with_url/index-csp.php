<?php
$user = $_GET["user"] ?? "unknown user";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>inline script with url</title>
        <meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' http://localhost:8080 'sha256-b0wIol3V1kTL/TiBO5xkMC3MCsxQSGY/u6kUedKpvh4=' 'sha256-rr+HAv/rvjCyw6HOiKuNCRhCMB7YDTSkVk9fiq2+U2k=' 'sha256-AbpHGcgLb+kRsJGnwFEktk7uzpZOCcBY74+YBdrKVGs=' 'strict-dynamic'; style-src 'self'; connect-src 'self' https://unpkg.com; base-uri 'none'">        
        <script integrity="sha256-b0wIol3V1kTL/TiBO5xkMC3MCsxQSGY/u6kUedKpvh4=" integrity="sha256-b0wIol3V1kTL/TiBO5xkMC3MCsxQSGY/u6kUedKpvh4=" src="./xhr_jquery.js"></script>
        <script integrity="sha256-rr+HAv/rvjCyw6HOiKuNCRhCMB7YDTSkVk9fiq2+U2k=" integrity="sha256-rr+HAv/rvjCyw6HOiKuNCRhCMB7YDTSkVk9fiq2+U2k=" src="./xhr_react.js"></script>    </head>
    <body>
        <p>Hello, <?php echo $user; ?>!</p>
    </body>
</html>