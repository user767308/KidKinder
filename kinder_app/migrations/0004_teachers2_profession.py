# Generated by Django 4.1.7 on 2023-03-13 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinder_app', '0003_alter_blog_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers2',
            name='profession',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
