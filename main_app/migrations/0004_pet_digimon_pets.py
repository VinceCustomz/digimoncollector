# Generated by Django 4.0.4 on 2022-05-20 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_playtime_options_alter_playtime_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='digimon',
            name='pets',
            field=models.ManyToManyField(to='main_app.pet'),
        ),
    ]