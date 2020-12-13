from django.shortcuts import render
from .forms import QuoteForm
from pages.models import Page
from django.views.generic.list import ListView
from .models import Quote


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


class QuoteList(ListView):
    model = Quote
    context_object_name = 'all_quotes'
