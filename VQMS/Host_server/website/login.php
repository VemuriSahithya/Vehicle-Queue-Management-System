
<?php
session_start();
include("database.php");
extract($_POST);

if(isset($submit))
{
	if(isset($_POST['radio'])){
		if($_POST['radio']=='user'){
			$rs=mysqli_query($conn,"select * from users where email='$email' and password='$passwd';");
			if(mysqli_num_rows($rs)<1)
			{
				$found="N";
			}
			else
			{
				$_SESSION['email'] = $email;
				header("location:index.php");
				exit();
			}
		}
		if($_POST['radio']=='security'){
			$rs = mysqli_query($conn,"select * from security where email='$email' and password='$passwd';");
			$_SESSION['email'] = $email;
			header("location:security.php");
			exit();
		}
	}
}
?>
<!DOCTYPE html>
<html>
<head>
<title>Login</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<link href="login.css" rel="stylesheet" type="text/css">
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

</head>
<body>
	<div class="container-fluid frontLogin">
		<div class="container justify-content-sm-center">
			<form class="loginform" method="post">
				<div class="form-group row">
					<label for="email" class="form-label form-label-lg col-sm-3 label"> Email : </label>
					<div class="col-sm-9">
						<input type="text" name="email" placeholder="Enter Your E-mail ID" class="form-control" id="email" required>
					</div>
				</div>
				<div class="form-group row">
					<label for="passwd" class="form-label form-label-lg col-sm-3 label"> Password : </label>
					<div class="col-sm-9">
						<input type="password" name="passwd" placeholder="Enter Your Password" class="form-control" id="passwd" required>
					</div>
				</div>
				<div class="form-group">
          <input type="submit" name="submit" value="Login" class="btn btn-lg btn-block btn-primary">
        </div>
				<fieldset>
					<div class="form-check form-check-inline">
	  				<input class="form-check-input" type="radio" id="user" name="radio" value="user">
	  				<label class="form-check-label" for="user">User</label>
					</div>
					<div class="form-check form-check-inline">
	  				<input class="form-check-input" type="radio" id="security" name="radio" value="security">
	  				<label class="form-check-label" for="security">Security</label>
					</div>
				</fieldset>
				<p>Not Registered? <a href="signup.php">Signup Here</a></p>
				<?php
						  if(isset($found))
						  {
						  	echo '<p class="w3-center w3-text-red">Invalid user id or password<br><a href="login.php">Please try again</p>';
						  }
				?>
			</form>

		</div>
	</div>


</body>
</html>
