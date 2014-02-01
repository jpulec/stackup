from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from stackup.apps.main.forms import SalaryForm

class Home(FormView):
    template_name = "main/home.html"
    form_class = SalaryForm

class Salary(TemplateView):
    template_name = "main/salary.html"
