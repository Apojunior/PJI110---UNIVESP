from django.db import models

class Cliente(models.Model):
    TIPO_DOCUMENTO_CHOICES = (
        ('CPF', 'CPF'),
        ('CNPJ', 'CNPJ'),
    )
    tipo_documento = models.CharField(max_length=4, choices=TIPO_DOCUMENTO_CHOICES)
    # outros campos do modelo Cliente
    nome = models.CharField(max_length=255)
    documento = models.CharField(max_length=18, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

