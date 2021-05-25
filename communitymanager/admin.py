from django.contrib import admin
from .models import Communaute, Priorite, Post, Commentaire


class PostAdmin(admin.ModelAdmin):
    list_display = ('titre', 'communaute', 'date_creation', 'auteur')
    list_filter = ('titre', 'communaute', 'date_creation', 'auteur', 'priorite')
    ordering = ('date_creation', )
    search_fields = ('titre', 'communaute')
    fieldsets = (
        #meta info
        ('General', {
            'fields': ('titre', 'communaute', 'auteur', 'priorite')
        }),
        ('Description', {
            'fields': ['description']
        }),
        ('Evenement', {
            'classes': ['collapse', ],
            'fields': ('evenementiel', 'date_evenement')
        }),
    )

class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('post', 'auteur', 'date_creation')
    list_filter = ('post', 'auteur', 'date_creation')
    ordering = ('date_creation', )
    search_fields = ('post', 'auteur')
    fieldsets = (
        #meta info
        ('General', {
            'fields': ('post', 'auteur')
        }),
        ('Description', {
            'fields': ['contenu']
        })
    )


admin.site.register(Communaute)
admin.site.register(Priorite)
admin.site.register(Post, PostAdmin)
admin.site.register(Commentaire, CommentaireAdmin)