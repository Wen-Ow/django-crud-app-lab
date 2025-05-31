import django.forms as forms

class WatchlistForm(forms.Form):
    class Meta:
        fields: ['title', 'genre', 'description', 'watched', 'rating', 'release_year']