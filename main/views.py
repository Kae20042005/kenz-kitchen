from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'menu' : 'Japanese Cheese Cake',
        'price': 'RpXX.XXX',
        'desc': 'Special cheese cake from Japan'
    }

    return render(request, "main.html", context)