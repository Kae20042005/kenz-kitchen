from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        "appName" : "Ken'z Kitchen",
        "nama": "Farrel Ahmad Ilyasa",
        "kelas": "PBP E"
    }

    return render(request, "main.html", context)