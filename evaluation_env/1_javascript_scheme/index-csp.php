<?php
$user = $_GET["user"] ?? "unknown user";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>javascript scheme</title>
        <meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' 'strict-dynamic'; style-src 'self'; connect-src 'self'; base-uri 'none'">
    </head>
    <body>
        <p>Hello, <?php echo $user; ?>!</p>
        <a href="javascript: console.log('[javascript scheme]')">javascript scheme</a>
    </body>
</html>