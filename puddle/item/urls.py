from django.urls import path
from . import views


app_name = "item"
urlpatterns = [
    path("", views.items, name="items"),
    path("new/", views.new, name="new"),
    path("<int:pk>/", views.detail, name="item-detail"),
    path("<int:pk>/delete/", views.delete, name="item-delete"),
    path("<int:pk>/edit/", views.edit, name="item-edit"),
]
