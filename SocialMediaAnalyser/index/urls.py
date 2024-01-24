from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('link/', views.option_link, name="link_option"),
    path('upload/', views.option_upload, name="upload_option")
    # Add more URL patterns here
]
