# Generated by Django 4.2.1 on 2023-07-07 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('option', models.CharField(max_length=100)),
                ('files', models.FileField(upload_to='MyNotes')),
                ('disc', models.TextField()),
            ],
        ),
    ]
