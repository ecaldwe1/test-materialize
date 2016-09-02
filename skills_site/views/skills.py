# View file for developer pages
from django.views.generic import *
from skills_site.models import Skill, Developer, DeveloperSkill
from skills_site.views import developer
from django.core.urlresolvers import reverse

# ListView that lists all of the skills using the skills_list_materialize.html template
class SkillsList(ListView):

    model = Skill
    template_name = 'skill_list_materialize.html'

    def get_queryset(self):
        q = super(SkillsList, self).get_queryset()
        return q.order_by('name')
