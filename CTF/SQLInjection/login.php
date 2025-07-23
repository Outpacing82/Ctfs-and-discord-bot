<?php
$db = new SQLite3('users.db');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
    $result = $db->query($query);

    if ($row = $result->fetchArray()) {
        echo "Welcome, " . htmlspecialchars($row['username']) . "!<br>";
        if ($row['is_admin']) {
            echo "Here is the flag: " . $row['flag'];
        }
    } else {
        echo "Invalid credentials, please try again.";
    }
}
?>
