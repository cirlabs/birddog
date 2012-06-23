# Create your views here.
from django.views.generic import ListView, TemplateView, DetailView
from apps.requests.models import Agency, Event, Request

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