# Generated by Django 3.1.3 on 2020-11-06 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.ImageField(default=0, upload_to='')),
                ('description', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(upload_to='uploads/product/')),
            ],
        ),
    ]
