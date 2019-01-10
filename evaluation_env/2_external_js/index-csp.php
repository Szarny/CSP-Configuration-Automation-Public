<?php
$user = $_GET["user"] ?? "unknown user";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>external js</title>
        <meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' http://localhost:8080 'sha256-gZmBnd4RznX/R53Rxj7t8Swp7HDysCKvy25yYD5QGfE=' 'strict-dynamic'; style-src 'self'; connect-src 'self'; base-uri 'none'">
        <script integrity="sha256-gZmBnd4RznX/R53Rxj7t8Swp7HDysCKvy25yYD5QGfE=" src="./script.js"></script>
    </head>
    <body>
        <p>Hello, <?php echo $user; ?>!</p>
    </body>
</html>