# Generated by Django 4.2.6 on 2023-10-14 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Std',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('middlename', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('father', models.CharField(max_length=50)),
                ('mother', models.CharField(max_length=50)),
                ('d', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('mobile', models.BigIntegerField()),
                ('amobile', models.BigIntegerField()),
                ('add', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
