from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import QuoteForm
from pages.models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Quote


# Create your views here.
@login_required(login_url=reverse_lazy('login'))
def create_quote(request):
    submitted = False
    if request.method == 'POST':
        form = QuoteForm(request.POST, request.FILES)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.username = request.user
            quote.save()
            submitted = True
    else:
        form = QuoteForm()
    context = {'submitted': submitted, 'form': form, 'pages': Page.objects.all()}
    return render(request, 'quotes/create_quote.html', context)


class QuoteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    context_object_name = 'all_quotes'

    def get_queryset(self):
        return Quote.objects.filter(username=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(QuoteList, self).get_context_data(**kwargs)
        context['pages'] = Page.objects.all()
        return context


class QuoteView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    context_object_name = 'quote'

    def get_queryset(self):
        return Quote.objects.filter(username=self.request.user)

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
