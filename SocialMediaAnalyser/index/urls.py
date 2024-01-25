from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('link', views.option_link, name="link_option"),
    path('upload', views.option_upload, name="upload_option"),
    path('results', views.view_result, name="result"),
    path('uploadResults', views.view_result_upload, name='uploadResults'),
    path("view_upload_results", views.uploadResults, name="view_upload_results")
]
