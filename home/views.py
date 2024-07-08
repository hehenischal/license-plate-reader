from django.shortcuts import render

from .models import NumberPlate

# Create your views here.

def home(req):

    if req.method == "POST":
        image = req.FILES.get('image')
        print(image)
        number_plate = NumberPlate.objects.create(number_plate=image)
        context = {
            'number_plate': number_plate
        }
        return render(req, 'home.html',context)
    
    return render(req, 'home.html')
