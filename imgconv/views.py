from django.shortcuts import render
from django.core.files.storage import default_storage
from django.http import HttpResponse
from PIL import Image
import os

def index(request):
    image_url = None
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        path = default_storage.save('uploaded/uploaded_image.jpg', image_file)
        full_path = default_storage.path(path)

        # Convert image to grayscale
        img = Image.open(full_path).convert('L')
        gray_path = 'uploaded/grayscale_image.jpg'
        gray_full_path = default_storage.path(gray_path)
        img.save(gray_full_path)

        image_url = default_storage.url(gray_path)  # To display in template

    return render(request, 'index.html', {'image_url': image_url})
