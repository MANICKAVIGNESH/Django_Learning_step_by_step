from django.contrib import admin
from movie_review_app.models import  CineProfessionals, Movie, MovieReview

# Register your models here.

admin.site.register(CineProfessionals)
admin.site.register(Movie)
admin.site.register(MovieReview)
