# Generated by Django 4.2.2 on 2023-06-13 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sipalaya', '0002_rename_studentinfo_contactinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=20)),
                ('Phone', models.BigIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='ContactInfo',
        ),
    ]