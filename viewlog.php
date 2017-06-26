<?php require_once("./template/header.html"); ?>

<textarea>
<?php
$filename = "./logs/".$getresult[id].".txt";
if (!file_exists($filename)){ die('{"status":"404"}'); }
require_once($filename);
?>
</textarea>

<?php require_once("./template/footer.html"); ?>