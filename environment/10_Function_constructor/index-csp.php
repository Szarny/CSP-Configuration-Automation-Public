<?php
$user = $_GET["user"] ?? "unknown user";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>Function constructor</title>
        <meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' http://localhost:8080 'sha256-Ea7I3R+VZagjvvJqYc6qtkSUKGKA0ntjQ1WFYY1g+aM=' 'strict-dynamic'; style-src 'self'; connect-src 'self'; base-uri 'none'">
        <script integrity="sha256-Ea7I3R+VZagjvvJqYc6qtkSUKGKA0ntjQ1WFYY1g+aM=" src="./script.js"></script>
    </head>
    <body>
        <p>Hello, <?php echo $user; ?>!</p>
    </body>
</html>