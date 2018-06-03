from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext_lazy

from .models import *


# https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#modeladmin-objects

class AdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = gettext_lazy('IOE')

    # Text to put in each page's <h1>.
    site_header = gettext_lazy('IOE PUL')

    # Text to put at the top of the admin index page.
    index_title = gettext_lazy('IOE PUL MSC')


admin.site = AdminSite()

admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)

# Register your models here.
admin.site.register(Programme)
admin.site.register(Batch)
admin.site.register(Semester)
admin.site.register(Expert)
admin.site.register(Topic)
admin.site.register(Teacher)
admin.site.register(Subject)



