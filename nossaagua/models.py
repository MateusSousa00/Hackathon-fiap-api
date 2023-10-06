from django.db import models

class Morador(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=30)
    celular = models.CharField(max_length=11)
    rua = models.CharField(max_length=30)
    numero_casa = models.CharField(max_length=9)
    bairro = models.CharField(max_length=40)
    cep = models.CharField(max_length=8)
    
    def __str__(self):
        return self.nome

class FaltouAgua(models.Model):
    RESPOSTAFALTA = (
        ("Sim", "Sim"),
        ("Não", "Não")
    )
    PERIODO = (
        ("1", "Manha"),
        ("3", "Tarde"),
        ("5","Noite"),
        ("4", "Manha/Tarde"),
        ("6", "Manha/Noite"),
        ("8", "Tarde/Noite"),
        ("9", "Manha/Tarde/Noite")
    )
    QUALIDADE = (
        ("A", "Muito Bom"),
        ("B", "Bom"),
        ("C","Regular"),
        ("D", "Ruim"),
        ("E", "Muito Ruim")
    )
    respostafalta = models.CharField(max_length=3, choices=RESPOSTAFALTA, blank=False, null=False, default="Sim")
    respostaperiodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default="Sim")
    qualidadeagua = models.CharField(max_length=1, choices=QUALIDADE, blank=False, null=False, default="Sim")
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE)
    def __str__(self):
        return self.qualidadeagua
        

