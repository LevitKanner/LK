from django.shortcuts import render
from .forms import QuoteForm
from pages.models import Page


# Create your views here.
def create_quote(request):
    submitted = False
    if request.method == 'POST':
        form = QuoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        form = QuoteForm()
    context = {'submitted': submitted, 'form': form, 'pages': Page.objects.all()}
    return render(request, 'quotes/create_quote.html', context)
