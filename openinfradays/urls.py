"""openinfradays URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views, sns_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('session/<int:session_id>', views.session_detail),
    path('program/sessions', views.session_list),
    path('about', views.about),
    path('sponsors', views.sponsors),
    path('virtualbooth', views.virtualbooth),
    path('virtualbooth/<int:virtualbooth_id>', views.virtualbooth_detail),
    path('schedule', views.schedules),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
