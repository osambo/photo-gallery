# Generated by Django 3.2.7 on 2021-09-06 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Image_Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='image/')),
                ('name', models.CharField(max_length=60)),
                ('Description', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.categories')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.image_location')),
            ],
        ),
    ]