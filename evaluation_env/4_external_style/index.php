<?php
$user = $_GET["user"] ?? "unknown user";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>external style</title>
        <link rel="stylesheet" href="./style.css"></link>
    </head>
    <body>
        <p>Hello, <?php echo $user; ?>!</p>
        <p id="target">This text is styled by external css</p>
    </body>
</html>