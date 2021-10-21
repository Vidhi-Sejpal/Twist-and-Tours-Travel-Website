from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('tours',views.tours,name='tours'),
    path('about',views.about, name ='about'),
    path('blogs',views.blogs,name = 'blogs'),
    path('blogdetails/<str:title>',views.blogdetails,name = 'blogdetails'),
    path('search',views.search,name = 'search'),
    path('searchdest',views.searchdest, name ='searchdest'),
    path('contact',views.contact, name ='contact'),
    path('booking/<str:dst_title>',views.booking,name='booking'),
    path('tourbook/<str:trip_title>',views.tourbook,name='tourbook'),
    path('gallery',views.gallery,name='gallery'),
    path('faqs',views.faqs,name='faqs'),
    path('privacypolicy',views.privacypolicy,name='privacypolicy'),
    path('cancelpolicy',views.cancelpolicy,name='cancelpolicy'),
    path('termscondition',views.termscondition,name = 'termscondition'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
