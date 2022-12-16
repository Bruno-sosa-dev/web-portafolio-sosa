from django.contrib import admin
from .models import Portfolio, Project, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(Category, CategoryAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ["title", "portfolio_categories", "created", "updated"]
    
    def portfolio_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    portfolio_categories.short_description = "Categorias"

admin.site.register(Portfolio, PortfolioAdmin)


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ["title", "projects_categories", "created", "updated"]
    
    def projects_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    projects_categories.short_description = "Categorias"
    
admin.site.register(Project, ProjectAdmin)