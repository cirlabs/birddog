# Create your views here.
from django.views.generic import ListView, TemplateView, DetailView
from apps.requests.models import Agency, Event, Request
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext


from .forms import NewRequestForm, NewOptionalRequestForm


class RequestListView(ListView):
    """
    Main view showing the list of top donors. Used as an index page.
    """
    context_object_name = 'request_list'
    template_name = 'requests/request_list.html'
    queryset = Request.objects.all()

class RequestListViewPublic(ListView):
    """
    Main view showing the list of top donors. Used as an index page.
    """
    context_object_name = 'request_list'
    template_name = 'requests/request_list_public.html'
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
    template_name = 'requests/request_detail_public.html'
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
    
def request_add_support(request, slug, user_id):
    message = ''
    supporters = Request.objects.filter(slug=slug)[0].supporters.all()
    
    if len(supporters) > 0:
        success = False
        message = "You already support this request. Thanks for your support!"
    else:
        print User.objects.get(id=user_id)
        try:
            user = User.objects.get(id=user_id)
            Request.objects.get(slug=slug).supporters.add(user)
            supporters = Request.objects.get(slug=slug).supporters.all()
            success = True
            message = 'Thanks! You are now a public supporter of this request.'
        except:
            success = False
            message = 'Something went wrong (Invalid user id).'
    
    return render_to_response('requests/addsupport.json', {
        "success": success,
        "message": message,
        "supporters": supporters,
        },
        context_instance=RequestContext(request))
