<?php
$user = $_GET["user"] ?? "unknown user";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>external style</title>
        <meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' 'strict-dynamic'; style-src 'self' http://localhost:8080; connect-src 'self'; base-uri 'none'">
        <link rel="stylesheet" href="./style.css"></link>
    </head>
    <body>
        <p>Hello, <?php echo $user; ?>!</p>
        <p id="target">This text is styled by external css</p>
    </body>
</html>