import datetime as dt
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Image, Categories, Image_Location


# Create your views here.
def picture( request ):
    photos = Image.save_Image()
    return render(request, 'picture.html',{"photos":photos})

def photos_of_day(request):
    date = dt.date.today()
    photos = Image.todays_photos()
    return render(request, 'all-photos/today-photos.html',{'date': date,"photos":photos})

def past_days_photos(request,past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photos_today)
    
    photos = Image.days_photos(date)
    return render(request, 'all-photos/past-photos.html', {"date":date, 'photos':photos})

def search_results(request):

    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        print(search_term)
        searched_photos = Image.search_by_category(search_term)
        print(searched_photos)
        message = f'{search_term}'
      

        return render(request, 'all-photos/search.html', {
            'images': searched_photos,
            'message': message,
        })

    else:
        
        message = "You haven't searched for any category"
        return render(request, 'all-photos/search.html',{"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/image.html", {"image":image})

def filter_by_category(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        print(search_term)
        searched_photos = Image.search_by_category(search_term)
        message = f'{search_term}'
        params = {
            'searched_photos': searched_photos,
            'message': message,
        }

        return render(request, 'category.html', params)


def filter_by_locale(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        print(search_term)
        searched_photos = Image.filter_by_location(search_term)
        message = f'{search_term}'
        params = {
            'searched_photos': searched_photos,
            'message': message,
        }