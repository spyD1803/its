from django.forms import CheckboxInput, CharField, BooleanField, FloatField, TextInput, Textarea, FileInput,SelectMultiple,IntegerField,ChoiceField,NumberInput,Select
from django.contrib.auth.forms import *

class insert_form(forms.Form):

    latitude = FloatField(initial=13.5546534005, widget=NumberInput(attrs={'class' : 'form-control','id':'latitude'}))
    longitude = FloatField(initial=80.0273822403, widget=NumberInput(attrs={'class' : 'form-control','id':'longitude'}))
    temperature = IntegerField(widget=NumberInput(attrs={'class' : 'form-control','id':'temperature'}))
    humidity = IntegerField(widget=NumberInput(attrs={'class' : 'form-control','id':'humidity'}))
    co2 = IntegerField(widget=NumberInput(attrs={'class' : 'form-control','id':'co2'}))
    smoke = IntegerField(widget=NumberInput(attrs={'class' : 'form-control','id':'smoke'}))