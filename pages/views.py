from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>DevOps Course — Git Demo</h1>")


