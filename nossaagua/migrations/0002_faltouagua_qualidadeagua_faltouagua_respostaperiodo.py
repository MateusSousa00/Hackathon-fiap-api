# Generated by Django 4.2.6 on 2023-10-05 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nossaagua', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faltouagua',
            name='qualidadeagua',
            field=models.CharField(choices=[('A', 'Muito Bom'), ('B', 'Bom'), ('C', 'Regular'), ('D', 'Ruim'), ('E', 'Muito Ruim')], default='Sim', max_length=1),
        ),
        migrations.AddField(
            model_name='faltouagua',
            name='respostaperiodo',
            field=models.CharField(choices=[('1', 'Manha'), ('3', 'Tarde'), ('5', 'Noite'), ('4', 'Manha/Tarde'), ('6', 'Manha/Noite'), ('8', 'Tarde/Noite'), ('9', 'Manha/Tarde/Noite')], default='Sim', max_length=1),
        ),
    ]