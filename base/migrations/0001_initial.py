# Generated by Django 4.1.3 on 2022-12-12 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('no_of_bed', models.IntegerField()),
                ('floor_no', models.IntegerField()),
                ('space_in_square_ft', models.FloatField()),
                ('price', models.FloatField()),
            ],
            options={
                'ordering': ['floor_no'],
            },
        ),
    ]