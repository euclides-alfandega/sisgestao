from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pessoa(models.Model):


    SEXO = (
        ('Masculino', 'M'),
        ('Feminino', 'F'),
    )

    nome = models.CharField(max_length=200, null=True, blank=True)
    apelido = models.CharField(max_length=200, null=True, blank=True)
    sexo = models.CharField(max_length=9, null=True, choices=SEXO)
    data_nascimento = models.DateField(null=True, blank=True) 
    bi = models.CharField(max_length=13, null=True, unique=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    bairro = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=250, null=True, blank=True)
    profissao = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        get_latest_by = ['id']


    def _str_(self):
        return self.apelido

class Paciente(models.Model):
    dados = models.OneToOneField(Pessoa, on_delete=models.CASCADE, verbose_name="Dados Paciente", unique=True, null=False)
    conjuge = models.CharField(max_length=250, null=True, blank=True)
    telefoneConjuge = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.dados.nome

class Funcionario(models.Model):

    dados = models.OneToOneField(Pessoa, on_delete=models.CASCADE, verbose_name="Dados Funcionario", unique=True, related_name='dados_funcionario', null=False)
    cargo = models.CharField(max_length=200, null=True, blank=True)
    salario = models.FloatField(null=True, blank=True)
    activo = models.BooleanField(verbose_name="E activo", null=True)
    administrador = models.BooleanField(verbose_name="E admnistrador", null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario', null=True)
   
    def __str__(self):
        return self.dados.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    CNPJ = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome