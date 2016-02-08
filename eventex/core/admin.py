from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


class MyAdminSite(AdminSite):

    AdminSite.site_header = "Eventex - Painel de Controle"

    AdminSite.index_title = ''

