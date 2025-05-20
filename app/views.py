from django.shortcuts import render

# Create your views here.
def django(req):
    return render(req,'app/index.html')