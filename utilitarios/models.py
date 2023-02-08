from django.db import models

# Create your models here.

choices_status = (
    ('a', 'Ativo'),
    ('i', 'inativo'),
    ('c', 'Cancelado'),
    ('b', 'Bloqueado'),
)
choices_sexo = (
    ('m', 'Masculino'),
    ('f', 'Femenino'),
    ('n', 'Nenhuma das opções')
)
choices_tipoPess = (
    ('s', 'Servirdor'),
    ('t', 'terceirizado'),
    ('b', 'Bolsista'),
    ('v', 'Visitante'),
)

class Pessoa(models.Model):

    nome = models.CharField(max_length=50, verbose_name="Nome", blank=False, null=False)
    fonePess = models.CharField(max_length=15, verbose_name="Telefone Pessoal", blank=False, null=False)
    status = models.CharField(max_length=1, choices=choices_status, null=False, blank=False)
    tipoPessoa = models.CharField(max_length=1, choices=choices_sexo, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=choices_sexo, null=False, blank=False)
    cpf = models.CharField(max_length=14, verbose_name="CPF", blank=False, null=False)
    email = models.EmailField(blank=False, null=False)

class Bloco(models.Model):
    bloco = models.CharField(max_length=50, verbose_name="Bloco", blank=False, null=False)

class Setor(models.Model):
    bloco = models.ForeignKey(Bloco, verbose_name="Bloco", blank=False, null=False, on_delete=models.CASCADE)
    andar = models.CharField(max_length=50, verbose_name="Bloco", blank=False, null=False)

class Area(models.Model):
    area = models.CharField(max_length=50, verbose_name="Fone/Ramal", blank=False, null=False)

class ListaFone(models.Model):
    pessoaLista = models.ForeignKey(Pessoa, verbose_name="Colaborador", blank=False, null=False, on_delete=models.CASCADE)
    fone = models.CharField(max_length=15, verbose_name="Fone/Ramal", blank=False, null=False)
    area = models.ForeignKey(Area, verbose_name="Área", blank=True,null=True, on_delete=models.CASCADE)
    bloco = models.ForeignKey(Bloco, verbose_name="Bloco", blank=False, null=False, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, verbose_name="Setor", blank=False, null=False, on_delete=models.CASCADE)

