# Generated by Django 5.0.2 on 2024-02-24 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_image',
            field=models.ImageField(blank=True, null=True, upload_to='authors/'),
        ),
    ]
