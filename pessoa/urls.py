from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from .views import FornecedorViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register('fornecedor', FornecedorViewSet, basename='fornecedor')


urlpatterns = [

    path('dados_pessoa/', PessoaApiView.as_view(), name='pessoa'),
    path('funcionario/', FuncionarioAPIView.as_view(), name='funcionario'),
    path('dados_pessoa/<int:id>/', PessoaDetail.as_view(), name='pessoa_detail'),
    path('paciente/', PacienteAPIView.as_view(), name='paciente'),
    path('paciente_detail/<int:id>/', PacienteDetail.as_view(), name='pacientedetalhes'),
    path('', include(router.urls)),
    path('gettoken/', obtain_auth_token)

]