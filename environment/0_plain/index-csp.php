<?php
$user = $_GET["user"] ?? "unknown user";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>plane</title>
        <meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' 'strict-dynamic'; style-src 'self'; connect-src 'self'; base-uri 'none'">
    </head>
    <body>
        <p>Hello, <?php echo $user; ?>!</p>
    </body>
</html>