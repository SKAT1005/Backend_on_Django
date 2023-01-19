from django import forms


class FilterForm(forms.Form):
    name = forms.CharField(max_length=1024)


class ReviewsForm(forms.Form):
    text = forms.CharField(max_length=2048)