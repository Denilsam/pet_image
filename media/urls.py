from django.urls import path
from . import views
urlpatterns = [
    path('', views.pet_list, name='pet_list'),
    path('upload/', views.upload_pet, name='upload_pet'),
    path('delete/<int:pet_id>/',views.delete_pet,name='delete_pet'),
    path('update/<int:pet_id>/',views.update_pet,name='update_pet'),
]