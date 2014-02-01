from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Max, Q

from stackup.apps.main.forms import SalaryForm
from stackup.apps.main.models import Region, StandardOfLiving

class Home(FormView):
    template_name = "main/home.html"
    form_class = SalaryForm
    
class About(TemplateView):
    template_name = "main/about.html"

class Salary(ListView):
    context_object_name = "standards"
    template_name = "main/salary.html"

    def get(self, request, *args, **kwargs):
        if "salary" in self.request.GET and self.request.GET['salary'] and self.request.GET['salary'] != "0":
            pass
        else:
            return HttpResponseRedirect(reverse("home"))
        return super(Salary, self).get(request, *args, **kwargs)

    def get_queryset(self):
        model_max_set = StandardOfLiving.objects.filter(threshold__lte=self.request.GET['salary']).values('region').annotate(max_star_level=Max('star_level')).order_by()

        q_statement = Q()
        for pair in model_max_set:
            q_statement |= (Q(region__exact=pair['region']) & Q(star_level=pair['max_star_level']))
        model_set = StandardOfLiving.objects.filter(q_statement)
        return model_set
