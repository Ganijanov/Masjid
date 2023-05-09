# Generated by Django 4.2 on 2023-04-29 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hodim',
            name='status',
            field=models.IntegerField(choices=[(2, 'Imom hatib'), (4, 'Muazzin'), (3, 'Qori'), (1, 'Imom')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shahartuman',
            name='status',
            field=models.CharField(max_length=255, verbose_name={('t', 'Shaxar'), ('sh', 'Shaxar')}),
        ),
    ]
