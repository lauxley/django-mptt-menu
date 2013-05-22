from django.contrib import admin

from example_app.models import ExampleModel


class ExampleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(ExampleModel, ExampleAdmin)
