from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

PETTINGS = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pets_detail', kwargs={'pk': self.id})
        # default route to toys_details

class Digimon(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    level = models.IntegerField()
    pets = models.ManyToManyField(Pet)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"digimon_id": self.id})

    def played_for_today(self):
        return self.playtime_set.filter(date=date.today()).count() >= len(PETTINGS)
        # can also use len( self.feeding_set.filter(date=date.today()) ); less efficient
        # .count turns it into an integer, then we compare the the integer to the length of MEALS(3)
        # return true of >= 3, otherwise false

class Playtime(models.Model):
    date = models.DateField('Petting Date')
    petting = models.CharField(
        max_length = 1,
        choices = PETTINGS,
        default = PETTINGS[0][0]
    )

    # creating a digimon_id foreignkey; because Playtime belongs to a Digimon
    digimon = models.ForeignKey(Digimon, on_delete=models.CASCADE)
    
    # just because django
    # gives it a more 'normalized name to work with'
    def __str__(self):
        return f"{self.get_petting_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
        # dates in descending order