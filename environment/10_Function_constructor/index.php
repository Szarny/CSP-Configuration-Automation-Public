<?php
$user = $_GET["user"] ?? "unknown user";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>Function constructor</title>
        <script src="./script.js"></script>
    </head>
    <body>
        <p>Hello, <?php echo $user; ?>!</p>
    </body>
</html>