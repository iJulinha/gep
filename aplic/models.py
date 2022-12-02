from django.db import models


class Pessoa(models.Model):

    email = models.EmailField('E-mail', blank=True, max_length=200, null=True)
    contato = models.CharField('Número de contato', blank=True, max_length=14, null=True)
    logradouro = models.CharField('Logradouro', max_length=100, null=True)
    bairro = models.CharField('Bairro', max_length=100, null=True)
    numero = models.IntegerField('Número', null=True)
    complemento = models.CharField('Complemento', blank=True, max_length=30, null=True)
    cep = models.CharField('CEP', help_text='Format: XXXXX-XXX', max_length=9, null=True)

    class Meta:
        abstract = True
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return self.nome

class Empresa(Pessoa):

    razao_social = models.CharField('Razão Social', max_length=100)
    nome_fantasia = models.CharField('Nome Fantasia', max_length=100, blank=True, null=True)
    cnpj = models.CharField('CNPJ', max_length=18)
    ie = models.CharField('Inscrição Estadual', max_length=13, null=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.razao_social


class Cargo(models.Model):

    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', max_length=500)
    carga_horaria = models.IntegerField('Carga Horária')
    salario = models.DecimalField('Faixa Salarial', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.nome


class Funcionario(Pessoa):

    nome = models.CharField('Nome', max_length=100, null=True)
    cargo = models.ForeignKey(Cargo, null=True, on_delete=models.SET_NULL)
    cpf = models.CharField('CPF', max_length=14, null=True)
    sexo = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )
    data_nascimento = models.DateField('Data de Nascimento', null=True, help_text='Por favor use o seguinte formato: <em>DD/MM/YYYY')
    opcao = models.CharField('Sexo', max_length=1, choices=sexo, blank=True, null=False)

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

        def __str__(self):
            return self.nome

class Base(models.Model):

    criacao = models.DateTimeField(auto_created=True)
    atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Ponto(Base):

    funcionario = models.ForeignKey(Funcionario, null=True, on_delete=models.SET_NULL)
    observacao = models.TextField('Observações', max_length= 300, blank=True, null=True)

    class Meta:
        verbose_name = 'Ponto'
        verbose_name_plural = 'Pontos'

        def __str__(self):
            return f'{self.funcionario} bateu o ponto {self.Ponto} as {self.criacao} e {self.atualização}'



