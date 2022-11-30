from django.contrib import admin

from .models import Empresa, Cargo, Funcionario, Ponto


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('razao_social', 'nome_fantasia', 'cnpj', 'contato', 'email')

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'carga_horaria', 'salario')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'cpf', 'data_nascimento', 'opcao', 'email', 'contato', 'logradouro', 'bairro', 'numero', 'complemento', 'cep')

@admin.register(Ponto)
class PontoAdmin(admin.ModelAdmin):
    list_display = ('funcionario', 'criacao', 'atualizacao', 'observacao')