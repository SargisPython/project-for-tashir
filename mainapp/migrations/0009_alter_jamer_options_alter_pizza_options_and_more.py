# Generated by Django 4.0.5 on 2022-07-30 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_alter_contact_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jamer',
            options={'ordering': ['id'], 'verbose_name': 'jamer', 'verbose_name_plural': 'ժամերը'},
        ),
        migrations.AlterModelOptions(
            name='pizza',
            options={'verbose_name': 'pizza', 'verbose_name_plural': 'Պիցցաներ'},
        ),
        migrations.AlterModelOptions(
            name='salat',
            options={'verbose_name': 'salat', 'verbose_name_plural': 'Սալատներ'},
        ),
        migrations.AlterModelOptions(
            name='sous',
            options={'verbose_name': 'sous', 'verbose_name_plural': 'Սոուսներ'},
        ),
        migrations.AlterModelOptions(
            name='xohanocy',
            options={'ordering': ['id'], 'verbose_name': 'xohanocy', 'verbose_name_plural': 'Խոհանոցներ'},
        ),
    ]
