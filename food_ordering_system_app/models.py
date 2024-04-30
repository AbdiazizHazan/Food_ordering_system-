from django.db import models
from django.core.validators import RegexValidator
from django.forms import ModelForm, ValidationError



class CustomerDetails(models.Model):
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed without space.",
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=16)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email=models.EmailField()
    Address=models.CharField(max_length=50)
    Quantity=models.DecimalField(max_digits=2, decimal_places=0)



  
