from django.contrib import admin

from apps.financeiro.models import contasapagar
from baton.admin import DropdownFilter, ChoicesDropdownFilter

# Register your models here.

@admin.register(contasapagar)
class ContasaPagarAdmin(admin.ModelAdmin):
    list_display = ('empresas', 'data_competencia_br', 'data_vencimento','conta','categoria','descricao', 'fornecedor', 'valor', 'pago')
    search_fields = ['empresas__nome','descricao','categoria__descricao','fornecedor__nome_fantasia']
    list_filter = (
                    ('empresas__nome', DropdownFilter),
                    ('categoria__descricao', DropdownFilter),
                    ('descricao', DropdownFilter),
                    ('fornecedor__nome_fantasia', DropdownFilter),
                    ('data_vencimento', DropdownFilter),
                    ('pago', DropdownFilter),
                )
    list_per_page = 5

    @admin.display(description='Data de Compra')
    def data_competencia_br(self, obj):
        if obj.data_competencia:
            return obj.data_competencia.strftime('%d/%m/%Y')