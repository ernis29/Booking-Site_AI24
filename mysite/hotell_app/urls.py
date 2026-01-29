from .views import (UserProfileViewSet, CityListViewSet, CountryDetailViewSet, CityDetailViewSet,
                    ServicesViewSet, HotelListViewSet, HotelDetailViewSet, ImageHotelViewSet, RoomViewSet,
                    ImageRoomViewSet, ReviewViewSet, BookingViewSet, CountryListViewSet, RegisterView, CustomLoginView, LogoutView)
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()

router.register(r"user_profile", UserProfileViewSet, basename="user_profile")
router.register(r"service", ServicesViewSet, basename="service")
router.register(r"image-hotel", ImageHotelViewSet, basename="image-hotel")
router.register(r"room", RoomViewSet, basename="room")
router.register(r"image-room", ImageRoomViewSet, basename="image-room")
router.register(r"review", ReviewViewSet, basename="review")
router.register(r"booking", BookingViewSet, basename="booking")

urlpatterns = [
    path("", include(router.urls)),

    path('register/', RegisterView.as_view(), name='register_list'),
    path('login/', CustomLoginView.as_view(), name='login_list'),
    path('logout/', LogoutView.as_view(), name='logout_list'),

    path("city/", CityListViewSet.as_view(), name="city-list"),
    path("city/<int:pk>/", CityDetailViewSet.as_view(), name="city-detail"),

    path("country/", CountryListViewSet.as_view(), name="country-list"),
    path("country/<int:pk>/", CountryDetailViewSet.as_view(), name="country-detail"),

    path("hotel/", HotelListViewSet.as_view(), name="city-list"),
    path("hotel/<int:pk>/", HotelDetailViewSet.as_view(), name="city-detail"),
]
