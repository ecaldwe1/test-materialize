from django.contrib import admin
from skills_site.models import Skill, Developer, DeveloperSkill, ExtraCredit, Project, ProjectDeveloper, ProjectSkill

# Register your models here.

# Skill admin configuration
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'family')
    list_filter = ('difficulty', 'family')

admin.site.register(Skill, SkillAdmin)


# Developer admin configuration
admin.site.register(Developer)


# DeveloperSkills admin configuration
class DeveloperSkillAdmin(admin.ModelAdmin):
    list_display = ('get_developer_username', 'skill', 'proficiency', 'years_of_experience')
    list_filter = ('skill', 'proficiency', 'years_of_experience')

    def get_developer_username(self, obj):
        return obj.developer.user.username

    get_developer_username.short_description = 'Developer Username'

admin.site.register(DeveloperSkill, DeveloperSkillAdmin)


# ExtraCredit admin configuration
admin.site.register(ExtraCredit)

# Project admin configuration
admin.site.register(Project)

# ProjectSkills admin configuration
class ProjectSkillAdmin(admin.ModelAdmin):
    list_display = ('project', 'skill')
    list_filter = ('skill', 'project')

admin.site.register(ProjectSkill, ProjectSkillAdmin)

# ProjectDeveloper admin configuration
class ProjectDeveloperAdmin(admin.ModelAdmin):
    list_display = ('get_project_developer_username', 'project')
    list_filter = ('developer', 'project')

    def get_project_developer_username(self, obj):
        return obj.developer.user.username

    get_project_developer_username.short_description = 'Project Developer Username'

admin.site.register(ProjectDeveloper, ProjectDeveloperAdmin)