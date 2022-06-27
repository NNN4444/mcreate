<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>ブラボっぽいな何か</h1>
    <?php
    $output=null;
    $command=null;
    $command="python3 mojya.py ";
    exec($command,$output);
    print "$output[0]\n";
    ?>
</body>
</html>
