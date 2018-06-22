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
    site_title = gettext_lazy('MSc Teachers & Experts Database - IOE, DOECE')

    # Text to put in each page's <h1>.
    site_header = gettext_lazy('MSc Teachers & Experts Database')

    # Text to put at the top of the admin index page.
    index_title = gettext_lazy('Welcome!')


admin.site = AdminSite()
admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)


class ExpertAdmin(ModelAdmin):
    list_display = (
        'full_name', 'mobile_phone', 'email', 'organization', 'upper_degree',  'get_topics')
    list_filter = ('organization__institute_name', 'upper_degree',)
    search_fields = (
        'first_name', 'last_name', 'middle_name', 'salutation', 'mobile_phone', 'email', 'organization__institute_name',
        'upper_degree', 'topic__name')

    def get_topics(self, obj):
        return ",\n".join([p.name for p in obj.topic.all()])

    get_topics.short_description = "Topics Known"

    pass


class TopicAdmin(ModelAdmin):
    pass


class TeacherAdmin(ModelAdmin):
    list_filter = ('affiliated_institute__institute_name', 'upper_degree', 'aff_type')
    list_display = (
        'full_name', 'mobile_phone', 'email', 'affiliated_institute', 'upper_degree', 'aff_type', 'get_known_subjects')
    search_fields = (
        'first_name', 'last_name', 'middle_name', 'salutation', 'mobile_phone', 'email',
        'affiliated_institute__institute_name',
        'upper_degree', 'aff_type', 'known_subjects__name')

    def get_known_subjects(self, obj):
        return ",\n".join([p.name for p in obj.known_subjects.all()])

    get_known_subjects.short_description = "Subjects Known"
    pass


class SubjectAdmin(ModelAdmin):
    list_filter = ('program', 'semester', 'elective')
    list_display = (
        'name', 'program', 'semester', 'subject_teacher', 'subject_teacher_teaching_experience_years', 'elective')
    search_fields = ('name', 'subject_teacher__first_name', 'subject_teacher_teaching_experience_years',)
    pass


admin.site.register(Expert, ExpertAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Programme)
admin.site.register(Semester)
admin.site.register(AffiliatedInstitute)
