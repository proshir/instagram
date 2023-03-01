from django.shortcuts import render, redirect
from .models import Photo

def upload_photo(request):
    if request.method == 'POST':
        photo = Photo.objects.create(
            image=request.FILES['image'],
            caption=request.POST['caption']
        )
        return redirect('view_all_photos')
    return render(request, 'upload_photo.html')

def view_all_photos(request):
    photos = Photo.objects.all()
    return render(request, 'view_all_photos.html', {'photos': photos})

def like_photo(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    photo.likes += 1
    photo.save()
    return redirect('view_all_photos')
