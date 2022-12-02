from rest_framework import serializers

from .models import Funcionario, Ponto


class FuncionarioSerializer(serializers.ModelSerializer):

    extra_kargs = {
        'cpf': {'write_only': True},
        'email': {'write_only': True}
    }

    class Meta:
        model = Funcionario.models
        fields = (
            'id',
            'nome',
            'cargo',
            'cpf',
            'opcao',
            'data_nascimento',
            'email',
            'contato',
            'logradouro',
            'bairro',
            'numero',
            'complemento',
            'cep'
        ),


class PontoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ponto.models
        fields = (
            'id',
            'criacao',
            'funcionario',
            'observação'

        )

