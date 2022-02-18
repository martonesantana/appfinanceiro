# Generated by Django 3.2.12 on 2022-02-18 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0007_centrocustos_ativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='documentos',
            field=models.FileField(blank=True, help_text='Anexe o documento da convenção', null=True, upload_to='uploads/documents/%Y/%m/%d/', verbose_name='Documentos'),
        ),
    ]