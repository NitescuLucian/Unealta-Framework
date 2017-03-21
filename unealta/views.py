from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now()
    html = """
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="http://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.6.1/css/font-awesome.min.css" rel="stylesheet" type="text/css">
  <link href="http://v4.pingendo.com/assets/bootstrap/themes/default.css" rel="stylesheet" type="text/css">
</head>

<body>
  <div class="section">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <h1 class="display-1">Unealta</h1></div>
      </div>
    </div>
  </div>
  <div class="section">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <h1 class="">This is a Kali linux python based automatization for web pentesting.</h1></div>
      </div>
    </div>
  </div>
  <script type="text/javascript" src="http://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
  <script type="text/javascript" src="https://cdn.rawgit.com/twbs/bootstrap/v4-dev/dist/js/bootstrap.js"></script>
  <div class="section">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <form class="">
            <div class="form-group">
              <label>Enter target</label>
              <input type="URL" class="form-control" placeholder="HTTP(S)://">
            </div>

            <button type="Perform Attack" class="btn btn-primary">Submit</button>
          </form>
        </div>
      </div>
    </div>
  </div>


</body>

</html>
"""
    return HttpResponse(html)
