<?php
$user = $_GET["user"] ?? "unknown user";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>javascript scheme</title>
    </head>
    <body>
        <p>Hello, <?php echo $user; ?>!</p>
        <a href="javascript: console.log('[javascript scheme]')">javascript scheme</a>
    </body>
</html>