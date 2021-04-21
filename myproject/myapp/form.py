from django import forms


class Feedback(forms.Form):
    title = forms.CharField(label="title", max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    subject = forms.CharField(label="Subject Descreption", max_length=50,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.CharField(label="email" , max_length=50 , widget = forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.IntegerField(label="phone", widget = forms.NumberInput(attrs={'class':'form-control'}))