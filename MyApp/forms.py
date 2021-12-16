from django.forms import ModelForm

# import GeeksModel from models.py
from .models import *


class appointmentForm(ModelForm):
    class Meta:
        model=appointment
        fields='__all__'

form=appointmentForm()



class contactform(ModelForm):
    class Meta:
        model=contact
        fields='__all__'
form=contactform()


class MedicineForm(ModelForm):
    class Meta:
        model=Medicine
        fields='__all__'
form=MedicineForm()