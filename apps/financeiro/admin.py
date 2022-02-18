from django.contrib import admin

from apps.financeiro.models import contasapagar
from baton.admin import DropdownFilter, ChoicesDropdownFilter

# Register your models here.

@admin.register(contasapagar)
class ContasaPagarAdmin(admin.ModelAdmin):
    list_display = ('empresas', 'data_competencia_br', 'categoria','descricao', 'fornecedor', 'valor', 'pago')
    search_fields = ('empresas__nome','data_competencia_br', 'descricao', 'categoria','fornecedor')
    list_filter = (
                    ('empresas__nome', DropdownFilter),
                    ('categoria__descricao', DropdownFilter),
                    ('descricao', DropdownFilter),
                    ('fornecedor__nome_fantasia', DropdownFilter),
                )
    list_per_page = 5

    @admin.display(description='Data')
    def data_competencia_br(self, obj):
        if obj.data_competencia:
            return obj.data_competencia.strftime('%d/%m/%Y')