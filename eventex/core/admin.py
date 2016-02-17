from django.contrib import admin
from django.contrib.admin import AdminSite
from eventex.core.models import Speaker, Contact


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'photo_img', 'website_link']

    def website_link(self, obj):
        return '<a href="{0}">{0}</a>'.format(obj.website)

    website_link.allow_tags = True

    website_link.short_description = 'website'

    def photo_img(self, obj):
        return '<img width="32px" src="{}" />'.format(obj.photo)

    photo_img.allow_tags = True
    photo_img.short_description = 'foto'


class MyAdminSite(AdminSite):
    AdminSite.site_header = "Eventex - Painel de Controle"

    AdminSite.index_title = ''


admin.site.register(Speaker, SpeakerModelAdmin)
