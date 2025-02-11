from django import forms
from django.forms.widgets import NumberInput

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
class userForm(forms.Form):

  name= forms.CharField()
  comment = forms.CharField(widget=forms.Textarea)
  comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
  email = forms.EmailField()
  agree = forms.BooleanField()
  date = forms.DateField()
  birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
  value = forms.DecimalField()
  favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
  favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)