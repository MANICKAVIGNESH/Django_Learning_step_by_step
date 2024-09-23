from django.db import models

# Create your models here.

class CineProfessionals(models.Model):

    '''
    To store information about cine professional
    '''

    name = models.CharField(max_length=200)
    profile = models.TextField()
    date_of_birth = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    '''
    To store information about movies 
    '''

    title = models.CharField(max_length=200)
    plot = models.TextField()
    cast = models.ManyToManyField(CineProfessionals, related_name="movie_cast")
    producer = models.ForeignKey(CineProfessionals, related_name="movie_producer", on_delete=models.CASCADE)
    director = models.ForeignKey(CineProfessionals, related_name="movie_director", on_delete=models.CASCADE)

class MovieReview(models.Model):

    movie = models.ForeignKey(Movie, related_name="movie_review", on_delete=models.CASCADE)
    review = models.TextField()