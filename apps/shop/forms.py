from django import forms


class Search(forms.Form):
    search_field = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'search-field', 'placeholder': 'поиск'})
    )
