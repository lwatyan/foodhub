from django.http import HttpResponse
from django.shortcuts import render
from .models import Restaurant

# Create your views here.


def restaurant_list(request):

	objects =Restaurant.objects.all()

	context = {

	"objects" : objects
	}

	return render(request, "restaurant_list.html", context)


def restaurant_detail(request,restaurant_id):

	detail = Restaurant.objects.get(id= restaurant_id)

	context = {
	"the_detail" : detail
	}

	return render(request, "restaurant_detail.html", context)