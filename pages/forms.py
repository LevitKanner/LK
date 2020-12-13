from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=20, label='Your name',
                           widget=forms.TextInput(attrs={'class': ' placeholder-blue-600 placeholder-opacity-75 border-2 text-pink-600 text-sm font-bold rounded-lg px-2 py-1 my-2'}))
    email = forms.EmailField(required=False, label='Your email',
                             widget=forms.EmailInput(attrs={'class': ' placeholder-blue-600 placeholder-opacity-75 border-2 text-pink-600 text-sm font-bold rounded-lg px-2 py-1 my-2'}))
    subject = forms.CharField(max_length=100,
                              widget=forms.TextInput(attrs={'class': ' placeholder-blue-600 placeholder-opacity-75 border-2 text-pink-600 text-sm font-bold rounded-lg px-2 py-1 my-2'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': ' placeholder-blue-600 placeholder-opacity-75 border-2 text-pink-600 text-sm font-bold rounded-lg px-2 py-1 my-2'}))
