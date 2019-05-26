<?php
$user = $_GET["user"] ?? "unknown user";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>external style</title>
        <style>
        #target {
            color: blue;
        }
        </style>
    </head>
    <body>
        <p>Hello, <?php echo $user; ?>!</p>

        <p style="color: red;">This text is styled by style attribute</p>
        <p id="target">This text is styled by inline css</p>
    </body>
</html>