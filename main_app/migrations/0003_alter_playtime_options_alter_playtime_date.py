# Generated by Django 4.0.4 on 2022-05-20 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_digimon_name_alter_digimon_type_playtime'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playtime',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='playtime',
            name='date',
            field=models.DateField(verbose_name='Petting Date'),
        ),
    ]