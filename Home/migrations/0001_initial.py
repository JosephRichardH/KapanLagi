# Generated by Django 2.1.7 on 2019-02-14 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lagu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('artis', models.CharField(max_length=255)),
                ('teks', models.TextField(max_length=5000)),
            ],
        ),
    ]