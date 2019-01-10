<?php
$user = $_GET["user"] ?? "unknown user";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>document.write(ln)</title>
        <meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' http://localhost:8080 'sha256-1NYcwZPUGTVgwxOoV8wIyICVCMhB3F9b3H22XnvuEVw=' 'strict-dynamic'; style-src 'self'; connect-src 'self'; base-uri 'none'">
        <script integrity="sha256-1NYcwZPUGTVgwxOoV8wIyICVCMhB3F9b3H22XnvuEVw=" src="./script.js"></script>
    </head>
    <body>
        <p>Hello, <?php echo $user; ?>!</p>
    </body>
</html>