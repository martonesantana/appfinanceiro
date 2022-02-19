from django.contrib import admin

from apps.financeiro.models import contasapagar
from baton.admin import DropdownFilter
from rangefilter.filters import DateRangeFilter

# Register your models here.

@admin.register(contasapagar)
class ContasaPagarAdmin(admin.ModelAdmin):
    list_display = ('empresas', 'data_competencia', 'data_vencimento','conta','categoria','descricao', 'fornecedor', 'valor', 'pago')
    search_fields = ['empresas__nome','descricao','categoria__descricao','fornecedor__nome_fantasia']
    list_filter = (
                    ('empresas__nome', DropdownFilter),
                    ('categoria__descricao', DropdownFilter),
                    ('descricao', DropdownFilter),
                    ('fornecedor__nome_fantasia', DropdownFilter),
                    ('data_competencia', DateRangeFilter),
                    ('data_vencimento', DateRangeFilter),
                    ('pago', DropdownFilter),
                )
    list_per_page = 5
    fieldsets = (
        (None, {
            "fields":[ (
                       'descricao',
                       'categoria',
            )],
        }),
        (None, {
            "fields":[ ('conta', 'valor'),
                       ('data_competencia','data_vencimento',),
            ],
        }),
        (None, {
            "fields":[ ('fornecedor', 'centrocustos'),
                       ('documentos', 'boletos'),
                       ('observacoes',),
            ],
        }),
        (None, {
            "fields":[ 'pago', ('data_pagamento', 'descontos', 'juros', 'valor_pago'),

            ],
        }),
    )
