# Generated by Django 4.2.2 on 2023-06-18 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sipalaya', '0003_employeeinfo_delete_contactinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='YourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column1', models.CharField(max_length=100)),
                ('column2', models.IntegerField()),
            ],
        ),
    ]
