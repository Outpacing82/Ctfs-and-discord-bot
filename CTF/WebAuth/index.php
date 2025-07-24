<?php
session_start();
?>

<!DOCTYPE html>
<html>
<head>
  <title>SecureCorp Login</title>
</head>
<body>
  <h1>Login to SecureCorp</h1>
  <form method="POST" action="login.php">
    <input type="text" name="uid" placeholder="Username" required><br><br>
    <input type="password" name="pwd" placeholder="Password" required><br><br>
    <input type="submit" value="Login">
  </form>
</html>
