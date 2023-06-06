from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>', views.post, name='post'),
    path('createpost', views.createpost, name='createpost'),
    path('post/<int:pk>/editpost', views.editpost, name='editpost'),
]
