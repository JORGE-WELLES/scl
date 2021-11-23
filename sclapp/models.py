from django.db import models

# Create your models here.
class Orgao(models.Model):
    UF_CHOICE = (
        ("SP", "SP"),
        ("RJ", "RJ"),
        ("BH", "BH"),
        ("RO", "RO"),
        ("AM", "AM"),
        ("SC", "SC"),
        ("PA", "PA"),
    )

    nome = models.CharField(max_length=50, verbose_name="Empresa")
    cidade = models.CharField(max_length=25, verbose_name="Cidade")
    uf = models.CharField(max_length=2, choices=UF_CHOICE, default="SP", verbose_name="UF")

class Licitante(models.Model):
    UF_LIC_CHOICE = (
        ("SP", "sp"),
        ("RJ", "rj"),
        ("BH", "bh"),
        ("RO", "ro"),
        ("AM", "am"),
        ("SC", "sc"),
        ("PA", "pa"),
    )
    cnpj_lic = models.IntegerField(verbose_name="CNPJ")
    nome_lic = models.CharField(max_length=50, verbose_name="Licitante")
    cidade_lic = models.CharField(max_length=25, verbose_name="Cidade")
    uf_lic = models.CharField(max_length=2, choices=UF_LIC_CHOICE, default="SP", verbose_name="UF")



class Licitacao(models.Model):
    orgao = models.ForeignKey(Orgao, on_delete=models.CASCADE)
    numero_certame = models.IntegerField(verbose_name="Numero do Pregão")
    certame = models.CharField(max_length=50, verbose_name="Licitação")
    data_publicacao = models.DateField(max_length=10, verbose_name="Data da Plubicação")
    data_abertura = models.DateField(max_length=10, verbose_name="Data da Abertura")
    numero_do_item = models.IntegerField(verbose_name="Numero do Item")
    desc_item = models.TextField(verbose_name="Descrição")
    qtd_item = models.DecimalField(max_digits=5, decimal_places=4, verbose_name="Quantidade")
    unidade = models.CharField(max_length=2, verbose_name="Unidade")
    preco = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Preço")
    marca = models.CharField(max_length=20, verbose_name="Marca")
    