<?php
header('Content-Type: text/html');
{
  $denied = $_POST['Denied'];
  $una = $_POST['Una'];
  $time = $_POST['Time'];
  $unk = $_POST['Unk'];
  $support = 'GPS dan foydalanishni iloji yo`q!';

  if (isset($denied))
  {
    $f = fopen('result.txt', 'w+');
    fwrite($f, $denied);
    fclose($f);
  }
  elseif (isset($una))
  {
    $f = fopen('result.txt', 'w+');
    fwrite($f, $una);
    fclose($f);
  }
  elseif (isset($time))
  {
    $f = fopen('result.txt', 'w+');
    fwrite($f, $time);
    fclose($f);
  }
  elseif (isset($unk))
  {
    $f = fopen('result.txt', 'w+');
    fwrite($f, $unk);
    fclose($f);
  }
  else
  {
    $f = fopen('result.txt', 'w+');
    fwrite($f, $support);
    fclose($f);
  }
}
?>
