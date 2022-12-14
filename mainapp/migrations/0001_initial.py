# Generated by Django 4.0.5 on 2022-06-24 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tesaky', models.CharField(blank=True, max_length=100, null=True)),
                ('arjeqy', models.IntegerField(blank=True, null=True)),
                ('baxadrutyuny', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'pizza',
                'verbose_name_plural': 'pizzaners',
            },
        ),
        migrations.CreateModel(
            name='Salat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tesaky', models.CharField(blank=True, max_length=100, null=True)),
                ('arjeqy', models.IntegerField(blank=True, null=True)),
                ('baxadrutyuny', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'salat',
                'verbose_name_plural': 'salatner',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=255)),
                ('icon', models.ImageField(upload_to='icons')),
            ],
        ),
        migrations.CreateModel(
            name='Sous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tesaky', models.CharField(blank=True, max_length=100, null=True)),
                ('arjeqy', models.IntegerField(blank=True, null=True)),
                ('baxadrutyuny', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'sous',
                'verbose_name_plural': 'sousner',
            },
        ),
        migrations.CreateModel(
            name='Tashir_pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image')),
                ('title', models.CharField(max_length=100, null=True)),
                ('opening', models.IntegerField(null=True)),
                ('closing', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Xohanocy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'xohanocy',
                'verbose_name_plural': 'xohanocners',
            },
        ),
    ]
