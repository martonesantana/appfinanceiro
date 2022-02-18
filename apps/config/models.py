from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


# Cadastro da Empresa
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


# Cadastro do Plano de Contas
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

# Cadastro da Categoria
class categoria(models.Model):
    empresas = models.ForeignKey(empresa, on_delete=models.CASCADE, related_name='categorias_empresa', verbose_name='Empresa')
    descricao = models.CharField('Categoria', max_length=100)
    regra_contabilizacao = models.CharField('Regra de Contabilização', max_length=200, blank=True, null=True)
    conta_contabil = models.ForeignKey(planocontas, on_delete=models.CASCADE, related_name='conta_contabil_categoria', verbose_name='Conta Contábil' , blank=True, null=True)
    dre = models.CharField('DRE', max_length=155, blank=True, null=True)
        
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.descricao

# Cadastro do Fornecedor
class fornecedor(models.Model):

    tipo = [
        ('Jurídica', 'Jurídica'),
        ('Física', 'Física'),
    ]

    tipo_ie = [
        ('Não Contribuinte', 'Não Contribuinte'),
        ('Contribuinte', 'Contribuinte'),
        ('Contribuinte isento', 'Contribuinte isento'),
    ]

    tipo = models.CharField('Tipo de  pessoa', max_length=50,choices=tipo)
    razaosocial = models.CharField('Razão Social', max_length=250)
    nome_fantasia = models.CharField('Nome Fantasia', max_length=250)
    cnpj = models.CharField('CNPJ', max_length=18, unique=True)
    email = models.EmailField('E-mail Principal', blank=True, null=True)
    telefone = PhoneNumberField('Telefone', blank=True, null=True)
    data_abertura = models.DateField('Abertura da empresa', blank=True, null=True)
    simples = models.BooleanField('Optante pelo simples?', default=False)
    indicador_ie = models.CharField('Indicador de Inscrição Estadual', max_length = 100, choices=tipo_ie, blank=True, null=True)
    inscricao_estadual = models.CharField('Inscrição Estadual', max_length=50, blank=True, null=True)
    inscricao_municipal = models.CharField('Inscrição Municipal', max_length=50, blank=True, null=True)
    cep = models.CharField('CEP', max_length=50,blank=True, null=True)
    endereco = models.CharField('Endereço', max_length=150, blank=True, null=True)
    numero = models.CharField('Número', max_length=30, blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=150, blank=True, null=True)
    estado = models.CharField('Estado', max_length=50,blank=True, null=True)
    municipio = models.CharField('Municípo', max_length=150, blank=True, null=True)
    complemento = models.CharField('Complemento', max_length=150, blank=True, null=True)
    pessoa_contato = models.CharField('Pessoa de Contato', max_length=150, blank=True, null=True)
    pessoa_contato_email = models.EmailField('E-mail', blank=True, null=True)
    pessoa_contato_telefone = PhoneNumberField('Telefone', blank=True, null=True)
    pessoa_contato_cargo = models.CharField('Cargo', max_length=150, blank=True, null=True)
    observacoes = models.TextField('Observações', max_length=500, blank=True, null=True)


    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.nome_fantasia


# Cadastro da Conta
class conta(models.Model):
    empresas = models.ForeignKey(empresa, on_delete=models.CASCADE, related_name='contas_empresa', verbose_name='Empresa')
    banco = models.CharField('Banco', max_length=50)
    descricao = models.CharField('Descrição', max_length=150)
    agencia = models.CharField('Agência', max_length=50)
    conta = models.CharField('Conta', max_length=50)
    ativa = models.BooleanField('Ativa?' , default=True)
        
    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'

    def __str__(self):
        return self.descricao

# Cadastro da Centro de Custos
class centrocustos(models.Model):
    empresas = models.ForeignKey(empresa, on_delete=models.CASCADE, related_name='centros_custos_empresa', verbose_name='Empresa')
    codigo = models.CharField('Código', max_length=50)
    descricao = models.CharField('Descrição', max_length=150)
    ativo = models.BooleanField('Ativo?' , default=True)
    
        
    class Meta:
        verbose_name = 'Centro de Custo'
        verbose_name_plural = 'Centros de Custos'

    def __str__(self):
        return self.descricao