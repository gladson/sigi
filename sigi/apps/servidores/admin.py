# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.contenttypes import generic
from sigi.apps.servidores.models import Servidor, Funcao, Licenca, Ferias
from sigi.apps.contatos.models import Endereco, Telefone

class FuncaoInline(admin.TabularInline):
    model = Funcao
    extra = 1

class FuncaoAdmin(admin.ModelAdmin):
    list_display = ('servidor', 'funcao', 'cargo','inicio_funcao', 'fim_funcao')
    list_filter  = ('inicio_funcao', 'fim_funcao')
    search_fields = ('funcao', 'cargo', 'descricao',
                     'servidor__nome_completo', 'servidor__obs', 'servidor__apontamentos',
                     'servidor__user__email', 'servidor__user__first_name',
                     'servidor__user__last_name', 'servidor__user__username')

class FeriasInline(admin.TabularInline):
    model = Ferias
    extra = 1

class FeriasAdmin(admin.ModelAdmin):
    list_display = ('servidor', 'inicio_ferias', 'fim_ferias')
    list_filter  = ('servidor', 'inicio_ferias', 'fim_ferias')
    search_fields = ('obs',
                     'servidor__nome_completo', 'servidor__obs', 'servidor__apontamentos',
                     'servidor__user__email', 'servidor__user__first_name',
                     'servidor__user__last_name', 'servidor__user__username')

class LicencaInline(admin.TabularInline):
    model = Licenca
    extra = 1

class LicencaAdmin(admin.ModelAdmin):
    list_display = ('servidor', 'inicio_licenca', 'fim_licenca')
    list_filter  = ('servidor', 'inicio_licenca', 'fim_licenca')
    search_fields = ('obs',
                     'servidor__nome_completo', 'servidor__obs', 'servidor__apontamentos',
                     'servidor__user__email', 'servidor__user__first_name',
                     'servidor__user__last_name', 'servidor__user__username')

class EnderecoInline(generic.GenericTabularInline):
    model = Endereco
    extra = 1
    raw_id_fields = ('municipio',)

class TelefonesInline(generic.GenericTabularInline):
    extra = 1
    model = Telefone

class ServidorAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'servico')
    list_filter  = ('sexo', 'servico')
    search_fields = ('nome_completo', 'obs', 'apontamentos',
                     'user__email', 'user__first_name',
                     'user__last_name', 'user__username')
    inlines= (EnderecoInline, TelefonesInline)

admin.site.register(Servidor, ServidorAdmin)
admin.site.register(Funcao, FuncaoAdmin)
admin.site.register(Ferias, FeriasAdmin)
admin.site.register(Licenca, LicencaAdmin)