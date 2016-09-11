from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from advocates.models import Session
from django.views.generic import *
from django.core.urlresolvers import reverse_lazy
from advocates.forms import SessionForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

class SessionList(ListView):
    model = Session

class SessionDetail(DetailView):
    model = Session


class SessionCreate(CreateView):
    model = Session
    form_class = SessionForm
    success_url = reverse_lazy('sessions_list')


class SessionUpdate(UpdateView):
    model = Session
    form_class = SessionForm
    success_url = reverse_lazy('sessions_list')


#@login_required
#def submit_session(request):
#    return render(request, 'app/submit_session.html')

