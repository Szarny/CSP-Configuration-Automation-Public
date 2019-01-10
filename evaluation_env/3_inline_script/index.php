<?php
$user = $_GET["user"] ?? "unknown user";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>inline script</title>
    </head>
    <body>
        <p>Hello, <?php echo $user; ?>!</p>
        <script>console.log("[inline script]");</script>
    </body>
</html>