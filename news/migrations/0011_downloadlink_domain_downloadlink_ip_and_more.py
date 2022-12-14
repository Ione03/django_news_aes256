# Generated by Django 4.0.6 on 2022-08-05 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_alter_documents_file_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='downloadlink',
            name='domain',
            field=models.CharField(default='', editable=False, max_length=255),
        ),
        migrations.AddField(
            model_name='downloadlink',
            name='ip',
            field=models.CharField(db_index=True, default=None, editable=False, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='downloadlink',
            name='session',
            field=models.CharField(db_index=True, default=None, editable=False, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='downloadlink',
            name='user_agent',
            field=models.CharField(default=None, editable=False, max_length=255),
            preserve_default=False,
        ),
    ]
