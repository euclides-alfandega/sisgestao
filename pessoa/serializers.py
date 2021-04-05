from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class FuncionarioSerializer(serializers.ModelSerializer):
    
    dados_funcionario = serializers.StringRelatedField(read_only=True)

    class Meta:

       
        model = Funcionario

        fields = ['dados','cargo', 'salario', 'activo', 'administrador', 'dados_funcionario']

class PessoaSerializer(serializers.ModelSerializer):
    
    

    class Meta:
        
        funcionario = FuncionarioSerializer(read_only=True)

        model = Pessoa

        fields = ['nome', 'apelido', 'sexo', 'data_nascimento', 'bi', 'endereco', 'bairro', 'email', 'profissao', 'dados_funcionario']


class PacienteSerializer(serializers.ModelSerializer):

    Dados_Paciente = PessoaSerializer(read_only=True)

    class Meta:

        model = Paciente

        fields = ['dados', 'conjuge', 'telefoneConjuge', 'Dados_Paciente']


class FornecedorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Fornecedor

        fields = '__all__'
