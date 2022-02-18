from django.db import models

# Create your models here.

class empresa(models.Model):
    nome = models.CharField('Nome da Empresa', max_length=100)
    razaosocial = models.CharField('Razão Social', max_length=200)
    cnpj = models.CharField('CNPJ', max_length=18, unique=True)
    codigo_erp = models.CharField('Código ERP', max_length=10, blank=True, null=True)
    data_criacao = models.DateField('Data da Criação', blank=True, null=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nome


class categoria(models.Model):
    descricao = models.CharField('Categoria', max_length=100)
    regra_contabilizacao = models.CharField('Regra de Contabilização', max_length=200, blank=True, null=True)
    conta_contabil = models.CharField('Conta Contábil', max_length=18, blank=True, null=True)
    dre = models.CharField('DRE', max_length=155, blank=True, null=True)
        
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.descricao


class planocontas(models.Model):

    natureza_choices = [
        ('C', 'Credora'),
        ('D', 'Devedora'),
    ]
    
    empresas = models.ForeignKey(empresa, on_delete=models.CASCADE, related_name='empresas_plano_contas', verbose_name='Empresa')
    codigo = models.CharField('Código',max_length=14, help_text='Informe o código do plano de contas')
    descricao = models.CharField('Descrição',max_length=155, help_text='Informe a descrição do plano de contas')
    reduzido = models.CharField('Reduzido',max_length=3, blank=True, null=True)
    analitica = models.BooleanField('Analítica', default=False)
    patrimonial = models.BooleanField('Patrimonial', default=False)
    natureza = models.CharField('Natureza', max_length=1, choices=natureza_choices)
    seq = models.PositiveIntegerField('Seq', blank=True, null=True)
    
    
    class Meta:
        verbose_name = 'Plano de Contas'
        verbose_name_plural = 'Plano de Contas'

    def __str__(self):
        return self.descricao