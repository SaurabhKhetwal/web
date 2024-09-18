from django.contrib import admin
from ci_formdata.models import form

# Register your models here.
class FormAdmin(admin.ModelAdmin):
    list_display=('form_fullname','form_email','form_number','form_choice')
    
admin.site.register(form,FormAdmin)
