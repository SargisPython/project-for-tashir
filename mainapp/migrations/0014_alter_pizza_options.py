# Generated by Django 4.0.5 on 2022-07-30 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_alter_pizza_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pizza',
            options={'ordering': ['id'], 'verbose_name': 'pizza', 'verbose_name_plural': 'Պիցցաներ'},
        ),
    ]