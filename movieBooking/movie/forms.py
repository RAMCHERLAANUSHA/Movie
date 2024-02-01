from django import forms
from movie.models import  Location, Movie, Theatre, Premium_Movie, Movie_cast, Events, User, Payment, Adds
from django.forms import Select

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"

class LocationForm(forms.ModelForm):
    class Meta:
        model=Location
        fields="__all__"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['movie'].queryset = Movie.objects.all()
        self.fields['movie'].label_from_instance = lambda obj: f"{obj.movie_name}"
        
class TheatreForm(forms.ModelForm):
    class Meta:
        model = Theatre
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].queryset = Location.objects.all()
        self.fields['location'].label_from_instance = lambda obj: f"{obj.location}"
        self.fields['movie'].queryset = Movie.objects.all()
        self.fields['movie'].label_from_instance = lambda obj: f"{obj.movie_name}"

class Premium_MovieForm(forms.ModelForm):
    class Meta:
        model = Premium_Movie
        fields = '__all__'

class Movie_castForm(forms.ModelForm):
    class Meta:
        model = Movie_cast
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['movie_name'].queryset = Movie.objects.all()
        self.fields['movie_name'].label_from_instance = lambda obj: f"{obj.movie_name}"


class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].queryset = Location.objects.all()
        self.fields['location'].label_from_instance = lambda obj: f"{obj.location}"

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class PaymentForm(forms.ModelForm):
    filter_prize = forms.ChoiceField(choices=(
                (100,"0-100"),
                (200,"100-200"),
                (300,"200-300"),
                (400,"300-400")
    ))
    class Meta:
        model = Payment
        fields = '__all__'
        exclude = ['user','total_cost'] 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['theatre'].queryset = Theatre.objects.all()
        self.fields['theatre'].label_from_instance = lambda obj: f"{obj.theatre_name}"
        self.fields['location'].queryset = Location.objects.all()
        self.fields['location'].label_from_instance = lambda obj: f"{obj.location}"
    widgets = {
        'Prize' : Select(attrs={
                'class': "form-control", 
                'style': 'width: 280px;height: 18px;padding: 7px;border-radius: 10px;border-width: 1px;border-color: rgba(0, 0, 0, 0.2);',
                })
    }

class AddsForm(forms.ModelForm):
    class Meta:
        model = Adds
        fields = '__all__'