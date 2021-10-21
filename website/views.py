import os
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Travel_Destination,Review,Blog,Gallery
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.core.files import File
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


def index(request):

    #for travel destination
    travel_destination = Travel_Destination.objects.all()
    trending_trips = travel_destination.filter(trip_choice  = 'Trending Trips')[::-1]
    weekend_trips = travel_destination.filter(trip_choice  = 'Weekend Trips')[::-1][:3]
    backpacking_trips = travel_destination.filter(trip_choice  = 'Backpacking Trips')[::-1][:3]
    treks = travel_destination.filter(trip_choice = 'Treks')[::-1][:3]

    #for reviews
    reviews = Review.objects.all()[::-1]
    
    return render(request,'website/index.html',{'trending_trips': trending_trips,'weekend_trips':weekend_trips,'backpacking_trips':backpacking_trips,'treks':treks,'reviews': reviews})

def tours(request):
    alltours = None
    category = None
    
    if request.GET.get('category'):
        category = request.GET.get('category')
        alltours = Travel_Destination.objects.filter(trip_choice=category)[::-1]
        

    elif request.GET.get('tour_length'):
        tour_length_min, tour_length_max = request.GET.get('tour_length').split(',')
        alltours = Travel_Destination.objects.filter(trip_days__range=[int(tour_length_min), int(tour_length_max)])[::-1]

    elif request.GET.get('value'):
        values = request.GET.get('value')
        min, max = values.split(",")
        alltours = Travel_Destination.objects.filter(trip_price__range=[min, max])[::-1]

    else:
        alltours = Travel_Destination.objects.all()[::-1]
        
    p = Paginator(alltours[::-1],12)
    page_number = request.GET.get('page')

    try:
        page_obj = p.get_page(page_number) 
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    return render(request,'website/tours.html',{'alltours' : alltours, 'category' : category, 'length' : request.GET.get('tour_length'),'page_obj':page_obj})


def about(request):
    return render(request,'website/about.html')

def blogs(request):

    blogs = Blog.objects.all()
    blogs = blogs.order_by('blog_date')[::-1]

    return render(request,'website/blog.html',{'blogs':blogs})

def blogdetails(request,title):
    
    blogdetails = Blog.objects.filter(blog_title = title)
    popular_blog = Blog.objects.all()
    popular_blog = popular_blog.order_by('blog_date')
    
    return render(request,'website/blog-details.html',{'title':title,'blogdetails':blogdetails,'popular_blog':popular_blog[::-1][:5]})

def search(request):
    
    query=request.GET['query']

    if query == '':
        messages.success(request, 'Enter a Search Query!')
        return redirect('blogs')

    else :
        allblogs = Blog.objects.filter(blog_title__icontains=query)[::-1]

    return render(request,'website/search.html',{'allblogs':allblogs,'query': query })

def searchdest(request):

    querydest=request.GET['querydest']

    if querydest == '':
        messages.success(request, 'Enter a Search Query!')
        return redirect('index')

    else:
        alldest = Travel_Destination.objects.filter(Q(trip_title__icontains=querydest) | Q(trip_choice__icontains=querydest))[::-1]

    return render(request,'website/searchdest.html',{'alldest':alldest,'querydest':querydest})

def gallery(request):
    gallery_images = Gallery.objects.all()[::-1]

    # paginating remaining articles after selecting TOP-3 arctile
    p = Paginator(gallery_images[::-1],15)
    page_number = request.GET.get('page')

    try:
        page_obj = p.get_page(page_number) 
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    return render(request,'website/gallery.html',{'gallery_images':gallery_images,'page_obj':page_obj})


def booking(request,dst_title):
    if request.method == 'POST':
        fname = request.POST['firstname'].capitalize()
        lname = request.POST['lastname'].capitalize()
        gender = request.POST['usergender']
        email = request.POST['email']
        number = request.POST['number']
        country = request.POST['country'].capitalize()
        travellers = request.POST['traveller']
        address = request.POST['address']

        booking_parameters = {'fname':fname ,'lname' :lname,'email':email,'gender':gender,'travellers':travellers,'number':number, 'country':country,'address':address,'dst_title':dst_title}

        msg_html = render_to_string('website/confirmation.html',booking_parameters)

        email = EmailMultiAlternatives(f'Booking Hold Mail', '', settings.EMAIL_HOST_USER, [email])
        email.attach_alternative(msg_html, "text/html")
        email.send()

        msg_html = render_to_string('website/bookingadmin.html',booking_parameters)

        email = EmailMultiAlternatives(f'Booking  Mail for {dst_title} from {fname} {lname}', '', settings.EMAIL_HOST_USER, ['twistandtoursbooking@gmail.com'])
        email.attach_alternative(msg_html, "text/html")
        email.send()

        
    return render(request,'website/booking.html')

def tourbook(request,trip_title):

    tourdetails = Travel_Destination.objects.filter(trip_title = trip_title)

    return render(request,'website/booking.html',{'tourdetails':tourdetails,'title':trip_title})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name'].capitalize()
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']

        contact_parameters = {'name': name , 'email':email, 'number':number, 'message':message}

        msg_html = render_to_string('website/email.html',contact_parameters)

        email = EmailMultiAlternatives(f'Query from {name}', '', settings.EMAIL_HOST_USER, ['twistandtoursbooking@gmail.com'])
        email.attach_alternative(msg_html, "text/html")
        email.send()
        
    return render(request,'website/contact.html')

def faqs(request):
    return render(request,'website/faqs.html')

def privacypolicy(request):
    return render(request,'website/privacy-policy.html')

def cancelpolicy(request):
    return render(request,'website/cancelpolicy.html')

def termscondition(request):
    return render(request,'website/termscondition.html')

