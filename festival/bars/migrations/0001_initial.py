# Generated by Django 2.2.1 on 2019-05-08 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='bars/')),
                ('name', models.CharField(max_length=80)),
                ('text', models.TextField(max_length=200)),
                ('location_url', models.TextField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BarLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='bars.Bar')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]