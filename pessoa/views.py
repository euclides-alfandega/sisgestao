from django.contrib.auth.models import User

from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class PessoaApiView(APIView):

    #permission_classes = [IsAuthenticated]

    def post(self, request, format=None):

        serializer = PessoaSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):

        pessoas = Pessoa.objects.all()
        serializer = PessoaSerializer(pessoas, many=True)

        return Response(serializer.data)

class PessoaDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, id):

        try:

            pessoa = Pessoa.objects.get(id=id)
            return pessoa
        except Pessoa.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):

        pessoa = self.get_object(id)
        
        serializer = PessoaSerializer(instance=pessoa)

        return Response(serializer.data)


    def put(self, request, id):

        pessoa = self.get_object(id)
        serializer = PessoaSerializer(pessoa, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)


        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        pessoa = get_object(id)
        pessoa.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class FuncionarioAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):

        pessoa = Pessoa.objects.latest()
        post_data = request.data

        funcionario = Funcionario.objects.create(dados = pessoa, cargo = post_data['cargo'], salario = post_data['salario'], activo = post_data['activo'], administrador = post_data['administrador'] )
        
        serializers = FuncionarioSerializer(instance=funcionario)
        
        if serializers.is_valid():

            serializers.save()

        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, format=None):

        funcionario = Funcionario.objects.all()
        serializer =  FuncionarioSerializer(funcionario, many=True)

        return Response(serializer.data)

class FuncionarioDetail(APIView):

    def get_object(self, id):

        try:
            funcionario = Funcionario.objects.get(id=id)
            return funcionario
        except Funcionario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):

        funcionario = self.get_object(id)
        serializer = FuncionarioSerializer(instance=funcionario)

        return Response(serializer.data)

    def put(self, request, id):

        funcionario = self.get_object(id)
        serializer = FuncionarioSerializer(funcionario, data=request.data)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):

        funcionario = self.get_object(id)
        funcionario.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class PacienteAPIView(APIView):


    def post(self, request, format = None):
        
        data = request.data   
        datapessoa = data["dados"]

        try:
            pessoa = Pessoa.objects.create(

                nome = datapessoa["nome"],
                apelido = datapessoa["apelido"],
                sexo = datapessoa["sexo"],
                data_nascimento = datapessoa["data_nascimento"],
                bi = datapessoa["bi"],
                endereco = datapessoa["endereco"],
                email = datapessoa["email"],
                profissao = datapessoa["profissao"],    
            )

        except IntegrityError:
            
            pessoa = Pessoa.objects.get(bi=datapessoa["bi"])
            paciente = Paciente.objects.create(dados=pessoa, conjuge = data["conjuge"], telefoneConjuge = data["telefoneConjuge"])
            serializer = PacienteSerializer(instance=paciente)

            return Response(serializer.data, status=status.HTTP_201_CREATED) 
            

        paciente = Paciente.objects.create(dados=pessoa, conjuge = data['conjuge'], telefoneConjuge = data['telefoneConjuge'])
        serializer = PacienteSerializer(instance=paciente)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, format=None):

        paciente = Paciente.objects.all()
        serializer = PacienteSerializer(paciente, many=True)

        return Response(serializer.data)


class PacienteDetail(APIView):

    def get_object(self, id):

        try:

            paciente = Paciente.objects.get(id=id)
               
            return paciente
        except Paciente.DoesNotExist:

            return Response(status = status.HTTP_404_NOT_FOUND)
 
    
    def get(self, request, id):

        paciente = self.get_object(id)

        serializer = PacienteSerializer(instance=paciente)

        return Response(serializer.data, status=status)
    def put(self, request, id):
        
        paciente = self.get_object(id)

        serializer = PacienteSerializer(paciente, data=request.data)

        if serializer.is_valid():

            serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):

        paciente = self.get_object(id)

        paciente.delete()

        return Response(status=status.HTTP_200_OK)


class FornecedorViewSet(viewsets.ModelViewSet):

    serializer_class = FornecedorSerializer

    def get_queryset(self):

        fornecedores = Fornecedor.objects.all()

        return fornecedores
        
    def get_object(self, id):

        try:

            fornecedor = Fornecedor.objects.get(id=id)
            return fornecedor
        except Fornecedor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):

        serializer = FornecedorSerializer(data = request.data)

        if serializer.is_valid():

            serializer.save()
        
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):

        serializer = FornecedorSerializer(self.get_queryset(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):

        fornecedor = self.get_object(pk)

        serializer = FornecedorSerializer(instance=fornecedor)
        
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk):
        
        fornecedor = self.get_object(pk)

        serializer = FornecedorSerializer(fornecedor, data=request.data)

        if serializer.is_valid():

            serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):

        fornecedor = self.get_object(pk)

        fornecedor.delete()

        return Response(status=status.HTTP_200_OK)




