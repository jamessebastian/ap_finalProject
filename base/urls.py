from django.urls import path
from .views import RoomList,RoomDetail,CustomLoginView,RegisterPage,BookingList,DeleteView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('register', RegisterPage.as_view(), name='register'),
    path('asd', RoomList.as_view(), name='rooms'),
    path('your_bookings', BookingList.as_view(), name='your_bookings'),
    path('your_bookings-delete/<int:pk>', DeleteView.as_view(), name='your_bookings-delete'),
    path('asd/<int:pk>', RoomDetail.as_view(), name='room'),
]   