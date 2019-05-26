<?php
$user = $_GET["user"] ?? "unknown user";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>inner/outerHTML</title>
        <script src="./script.js"></script>
    </head>
    <body>
        <p>Hello, <?php echo $user; ?>!</p>
        <p id="p-tag"></p>
        <div id="div-tag"></div>
    </body>
</html>