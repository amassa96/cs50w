from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/search/', views.search, name='search'),
    path('wiki/create-new-page/', views.create, name='create'),
    path('wiki/random-page/', views.random_page, name='random-page'),
    path('wiki/<str:title>/', views.entry, name='entry'),
    path('wiki/<str:title>/edit-entry/', views.edit, name='edit')
]
