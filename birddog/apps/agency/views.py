# Create your views here.
from django.views.generic import ListView, TemplateView, DetailView
from django.utils.decorators import method_decorator
from django.shortcuts import render_to_response, get_object_or_404


from .models import Agency


class AgencyListView(ListView):
    """
    Main view showing the list of agencies. Used as an index page.
    """
    context_object_name = 'agency_list'
    template_name = 'agency/agency_list.html'
    queryset = Agency.objects.all()


class AgencyDetailView(DetailView):
    """
    Returns a specific agency using the slug as the unique identifier
    """
    context_object_name = 'agency'
    template_name = 'agency/agency_detail.html'
    queryset = Agency.objects.all()

    def dispatch(self, *args, **kwargs):
        return super(AgencyDetailView, self).dispatch(*args, **kwargs)
