# Generated by Django 2.2.17 on 2021-01-15 16:01

import app1.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Country')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Region')),
            ],
            bases=(app1.models.StrNameMixin, models.Model),
        ),
    ]
