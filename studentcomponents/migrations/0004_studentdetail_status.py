# Generated by Django 2.2.2 on 2019-07-18 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentcomponents', '0003_auto_20190713_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetail',
            name='status',
            field=models.CharField(choices=[('CURRENT', 'CURRENT'), ('LEFT', 'LEFT')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
