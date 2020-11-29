# Generated by Django 3.0.8 on 2020-09-07 12:41

from django.db import migrations, models
import django.db.models.deletion
import faker.providers.lorem
import faker.providers.person
import faker.providers.python


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(default=faker.providers.person.Provider.name, max_length=150),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bla', related_query_name='bla2', to='app2.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=faker.providers.python.Provider.pyint),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default=faker.providers.lorem.Provider.sentence, max_length=150),
        ),
    ]
