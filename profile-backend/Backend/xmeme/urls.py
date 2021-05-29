
from django.urls import path

from . import views

app_name = 'xmeme'
urlpatterns = [
    path('', views.show_list, name='show_memes'),
    path('<int:id>/', views.show_id, name='show_id'),
]