from django.db import models

class Hero(models.Model):
  name = models.CharField(max_length=200, help_text = 'The name of the hero')
  image = models.FileField(upload_to='gallery')
  description = models.TextField(help_text='Describe the individual')
  power_type = models.CharField(max_length=50, help_text='') 
  strength = models.IntegerField(help_text='A score between 0 and 10')
  durability = models.IntegerField(help_text='A score between 0 and 10')
  intelligence = models.IntegerField(help_text='A score between 0 and 10')
  fighting_ability = models.IntegerField(help_text='A score between 0 and 10')
  tech = models.IntegerField(help_text='A score between 0 and 10')
  sanity = models.IntegerField(help_text='A score between 0 and 10')
  xFactor = models.IntegerField(help_text='A score between 0 and 10')

  def __str__(self):
    return self.name