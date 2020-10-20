from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import IntegerRangeField

# Create your models here.

#cuisine model
class Cuisine(models.Model):
    cuisinename=models.CharField(max_length=255)

    def __str__(self):
        return self.cuisinename

    class Meta:
        db_table='cuisine'
        verbose_name_plural='cuisines'

#dietary model --- ex: vegeterian, gluten-free, lactose-free, etc.
class Dietary(models.Model):
    dietarytype=models.CharField(max_length=255)

    def __str__(self):
        return self.dietarytype
    
    class Meta:
        db_table='dietary'
        verbose_name_plural='dietary types'

#difficulty model
class Difficulty(models.Model):
    difficultylevel=models.CharField(max_length=255)

    def __str__(self):
        return self.difficultylevel

    class Meta:
        db_table='difficulty'
        verbose_name_plural='difficulty levels'

#dishtype model --- ex: one-pot, stew, stir-fry, etc.
class DishType(models.Model):
    dishtypename=models.CharField(max_length=255)

    def __str__(self):
        return self.dishtypename
    
    class Meta:
        db_table='dishtype'
        verbose_name_plural='dishtypes'

#occassion model --- ex: christmas, thanksgiving
class Occassion(models.Model):
    occassiontype=models.CharField(max_length=255)

    def __str__(self):
        return self.occassiontype

    class Meta:
        db_table='occassion'
        verbose_name_plural='occassions'

#rating model
class Rating(models.Model):
    ratingstar=models.IntegerRangeField(min_value=1, max_value=5, null=True, blank=True)

    def __str__(self):
        return str(self.ratingstar)

    class Meta:
        db_table='rating'
        verbose_name_plural='ratings'

#recipe model
class Recipe(models.Model):
    recipename = models.CharField(max_length = 255)
    recipedescription = models.CharField(max_length = 255)
    recipeinstruction = models.TextField()
    servingsize = models.SmallIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    preptime = models.CharField(max_length=11)
    cooktime = models.CharField(max_length=11)
    totaltime = models.CharField(max_length=11)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dietary = models.ManyToManyField(Dietary)
    cuisine = models.ManyToManyField(Cuisine)
    dishtype = models.ManyToManyField(DishType)
    occassion = models.ManyToManyField(Occassion)

    def __str__(self):
        return self.recipename
    
    class Meta:
        db_table='recipe'
        verbose_name_plural='recipes'

#review model
class Review(models.Model):
    reviewtitle=models.CharField(max_length=255)
    reviewdate=models.DateField()
    recipe=models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    rating=models.ForeignKey(Rating, on_delete=models.CASCADE)
    reviewtext=models.TextField()

    def __str__(self):
        return self.reviewtitle
    
    class Meta:
        db_table='review'
        verbose_name_plural='reviews'

#comment model
class Comment(models.Model):
    commentdate=models.DateField()
    commenttext=models.TextField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.commenttext

    class Meta:
        db_table='comment'
        verbose_name_plural='comments'


#ingredient model
class Ingredient(models.Model):
    ingredientname=models.CharField(max_length=255)
    measurement=models.CharField(max_length=255)
    recipe=models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredientname

    class Meta:
        db_table='ingredient'
        verbose_name_plural='ingredients'


#favorite model
class Favorite(models.Model):
    foldername=models.CharField(max_length=255)
    recipe=models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user=models.ManyToManyField(User)

    def __str__(self):
        return self.foldername

    class Meta:
        db_table='favorite'
        verbose_name_plural='favorites'






