# Generated by Django 4.2 on 2023-06-22 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endereco',
            name='cliente',
        ),
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.endereco'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
    ]