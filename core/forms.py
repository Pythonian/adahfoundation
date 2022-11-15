from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)
    subject = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    body = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'rows': '7', 'placeholder': 'Enter your message...'}))
