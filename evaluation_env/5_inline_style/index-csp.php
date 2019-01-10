<?php
$user = $_GET["user"] ?? "unknown user";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>external style</title>
        <meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' 'strict-dynamic'; style-src 'self' 'sha256-caL/t84GBpmtv6vzuELR38kq9LWs/L5BujNjEy1csGk='; connect-src 'self'; base-uri 'none'">
        <style>
        #target {
            color: blue;
        }
        </style>
    </head>
    <body>
        <p>Hello, <?php echo $user; ?>!</p>

        <p style="color: red;">This text is styled by style attribute</p>
        <p id="target">This text is styled by inline css</p>
    </body>
</html>