<!DOCTYPE HTML>
<html>
<head>
<title>Driver Signup</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>

<body>
<?php

extract($_POST);
include("database.php");
	date_default_timezone_set("Asia/Calcutta");
	$driver_name = $_POST['name'];
	$phone_number = $_POST['phone_number'];
	$license_id = $_POST['license_id'];
	$car_number = $_POST['cab_number'];
	$room_number = $_POST['room_number'];
	$status = "inside";
	$d= strtotime("now");
	$date=date("Y-m-d h:i:sa", $d);
	$hostel = $_POST['hostel'];

	$query="insert into request(driver_name,phone_number,license_id,car_number,status,date,hostel,room_number) values('$driver_name','$phone_number','$license_id','$car_number','$status','$date','$hostel','$room_number')";
	$rs=mysqli_query($conn,$query)or die("Could Not Perform the Query");
	shell_exec("python C:\Users\Rakesh\Desktop\python_practise\publish1.py 2>&1");
	header('location:security.php');
	exit();
?>
</body>
</html>