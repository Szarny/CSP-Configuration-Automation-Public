<?php
$user = $_GET["user"] ?? "unknown user";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>eval</title>
        <meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' http://localhost:8080 'sha256-1MV04PDgio8yygougSv5TFU7PFxDu8VCQImXHyG74Fo=' 'strict-dynamic'; style-src 'self'; connect-src 'self'; base-uri 'none'">
        <script integrity="sha256-1MV04PDgio8yygougSv5TFU7PFxDu8VCQImXHyG74Fo=" src="./script.js"></script>
    </head>
    <body>
        <p>Hello, <?php echo $user; ?>!</p>
    </body>
</html>