<?php
$text = htmlspecialchars($_POST['text'])
$fd = fopen("hello.txt", 'w') or die("не удалось создать файл");
fwrite($fd, $text);
fclose($fd);
