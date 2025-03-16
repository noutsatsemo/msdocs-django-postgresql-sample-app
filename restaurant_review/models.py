from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.core.validators import MaxValueValidator, MinValueValidator, EmailValidator
from django.core.exceptions import ValidationError
import re
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight



LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

def validate_phone(value):
    phone_pattern = re.compile(r'^\+?[0-9\s\-\(\)]+$')
    if not phone_pattern.match(value):
        raise ValidationError("Bitte eine gültige Telefonnummer eingeben (z.B. +49 123 4567890).")


# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class SillaUser(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, default='default@example.com', validators=[EmailValidator(message="Bitte eine gültige E-Mail-Adresse eingeben.")])
    phone = models.CharField(max_length=20, default='+41899584555',  validators=[validate_phone])
    birthday = models.DateField()
    owner = models.ForeignKey('auth.User', related_name='sillausers', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['email']


class SillaProject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    total_material_cost_price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_labor_cost_price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_other_cost_price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    owner = models.ForeignKey('auth.User', related_name='sillaprojects', on_delete=models.CASCADE)
    
    def total_cost(self):
        return self.total_material_cost_price + self.total_labor_cost_price + self.total_other_cost_price

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_text = models.CharField(max_length=500)
    review_date = models.DateTimeField('review date')

    def __str__(self):
        return f"{self.restaurant.name} ({self.review_date:%x})"
