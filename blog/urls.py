from django.urls import path,include
from . import views
 
app_name = 'blog'

urlpatterns = [
    path('', views.my_blogs, name='my_blogs'),
    path('<int:blog_id>/', views.detail, name = 'detail'),
]