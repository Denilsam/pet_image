from django.shortcuts import render,redirect

from .models import Petshop
def pet_list(request):
    pets = Petshop.objects.all() #fetch all pet records from the dashboard
    return render(request, 'pet_list.html', {'pets':pets}) 


def upload_pet(request):
    if request.method == 'POST':
        pet_name = request.POST.get('pet_name')
        pet_images = request.FILES.get('pet_images')
        Petshop.objects.create(pet_name=pet_name, pet_images=pet_images)
        return redirect('pet_list')
    return render(request, 'form.html')


#delete post

def delete_pet(request,pet_id):
    pet = Petshop.objects.filter(id=pet_id).first() #fetch the pet given ID
    if pet:
        pet.delete()
    return redirect('pet_list')


#edit_pet

def update_pet(request, pet_id):
    pet = Petshop.objects.filter(id=pet_id).first()
    if request.method == 'POST':
        pet_name = request.POST.get('pet_name')
        pet_image = request.FILES.get('pet_images')
        pet.pet_name = pet_name
        if pet_image:
            pet.pet_images = pet_image
        pet.save()
        return redirect('pet_list')
    return render(request, 'update_pet.html', {'pet': pet})

