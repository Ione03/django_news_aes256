# Generated by Django 4.0.6 on 2022-08-03 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_photo_content_type_alter_photo_object_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='count',
            field=models.PositiveIntegerField(blank=True, default=0, editable=False, null=True),
        ),
    ]