# Generated by Django 3.0.4 on 2020-04-05 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('econex', '0002_auto_20200405_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seria',
            name='catogory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='econex.Category'),
        ),
    ]
