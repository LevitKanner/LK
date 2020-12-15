from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import QuoteForm
from pages.models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(QuoteList, self).get_context_data(**kwargs)
        context['pages'] = Page.objects.all()
        return context


class QuoteView(DetailView):
    model = Quote
    context_object_name = 'quote'

    def get_context_data(self, **kwargs):
        context = super(QuoteView, self).get_context_data(**kwargs)
        context['pages'] = Page.objects.all()
        return context


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)
