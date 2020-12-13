from django import forms
from .models import Quote


class QuoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuoteForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class': ' placeholder-blue-600 placeholder-opacity-75 border-2 text-pink-600 text-sm font-bold rounded-lg px-2 py-1 my-2'}
        self.fields['position'].widget.attrs = {
        'class': ' placeholder-blue-600 placeholder-opacity-75 border-2 text-pink-600 text-sm font-bold rounded-lg px-2 py-1 my-2'}
        self.fields['company'].widget.attrs = {
        'class': ' placeholder-blue-600 placeholder-opacity-75 border-2 text-pink-600 text-sm font-bold rounded-lg px-2 py-1 my-2'}
        self.fields['address'].widget.attrs = {
            'class': ' placeholder-blue-600 placeholder-opacity-75 border-2 text-pink-600 text-sm font-bold rounded-lg px-2 py-1 my-2'}
        self.fields['email'].widget.attrs = {
            'class': ' placeholder-blue-600 placeholder-opacity-75 border-2 text-pink-600 text-sm font-bold rounded-lg px-2 py-1 my-2'}
        self.fields['web'].widget.attrs = {
            'class': ' placeholder-blue-600 placeholder-opacity-75 border-2 text-pink-600 text-sm font-bold rounded-lg px-2 py-1 my-2'}
        self.fields['description'].widget.attrs = {
            'class': ' placeholder-blue-600 placeholder-opacity-75 border-2 text-pink-600 text-sm font-bold rounded-lg px-2 py-1 my-2'}
        self.fields['job_file'].widget.attrs = {'class': 'my-2'}
        self.fields['priority'].widget.attr = {'class': 'my-2'}
        self.fields['site_status'].widget.attr = {'class': 'my-2'}

    class Meta:
        model = Quote
        fields = ('name', 'position', 'company', 'address',
                  'email', 'web', 'description', 'site_status',
                  'priority', 'job_file')
