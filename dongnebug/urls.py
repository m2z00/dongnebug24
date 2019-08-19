"""dongnebug24 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *
app_name = 'dongnebug'

urlpatterns = [
    path('complain/new/', ComplainCreateView.as_view(), name='complain_new'),
    path('complain/<int:pk>/', ComplainDetailView.as_view(), name='complain_detail'),
    path('content/<int:pk>/comment/', CommentCreateView.as_view(), name='create_comment'),
    path('homepage/', HomepageView.as_view(), name='homepage'),
    path('knockedbuk/', KnockedBukView.as_view(), name='knockedbuk'),
    path('newcomplain/', NewComplainView.as_view(), name='newcomplain'),
    path('search/', SearchView.as_view(), name='search'),
    path('uploadedcomplain/', UploadBukView.as_view(), name='uploadedbuk'),
    path('', LoginView.as_view(template_name='loegin.html'), name='login'),
    path('index/', IndexView.as_view(), name='index'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='update_profile')
    ]