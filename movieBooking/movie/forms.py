from django import forms
from movie.models import  Location, Movie, Theatre, Premium_Movie, Movie_cast, Events, User, Payment, Adds

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
    class Meta:
        model = Payment
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.all()
        self.fields['user'].label_from_instance = lambda obj: f"{obj.firstname}"
        self.fields['location'].queryset = Location.objects.all()
        self.fields['location'].label_from_instance = lambda obj: f"{obj.location}"

class AddsForm(forms.ModelForm):
    class Meta:
        model = Adds
        fields = '__all__'