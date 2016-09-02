# View file for developer pages
from django.views.generic import *
from skills_site.models import Skill
from django.core.urlresolvers import reverse

# ListView that lists all of the skills using the skills_list_materialize.html template
class SkillsList(ListView):

    model = Skill
    template_name = 'skill_list_materialize.html'

    # def get_context_data(self, **kwargs):
    #     context = super(PeopleList, self).get_context_data(**kwargs)
    #     return context
    def get_queryset(self):
        q = super(SkillsList, self).get_queryset()
        return q.order_by('name')