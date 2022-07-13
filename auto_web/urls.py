from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.auth import views


urlpatterns = [
    path('', views.index, name='index'),
    path('lyrics/<str:pk>',views.lyrics_page,name='lyrics_page'),
    path('logout/', views.logoutPage, name='logoutPage'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.loginPage, name='loginPage'),
    path('adminpanel/', views.adminpanel, name='adminpanel'),
    # path('post/', views.post, name='post'),
]