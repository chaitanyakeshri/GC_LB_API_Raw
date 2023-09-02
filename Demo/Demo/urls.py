

# main url file 
from django.contrib import admin
from django.urls import path
from django.conf.urls import include 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.about ),
    path('articles/', include('articles.urls')),
    path('api/', include('api.urls')),
    path('', views.homepage),
]

urlpatterns += staticfiles_urlpatterns()
