from django import forms


class PostCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(max_length=254, min_length=2)
    description = forms.CharField(widget=forms.Textarea())
    rate = forms.FloatField()
