<?php
$user = $_GET["user"] ?? "unknown user";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>inline script</title>
        <meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' 'sha256-uxVHDkI2VVxiLrjNPK9Qlg7amPkHZVarv+HgmvH7IUI=' 'strict-dynamic'; style-src 'self'; connect-src 'self'; base-uri 'none'">
    </head>
    <body>
        <p>Hello, <?php echo $user; ?>!</p>
        <script>console.log("[inline script]");</script>
    </body>
</html>