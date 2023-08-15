from django import forms


class SearchForm(forms.Form):
    input_values = forms.CharField(label='Input Values', widget=forms.TextInput(
        attrs={'placeholder': 'Enter comma-separated integers'}))
    search_value = forms.IntegerField(label='Search Value')
