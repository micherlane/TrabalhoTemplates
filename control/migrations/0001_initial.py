# Generated by Django 2.1.5 on 2019-02-01 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=20)),
                ('cpf', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=100)),
            ],
        ),
    ]
