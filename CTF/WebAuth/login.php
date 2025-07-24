<?php
session_start();

$users = [
  'user' => 'userpass',
  'guest' => 'guest123',
  // 'admin' => 'adminpass' — not stored or checked!
];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $username = $_POST['uid'];
  $password = $_POST['pwd'];

  // Intended logic flaw: if user is admin, skip password check
  if ($username === 'admin') {
    $_SESSION['identity'] = 'admin';
  } elseif (isset($users[$username]) && $users[$username] === $password) {
    $_SESSION['identity'] = $username;
  }

  header("Location: index.php");
  exit;
}
?>
