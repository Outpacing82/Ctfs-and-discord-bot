<?php

$greeting = "";
$flag = "";

if (isset($_GET["name"])) {
  $greeting = $_GET["name"];

  if (strpos($greeting, "<script>") !== false && strpos($greeting, "alert(") !== false) {
    $flag = "CTF{reflected_xss_is_easy}";
  }
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Hello!</title>
</head>
<body>
  <h1>Hello <?php echo $greeting; ?>!</h1>

  <?php if (!empty($flag)) echo "<p><strong>Flag:</strong> $flag</p>"; ?>
  
  <form method="GET">
    <input type="text" name="name" placeholder="Enter your name">
    <button type="submit">Say Hello</button>
  </form>
</body>
</html>
