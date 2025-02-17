"""
URL configuration for cloudintegration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin

import authentication.views
import publication.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',authentication.views.welcome_page, name='welcome'),
    path('login',authentication.views.login_page, name='login'),
    path('logout/',authentication.views.logout_user, name='logout'),
    path('register/',authentication.views.registration_page, name='register'),
    path('home/', publication.views.home_page, name='home'),
    path('like/<int:publication_id>/', publication.views.like_publication, name='like'),
    path('dislike/<int:publication_id>/', publication.views.dislike_publication, name='dislike'),
    # path('write_letter/', love.views.write_letter, name='write_letter'),
    # path('edit_letter/<int:letter_id>/', love.views.edit_letter, name='edit_letter'),

]
