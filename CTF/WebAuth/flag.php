<?php
session_start();

if (!isset($_SESSION['identity'])) {
  echo "You must be logged in.";
  exit;
}

if ($_SESSION['identity'] !== 'admin') {
  echo "Access restricted to admin only.";
  exit;
}

echo "<h2>Admin Portal</h2>";
echo "<p>Your flag is: flag{SUCCESS!}</p>";
?>

