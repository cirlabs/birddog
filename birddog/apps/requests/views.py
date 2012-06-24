# Create your views here.
from django.views.generic import ListView, TemplateView, DetailView
from apps.requests.models import Agency, Event, Request
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from .forms import NewRequestForm, NewOptionalRequestForm


class RequestListView(ListView):
    """
    Main view showing the list of top donors. Used as an index page.
    """
    context_object_name = 'request_list'
    template_name = 'requests/request_list.html'
    queryset = Request.objects.all()


class RequestDetailView(DetailView):
    """
    Returns a specific request using the slug as the unique identifier
    """
    context_object_name = 'request'
    template_name = 'requests/request_detail.html'
    queryset = Request.objects.all()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RequestDetailView, self).dispatch(*args, **kwargs)
        
class RequestDetailViewPublic(DetailView):
    """
    Returns a specific request using the slug as the unique identifier
    """
    context_object_name = 'request'
    template_name = 'requests/request_detail.html'
    queryset = Request.objects.all()

    def dispatch(self, *args, **kwargs):
        return super(RequestDetailViewPublic, self).dispatch(*args, **kwargs)


@login_required
def new_request(request):
    reqform = NewRequestForm(request.POST or None, label_suffix='')
    optform = NewOptionalRequestForm(request.POST or None, label_suffix='')

    if request.method == 'POST' and reqform.is_valid() and optform.is_valid():

        new_request = reqform.save(commit=False)
        new_request.author = request.user
        new_request.status = 'P'


        # Combine both forms and save
        optform = NewOptionalRequestForm(data=request.POST, instance=new_request)
        optform.save()
        reqform.save_m2m()

        return redirect('request_list')

    ctx = dict(reqform=reqform, optform=optform)
    template_name = "requests/new.html"
    return render(request, template_name, ctx)
