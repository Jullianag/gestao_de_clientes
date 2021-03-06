# Generated by Django 4.0.4 on 2022-04-21 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30)),
                ('idade', models.IntegerField()),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('biografia', models.TextField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='clients_photos')),
            ],
        ),
    ]
