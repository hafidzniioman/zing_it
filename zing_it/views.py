from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1><center>Zing It</center></h1>")

def about(request):
    return HttpResponse("""<h1>About Us:</h1><p>With Zing, you can easily find the music of your choice and easily share it with other people. You can also browse through the collections of friends, artists, and celebrities, or create a playlist of your own.
      Soundtrack your life with Zing. Subscribe or listen for free.</p>""")