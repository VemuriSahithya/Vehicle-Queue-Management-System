<?php
function get_image(){
    echo  nl2br("Waiting for Image...");
    $output = shell_exec("python C:\Users\Rakesh\Desktop\python_practise\sub.py 2>&1");   
    echo  nl2br($output);
    echo  nl2br("\n");
}

function get_car_number(){
    echo  nl2br("Executing Machine learning code:\n");
    $output = shell_exec("python C:\Users\Rakesh\Desktop\python_practise\p1.py 2>&1");
    echo nl2br("Detected Number:");
    echo nl2br($output);
}

function pub1(){
    echo nl2br("Open \n");
    shell_exec("python C:\Users\Rakesh\Desktop\python_practise\publish1.py 2>&1");
}
function pub0(){
    echo nl2br("Dont open\n");
    shell_exec("python C:\Users\Rakesh\Desktop\python_practise\publish0.py 2>&1");  
}


function check_database(){
    echo nl2br("Checking Data Base\n");
    return 1;
}

function send_result(){
    $res=check_database();
    if($res==1){
        pub1();
    }
    else{
        pub0();
    }
}
function test_input($data){
	$date= trim($data);
	$data=stripcslashes($data);
	$data= htmlentities($data);
	return $data;
}

function start(){
    
    while(1){
        echo nl2br("Process start\n");
        get_image();
        get_car_number();
        send_result();
        sleep(5);
        echo nl2br("Process End");
    }
}
echo nl2br("------------Started VQMS -------------\n\n");
start();
    
?>