from django.http import HttpResponse


# Function View
def welcome(request):
    return HttpResponse("<h1>Welcome To Django</h1>")
