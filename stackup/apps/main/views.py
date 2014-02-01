from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from stackup.apps.main.forms import SalaryForm

class Home(FormView):
    template_name = "main/home.html"
    form_class = SalaryForm

class Salary(TemplateView):
    template_name = "main/salary.html"

    def get(self, request, *args, **kwargs):
        if "salary" in self.request.GET and self.request.GET['salary']:
            pass
        else:
            return HttpResponseRedirect(reverse("home"))
        return super(Salary, self).get(request, *args, **kwargs)

