# Generated by Django 4.2.5 on 2023-09-27 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.club'),
        ),
    ]