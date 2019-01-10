<?php
$user = $_GET["user"] ?? "unknown user";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>inline script with url</title>
        <script src="./xhr_jquery.js"></script>
        <script src="./xhr_react.js"></script>
    </head>
    <body>
        <p>Hello, <?php echo $user; ?>!</p>
        <script>

        </script>
    </body>
</html>