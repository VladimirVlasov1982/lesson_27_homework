from django.contrib import admin
from django.urls import path
from ads import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.main, name="main"),
    path("cat/", views.CategoriesView.as_view(), name="categories"),
    path("ad/", views.AdsView.as_view(), name="ads"),
    path("cat/<int:pk>/", views.CategoriesDetailView.as_view(), name="categories-detail"),
    path("ad/<int:pk>/", views.AdsDetaiView.as_view(), name="ads-detail"),
]
