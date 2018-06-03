from django.contrib import admin
from django.contrib.admin import AdminSite, ModelAdmin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext_lazy

from .models import *


# https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#modeladmin-objects


class AdminSite(AdminSite):

    site_url = None

    # Text to put at the end of each page's <title>.
    site_title = gettext_lazy('IOE')

    # Text to put in each page's <h1>.
    site_header = gettext_lazy('IOE PUL')

    # Text to put at the top of the admin index page.
    index_title = gettext_lazy('IOE PUL MSC')




admin.site = AdminSite()
admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)


class ExpertAdmin(ModelAdmin):
    list_filter = ('affiliated_institute', 'upper_degree', 'aff_type')
    list_display = ('name', 'phone', 'email', 'affiliated_institute', 'upper_degree', 'aff_type', )
    search_fields = ('name', 'phone', 'email', 'affiliated_institute', 'upper_degree', 'aff_type')

    pass


class TopicAdmin(ModelAdmin):
    pass


class TeacherAdmin(ModelAdmin):

    list_filter = ( 'affiliated_institute','upper_degree', 'aff_type')
    list_display = ('name', 'phone', 'email', 'affiliated_institute','upper_degree', 'aff_type' )
    search_fields = ('name', 'phone', 'email', 'affiliated_institute','upper_degree', 'aff_type')

    pass


class SubjectAdmin(ModelAdmin):
    list_filter = ('program', 'semester')
    list_display = ('name', 'program', 'semester', 'subject_teacher', 'subject_teacher_teaching_experience_years')
    search_fields = ('name',)
    pass


admin.site.register(Expert, ExpertAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Programme)
admin.site.register(Semester)
