from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Pessoa)
admin.site.register(Funcionario)
admin.site.register(Paciente)
admin.site.register(Fornecedor)