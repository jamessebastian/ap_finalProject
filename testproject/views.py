from django.http import HttpResponse
from django.shortcuts import render

def test_page(request):
	return HttpResponse("<h1>test page-james sebastian</h1>")

def render_page(request):
	return render(request,'test.html')

def index_page(request):
	return render(request,'index.html')

def login_page(request):
	return render(request,'login.html')

def register_page(request):
	return render(request,'register.html')		

def admin_user_page(request):
	return render(request,'admin_user.html')
def admin_edit_user_page(request):
	return render(request,'admin_edit_user.html')
def admin_add_user_page(request):
	return render(request,'admin_add_user.html')

def admin_rooms_page(request):
	return render(request,'admin_rooms.html')
def admin_edit_rooms_page(request):
	return render(request,'admin_edit_rooms.html')
def admin_add_rooms_page(request):
	return render(request,'admin_add_rooms.html')

def admin_bookings_page(request):
	return render(request,'admin_bookings.html')
def admin_edit_bookings_page(request):
	return render(request,'admin_edit_bookings.html')
def admin_add_bookings_page(request):
	return render(request,'admin_add_bookings.html')

def admin_services_page(request):
	return render(request,'admin_services.html')
def admin_edit_services_page(request):
	return render(request,'admin_edit_services.html')
def admin_add_services_page(request):
	return render(request,'admin_add_services.html')

def rooms_page(request):
	return render(request,'rooms.html')

def book_room_page(request):
	return render(request,'book_room.html')
	
def your_bookings_page(request):
	return render(request,'your_bookings.html')