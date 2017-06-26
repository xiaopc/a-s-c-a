<?php
define("SOCKET",1);
require_once("gettime.php");

$filters = array
 (
 "id"   => FILTER_SANITIZE_NUMBER_INT,
 "pass" => FILTER_SANITIZE_NUMBER_INT,
 "kch1"=> FILTER_SANITIZE_NUMBER_INT,
 "kxh1"=> FILTER_SANITIZE_NUMBER_INT,
 "note1"=> FILTER_SANITIZE_SPECIAL_CHARS,
 "kch2"=> FILTER_SANITIZE_NUMBER_INT,
 "kxh2"=> FILTER_SANITIZE_NUMBER_INT,
 "note2"=> FILTER_SANITIZE_SPECIAL_CHARS,
 "kch3"=> FILTER_SANITIZE_NUMBER_INT,
 "kxh3"=> FILTER_SANITIZE_NUMBER_INT,
 "note3"=> FILTER_SANITIZE_SPECIAL_CHARS,
 );
$result = filter_input_array(INPUT_POST, $filters);
$getresult = filter_input_array(INPUT_GET, $filters);

if ($_GET["action"]=="add"){
    if ($_GET["code"]===$validation){
        define("TESTED",1);
        require_once("addconf.php");
    } else {
        die('{"status":"401"}');
    }
} else if ($_GET["action"]=="view"){
    require_once("viewlog.php");
}

?>