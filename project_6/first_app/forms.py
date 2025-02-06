from django import forms
from django.core import validators

# widgets == field to html input
class contactForm(forms.Form):
    name = forms.CharField(label="Full Name : ", help_text="Total length must be within 70 characters", required=False, error_messages={'required': 'Please enter your name.'},widget = forms.Textarea(attrs = {'id' : 'text_area', 'class' : 'class1 class 2', 'placeholder' : 'Enter your name'},))
    email = forms.EmailField(label = "User Email")
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput)
    check = forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget = forms.RadioSelect)
    MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)



# class StudentData(forms.Form):
#     name=forms.CharField(widget=forms.TextInput)
#     email=forms.CharField(widget=forms.EmailInput)
#     # def clean_name(self):
#     #     valname=self.cleaned_data['name']
#     #     if len(valname)<10:
#     #         raise forms.ValidationError("Enter a name with at least 10 character")
#     #     return valname
#     # def clean_Email(self):
#     #     valEmail=self.cleaned_data['email']
#     #     if '.com' not in valEmail:
#     #          raise forms.ValidationError("Your email must contain .com")
    
#     def clean(self):
#         cleaned_data= super().clean()
#         valname=self.cleaned_data['name']
#         valEmail=self.cleaned_data['email']
#         if len(valname)<10:
#           raise forms.ValidationError("Enter a name with at least 10 character")
#         if '.com' not in valEmail:
#           raise forms.ValidationError("Your email must contain .com")
    

def len_check(value):
    if len(value)<10:
        raise forms.ValidationError("Enter max 10 character")
class StudentData(forms.Form):
    name=forms.CharField(widget=forms.TextInput,validators=[validators.MaxLengthValidator(10,message='Enter a value with 10 char')])
    email=forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message='Enter valid message')])
    age=forms.IntegerField(validators=[validators.MaxValueValidator(34,message="Age at least 34"),validators.MinValueValidator(24,message="Age at least 24")])
    text=forms.CharField(widget=forms.TextInput,validators=[len_check])
    fire=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],message="File must be pdf")])

class PasswordValidationProject(forms.Form):
  name=forms.CharField(widget=forms.TextInput)
  password=forms.CharField(widget=forms.PasswordInput)
  confirmPassword=forms.CharField(widget=forms.PasswordInput)

  def clean(self):
      cleaned_data= super().clean()
      val_pass=self.cleaned_data['password']
      val_con=self.cleaned_data['confirmPassword']
      if val_pass !=val_con:
          raise forms.ValidationError("password is not matched")