from django.contrib import admin
# Register your models here.
from .models import Lab,User
# from import_export import resources

@admin.register(Lab)
class LabAdmin(admin.ModelAdmin):
    list_display =("id","name","address")
    list_filter = ("name","id")
    search_fields = ("name","id")
    ordering      = ("name",)
    list_per_page = 15


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display =("id","username","email")
    list_filter = ("email",)
    search_fields = ("username","id")
    ordering      = ("id",)
    list_per_page = 15



# from import_export.admin import ImportExportModelAdmin

# class BookResource(resources.ModelResource):

#     class Meta:
#         model = Lab

# class BookAdmin(ImportExportModelAdmin):
#     resource_class = BookResource

# admin.site.register(Lab, BookAdmin)



