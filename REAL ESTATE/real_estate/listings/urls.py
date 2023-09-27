from django.urls import path
from . import views

urlpatterns = [
    path("", views.listing_list, name="listing-list"),
    path("listings/<pk>", views.listing_retrieve, name="listing-retrieve"),
    path("listings/<pk>/edit/", views.listing_update, name="listing-update"),
    path("listings/<pk>/delete/", views.listing_delete, name="listing-delete"),
    path("add-listing", views.listing_create, name="listing-create"),
]
