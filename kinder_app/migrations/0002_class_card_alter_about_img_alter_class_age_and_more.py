# Generated by Django 4.1.7 on 2023-03-12 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinder_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='card',
            field=models.CharField(choices=[('Art', 'Art'), ('Music', 'Music'), ('reading', 'reading')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about',
            name='img',
            field=models.ImageField(upload_to='about/'),
        ),
        migrations.AlterField(
            model_name='class',
            name='age',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='class',
            name='groups',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='class',
            name='money',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='class',
            name='time',
            field=models.CharField(max_length=200),
        ),
    ]
