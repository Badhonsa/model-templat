import os

from django.shortcuts import render,redirect
from django.http import HttpResponse
from AA.models import Human


def Talk(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        image = request.FILES.get('image')
        address = request.POST.get('address')

        try:
            if image:
                human = Human.objects.create(name=name, email=email, age=age, gender=gender, image=image,
                                             address=address)
            else:
                human = Human.objects.create(name=name, email=email, age=age, gender=gender, address=address)
            print('Data saved successfully')
        except Exception as e:
            print(f'Error saving data: {e}')

    return render(request, "index.html")


def all_profiles(request):
    humans = Human.objects.all()
    return render(request, "allprofile.html", {'humans': humans})


def all_prof(request):
    human = Human.objects.all()
    return render(request, "allprofile.html", locals())


def profile(request):
    # Add logic to retrieve user profile data if needed
    return render(request, 'profile.html')

def delete_prof(request, id):
    prof = Human.objects.get(id=id)
    if prof.image != 'def.jpg':
        os.remove(prof.image.path)
    prof.delete()
    return redirect('all_prof')

def update(request, id):
    prof = Human.objects.get(id=id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        image = request.FILES.get('image')
        address = request.POST.get('address')

        if image:
            prof.name = name
            prof.email = email
            prof.age = age
            prof.gender = gender
            if prof.image != 'def.jpg':
                os.remove(prof.image.path)
            prof.image = image
            prof.address = address
            prof.save()
            return redirect('all_prof')

        else:
            prof.name = name
            prof.email = email
            prof.age = age
            prof.gender = gender
            prof.address = address
            prof.save()
            return redirect('all_prof')
    return render(request, "update.html", locals())