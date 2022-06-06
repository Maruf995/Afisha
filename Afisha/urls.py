from django.contrib import admin
from django.urls import path
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/directors/', views.Director_Create_ListView),
    path('api/v1/directors/<int:id>/', views.DirectorDetailView),

    path('api/v1/movies/', views.Movie_Create_ListView),
    path('api/v1/movies/<int:id>/', views.MovieDetailView),
    path("api/v1/movies/reviews/", views.Movie_Create_ListView),

    path('api/v1/reviews/', views.Review_Create_ListView),
    path('api/v1/reviews/<int:id>/', views.ReviewDetailView),
]
