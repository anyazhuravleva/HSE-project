# Generated by Django 2.1.7 on 2019-03-17 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190317_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='requesttable',
            name='antenna',
            field=models.CharField(default='01', max_length=80),
            preserve_default=False,
        ),
    ]