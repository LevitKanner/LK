from django.shortcuts import render
from .models import Page
from django.shortcuts import get_object_or_404, get_list_or_404
from .forms import ContactForm
from django.core.mail import get_connection, send_mail


# Create your views here.
def index(request, page_name):
    page_name = '/' + page_name
    pg = get_object_or_404(Page, permalink=page_name)
    pages = get_list_or_404(Page)
    context = {'title': pg.title, 'content': pg.body_text, 'last_updated': pg.update_date, 'pages': pages}
    return render(request, 'pages/index.html', context)


def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            connection = get_connection('django.core.mail.backends.console.EmailBackend', fail_silently=True)
            send_mail(cd['subject'],
                      cd['message'],
                      cd.get('email', 'noreply@gmai.com'),
                      ['lkanner21@gmail.com'], connection=connection)
            submitted = True
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form, 'submitted': submitted, 'pages': Page.objects.all()})

