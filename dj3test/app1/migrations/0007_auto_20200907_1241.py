# Generated by Django 3.0.8 on 2020-09-07 12:41

from django.db import migrations, models
import faker.providers.python


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20200907_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a',
            name='bla',
            field=models.CharField(default=faker.providers.python.Provider.pystr, max_length=250),
        ),
        migrations.AlterField(
            model_name='b',
            name='x',
            field=models.IntegerField(default=faker.providers.python.Provider.pyint),
        ),
        migrations.AlterField(
            model_name='c',
            name='title',
            field=models.CharField(default=faker.providers.python.Provider.pystr, max_length=250),
        ),
        migrations.AlterField(
            model_name='d',
            name='meh',
            field=models.CharField(default=faker.providers.python.Provider.pystr, max_length=250),
        ),
    ]
