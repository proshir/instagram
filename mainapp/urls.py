from django.urls import path
from .views import upload_photo, view_all_photos, like_photo

urlpatterns = [
    path('', view_all_photos, name='view_all_photos'),
    path('upload/', upload_photo, name='upload_photo'),
    path('photos/<int:photo_id>/like/', like_photo, name='like_photo'),
]
