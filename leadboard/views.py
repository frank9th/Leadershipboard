from django.shortcuts import render

# Create your views here.
def home(request):
    context = {"something": something.objects.all()}
    return render(request, "home.html", context)

def about(request):
    context = {"something": something.objects.all()}
    return render(request, "about.html", context)
