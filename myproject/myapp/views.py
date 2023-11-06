from django.shortcuts import render
from .models import Person 

# Import your model

def person_list(request):
    # Query the model to get all records
    people = Person.objects.all()
    
    # Define the template context with the 'people' queryset
    context = {
        'people': people
    }
    
    return render(request, 'view_data.html', context)


def new_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        person = Person.objects.create(name=name, age=age, phone_number=phone_number, address=address)
        person.save()
        return render(request, 'new_register.html', {'person': person})
    else:
        return render(request, 'new_register.html')


