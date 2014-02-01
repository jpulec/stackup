from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from stackup.apps.main.forms import SalaryForm
from stackup.apps.main.models import Region

class Home(FormView):
    template_name = "main/home.html"
    form_class = SalaryForm
    
class About(TemplateView):
    template_name = "main/about.html"

class Salary(ListView):
    model = Region
    context_object_name = "regions"
    template_name = "main/salary.html"

    def get(self, request, *args, **kwargs):
        if "salary" in self.request.GET and self.request.GET['salary'] and self.request.GET['salary'] != "0":
            pass
        else:
            return HttpResponseRedirect(reverse("home"))
        return super(Salary, self).get(request, *args, **kwargs)

