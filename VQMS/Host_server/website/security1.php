<!DOCTYPE html>
<?php
  session_start();
?>
<?php
  include('database.php');
  $email = $_SESSION['email'];
  extract($_POST);
?>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Vehicle Management System</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="login.css" type="text/css">
  </head>
  <body>
    <nav class="navbar navbar-expand-sm bg-dark" >
      <div class="navbar-collapse collapse" id="navbarCollapse">
          <nav class="navbar navbar-light bg-light">
          <span class="navbar-brand mb-0 h1">Vehicle Management System - Send</span>
        </nav>
          <ul class="nav nav-pills nav-fill navbar-nav ml-auto" id="pills-tab" role="tablist">
        <li class="nav-item">
          <a class="nav-link active" id="pills-detection-tab" data-toggle="pill" href="#pills-detection" role="tab" aria-controls="pills-detection" aria-selected="true">Send</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="security.php">Detection</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="logout.php">Logout</a>
        </li>
      </ul>
      </div>
    </nav>
    <div class="tab-content" id="pills-tabContent">
        <div class="tab-pane fade show active" id="pills-detection" role="tabpanel" aria-labelledby="pills-home-tab">
          <div class="container justify-content-sm-center">
      <form class="loginform" method="post">
        <div class="form-group">
          <input type="submit" name="detect" value="Detect" class="btn btn-lg btn-block btn-primary">
        </div>
      </form>
      <?php
        if(isset($detect)){
          /*Function ML*/
          shell_exec("python C:\Users\Rakesh\Desktop\python_practise\publish1.py 2>&1");
          $output = shell_exec("python C:\Users\Rakesh\Desktop\python_practise\sub.py 2>&1");
          $output = shell_exec("python C:\Users\Rakesh\Desktop\python_practise\p1.py 2>&1");
          echo $output;
          echo"<br>";
          echo '
          <form class="form-group loginform" method="post">
          <div class="form-group row">
          <img src="output.jpg">
        </div>
            <div class="form-group row">
          <label for="car_id" class="col-xs-3 col-sm-3 col-form-label col-form-label-lg label">Enter Car ID manually : </label>
          <div class="col-xs-9 col-sm-9">
            <input type="text" id="car_id" name="car_id" class="form-control" placeholder="Car Number" required value='.$output.'>
          </div>
          </div>
           <div class="form-group row">
          <input type="submit" name="submit" value="Detect" class="btn btn-lg btn-block btn-primary">
        </div>
        </form>
        ';
        }
      ?>
      <?php
        if(isset($_POST['submit'])){
          $car_id = $_POST['car_id'];
          $rs=mysqli_query($conn,"select * from request where car_number = '$car_id' and status!='completed';");

          $data = mysqli_fetch_array($rs,MYSQLI_NUM);
          if (mysqli_num_rows($rs)==0)
          {
            sleep(3);
            shell_exec("python C:\Users\Rakesh\Desktop\python_practise\publish0.py 2>&1");
            echo '
          <form class="form-group loginform" method="post">
           <div class="form-group row">
          <input type="submit" name="accept" value="Accept" class="btn btn-lg btn-block btn-primary">
        </div>
        </form>
        ';
          }
          else{
            sleep(3);
            shell_exec("python C:\Users\Rakesh\Desktop\python_practise\publish1.py 2>&1");
            $query="UPDATE request SET status = 'completed' WHERE car_number = '$car_id'";
            if($data[5]=='inside'){
              $rs=mysqli_query($conn,$query)or die("Could Not Perform the Query");
            }
            header('location:security1.php');
          }
        }
      ?>
      <?php
        if(isset($_POST['accept'])){
          sleep(3);
          shell_exec("python C:\Users\Rakesh\Desktop\python_practise\publish0.py 2>&1");
          header('location:security1.php');
        }
      ?>
    </div>
        </div>
      </div>
  </body>
</html>
