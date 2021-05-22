from django.contrib import admin
from .models import Communaute, Priorite, Post


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


admin.site.register(Communaute)
admin.site.register(Priorite)
admin.site.register(Post, PostAdmin)