from django.contrib import admin

from baton.admin import DropdownFilter, ChoicesDropdownFilter
from apps.config.models import empresa 
# Register your models here.

@admin.register(empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'razaosocial', 'codigo_erp', 'cnpj' , 'data_criacao_br')
    search_fields = ('nome', 'razaosocial')
    list_filter = (
                    ('nome', DropdownFilter),
                    ('codigo_erp', DropdownFilter),
                )
    list_editable = ('razaosocial','codigo_erp',)
    list_per_page = 5

    @admin.display(description='Data de Criação')
    def data_criacao_br(self, obj):
        if obj.data_criacao:
            return obj.data_criacao.strftime('%d/%m/%Y')