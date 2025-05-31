import django.forms as forms
from .models import Watchlist
class WatchlistForm(forms.ModelForm):
    class Meta:
        model = Watchlist
        fields = ['title', 'genre', 'description', 'watched', 'rating', 'release_year']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter genre'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'watched': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter rating (1-10)'}),
            'release_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter release year'}),
        }