from django.contrib import admin

# Register your models here.
from djangoContact.models import Contact_us


class admin_contact(admin.ModelAdmin):
    list_display = ["__str__","name","email","is_read"]
    list_editable = ["is_read"]
    list_filter = ["is_read"]


admin.site.register(Contact_us,admin_contact)