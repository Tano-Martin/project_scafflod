from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('name', 'date_add', 'date_update', 'status')

        # Configuration du champ de recherche
    search_fields = ('name', 'date_add')
    
@admin.register(models.Partner)
class PartnerAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('images_view', 'name', 'date_add', 'date_update', 'status')

        # Configuration du champ de recherche
    search_fields = ('name', 'date_add')

    def images_view(self, obj): #Permet d'avoir un aperçu des images
        return mark_safe(f'<img src="{obj.logo.url}" style="height:100px; width:200px">')

    images_view.short_description = 'Aperçu des images' # Titre de l'onglet dans l'admin

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('name', 'description', 'client', 'date_project', 'url_project', 'date_add', 'date_update', 'status')

        # Configuration du champ de recherche
    search_fields = ('name', 'date_add')

@admin.register(models.PictureProject)
class PictureProjectAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('picture', 'date_add', 'date_update', 'status')

        # Configuration du champ de recherche
    search_fields = ['date_add']

@admin.register(models.Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
        # Liste des champs a afficher
    list_display = ('images_view', 'name', 'poste', 'date_add', 'date_update', 'status')

        # Configuration du champ de recherche
    search_fields = ('name', 'date_add')

    def images_view(self, obj): #Permet d'avoir un aperçu des images
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:200px">')

    images_view.short_description = 'Aperçu des images' # Titre de l'onglet dans l'admin

