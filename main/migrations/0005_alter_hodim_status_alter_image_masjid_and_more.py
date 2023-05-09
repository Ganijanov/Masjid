# Generated by Django 4.2 on 2023-05-02 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_shahartuman_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hodim',
            name='status',
            field=models.IntegerField(choices=[(2, 'Imom hatib'), (3, 'Qori'), (4, 'Muazzin'), (1, 'Imom')]),
        ),
        migrations.AlterField(
            model_name='image',
            name='masjid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.masjid'),
        ),
        migrations.AlterField(
            model_name='shahartuman',
            name='status',
            field=models.CharField(choices=[('Tuman', 'Tuman'), ('Shaxar', 'Shaxar')], max_length=255),
        ),
    ]