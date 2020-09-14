<!DOCTYPE html>
<?php
  session_start();
?>
<?php
  include('database.php');
  $email = $_SESSION['email'];
  $result = mysqli_query($conn,"select * from users where email = '$email'");
  $data = mysqli_fetch_array($result,MYSQLI_NUM);
?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Profile</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="signup.css" type="text/css">
    <script type="text/javascript">
    $(function() {
  $('a[data-toggle="tab"]').on('click', function(e) {
      window.localStorage.setItem('activeTab', $(e.target).attr('href'));
  });
  var activeTab = window.localStorage.getItem('activeTab');
  if (activeTab) {
      $('#nav-tab a[href="' + activeTab + '"]').tab('show');
      window.localStorage.removeItem("activeTab");
  }
});
    </script>
</head>
<body>
  <nav class="navbar navbar-expand-sm bg-dark" >
      <div class="navbar-collapse collapse" id="navbarCollapse">
        <nav class="navbar navbar-light bg-light">
          <span class="navbar-brand mb-0 h1">Vehicle Management System</span>
        </nav>
      <ul class="nav nav-pills nav-fill navbar-nav ml-auto" id="pills-tab" role="tablist">
        <li class="nav-item">
          <a class="nav-link" href="logout.php">Logout</a>
        </li>
      </ul>
      </div>
    </nav>
  <div class="container-fluid front">
    <div class="container justify-content-sm-center">
    <form name="form1" method="post" action="drivers.php" class="signupform">
        <div class="form-group row">
          <label for="name" class="col-xs-3 col-sm-3 col-form-label col-form-label-lg label">Driver Name : </label>
          <div class="col-xs-9 col-sm-9">
            <input type="text" id="name" name="name" class="form-control" placeholder="Enter Driver Name" required>
          </div>
        </div>
        <div class="form-group row">
          <label for="phone_number" class="col-xs-3 col-sm-3 col-form-label col-form-label-lg label">Phone Number : </label>
          <div class="col-xs-9 col-sm-9">
            <input type="text" id="phone_number" name="phone_number" class="form-control" placeholder="Phone Number" required>
          </div>
        </div>
        <div class="form-group row">
          <label for="license_id" class="col-xs-3 col-sm-3 col-form-label col-form-label-lg label">Driver License ID : </label>
          <div class="col-xs-9 col-sm-9">
            <input type="text" id="license_id" name="license_id" class="form-control" placeholder="Driver License ID" required>
          </div>
        </div>
        <div class="form-group row">
          <label for="cab_number" class="col-xs-3 col-sm-3 col-form-label col-form-label-lg label">Cab Number : </label>
          <div class="col-xs-9 col-sm-9">
            <input type="text" id="cab_number" name="cab_number" class="form-control" placeholder="Please the Cab number" required>
          </div>
        </div>
        <div class="form-group row">
          <label for="hostel" class="col-form-label col-form-label-lg col-xs-3 col-sm-3 label">Hostel : </label>
          <select class="col-xs-9 form-control form-control-lg col-sm-9" name="hostel" id="hostel">
            <option value="lohit">Lohit</option>
            <option value="kapili">Kapili</option>
            <option value="siang">Siang</option>
            <option value="barak">Barak</option>
            <option value="umiam">Umiam</option>
            <option value="brahmaputra">Brahmaputra</option>
            <option value="dihing">Dihing</option>
            <option value="dibang">Dibang</option>
            <option value="kameng">Kameng</option>
            <option value="manas">Manas</option>
            <option value="subhansiri">Subhansiri</option>
            <option value="dhansiri">Dhansiri</option>
          </select>
        </div>
        <div class="form-group row">
          <label for="room_number" class="col-xs-3 col-sm-3 col-form-label col-form-label-lg label">Room Number : </label>
          <div class="col-xs-9 col-sm-9">
            <input type="text" id="room_number" name="room_number" class="form-control" placeholder="Room Number" required>
          </div>
        </div>
        <div class="form-group row">
          <input type="submit" name="submit" value="Enter" class="btn btn-lg btn-block btn-primary">
        </div>
      </div>
    </form>
    </div>
  </div>
</body>
</html>
