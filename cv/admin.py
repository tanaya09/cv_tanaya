from django.contrib import admin
from .models import ContactInfo, Education, Skill, Experience, Project

admin.site.register(ContactInfo)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Project)