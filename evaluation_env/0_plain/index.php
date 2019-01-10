<?php
$user = $_GET["user"] ?? "unknown user";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>plane</title>
    </head>
    <body>
        <p>Hello, <?php echo $user; ?>!</p>
    </body>
</html>