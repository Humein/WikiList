from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib import admin

app_name = 'wikiPage'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    path('<path:title_url>/', views.detail, name='detail'),
]