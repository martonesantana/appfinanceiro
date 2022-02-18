from django.contrib import admin

from baton.admin import DropdownFilter, ChoicesDropdownFilter
from apps.config.models import categoria, centrocustos, conta, empresa, fornecedor, planocontas 
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


@admin.register(planocontas)
class PlanoContasAdmin(admin.ModelAdmin):
    list_display = ('empresas', 'codigo', 'descricao', 'reduzido', 'analitica', 'patrimonial', 'natureza' )
    search_fields = ['empresas__nome', 'codigo', 'descricao']
    list_filter = (
                    ('codigo', DropdownFilter),
                    ('descricao', DropdownFilter),
                )
    list_editable = ('codigo','descricao', 'reduzido', 'analitica', 'patrimonial', 'natureza')
    list_per_page = 5

@admin.register(categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('empresas','descricao',  'conta_contabil', 'dre','regra_contabilizacao')
    search_fields = ('empresas__nome','descricao', 'conta_contabil__descricao')
    list_filter = (
                    ('empresas__nome', DropdownFilter),
                    ('descricao', DropdownFilter),
                    ('conta_contabil__descricao', DropdownFilter),
                )
    list_editable = ('descricao','regra_contabilizacao','conta_contabil', 'dre')
    list_per_page = 5

@admin.register(fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'nome_fantasia', 'razaosocial','email')
    search_fields = ('cnpj','nome_fantasia', 'razaosocial', 'email')
    list_filter = (
                    ('nome_fantasia', DropdownFilter),
                    ('razaosocial', DropdownFilter),
                )
    list_editable = ('nome_fantasia','razaosocial','email')
    list_per_page = 5

@admin.register(conta)
class ContaAdmin(admin.ModelAdmin):
    list_display = ('empresas', 'banco', 'descricao','agencia', 'conta', 'ativa')
    search_fields = ('empresas__nome','banco', 'descricao', 'conta')
    list_filter = (
                    ('empresas__nome', DropdownFilter),
                    ('banco', DropdownFilter),
                    ('agencia', DropdownFilter),
                    ('conta', DropdownFilter),
                )
    list_editable = ('banco', 'descricao','agencia', 'conta', 'ativa')
    list_per_page = 5

@admin.register(centrocustos)
class CentrosCustosAdmin(admin.ModelAdmin):
    list_display = ('empresas', 'codigo', 'descricao', 'ativo')
    search_fields = ('empresas__nome','codigo', 'descricao', 'ativo')
    list_filter = (
                    ('empresas__nome', DropdownFilter),
                    ('codigo', DropdownFilter),
                    ('descricao', DropdownFilter),
                    ('ativo', DropdownFilter),
                    
                )
    list_editable = ('codigo', 'descricao', 'ativo')
    list_per_page = 5