from django.db import models
from apps.config.models import categoria, centrocustos, empresa, conta, fornecedor

# Create your models here.

#Cadastro de Contas a Pagar
class contasapagar(models.Model):
    empresas = models.ForeignKey(empresa, on_delete=models.CASCADE, related_name='contas_a_pagar_empresa', verbose_name='Empresa')
    fornecedor = models.ForeignKey(fornecedor, on_delete=models.CASCADE, related_name='contas_a_pagar_fornecedor', verbose_name='Fornecedor')
    descricao = models.CharField('Descrição', max_length=255)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE, related_name='contas_a_pagar_categoria', verbose_name='Categoria')
    conta = models.ForeignKey(conta, on_delete=models.CASCADE, related_name='contas_a_pagar_conta', verbose_name='Conta')
    data_competencia = models.DateField('Data competência')
    data_vencimento = models.DateField('Data vencimento')
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    centrocustos = models.ForeignKey(centrocustos, on_delete=models.CASCADE, related_name='contas_a_pagar_empresa', verbose_name='Centro de Custos', blank=True, null=True)
    observacoes = models.TextField('Observações', max_length=500, blank=True, null=True)
    documentos = models.FileField('Documentos',upload_to='uploads/documents/%Y/%m/%d/',help_text='Anexe o documento, como Nota Fiscal, Recibo', null=True, blank=True)
    boletos = models.FileField('Boletos',upload_to='uploads/documents/%Y/%m/%d/',help_text='Anexe o boleto para pagamento', null=True, blank=True)
    pago = models.BooleanField('Pago', default=False)
    data_pagamento = models.DateField('Data pagamento', null=True, blank=True )
    descontos = models.DecimalField('Descontos', max_digits=10, decimal_places=2, null=True, blank=True )
    juros = models.DecimalField('Juros', max_digits=10, decimal_places=2, null=True, blank=True ) 
    valor_pago = models.DecimalField('Valor Pago', max_digits=10, decimal_places=2, null=True, blank=True ) 
    
        
    class Meta:
        verbose_name = 'Contas a Pagar'
        verbose_name_plural = 'Contas a Pagar'

    def __str__(self):
        return self.descricao