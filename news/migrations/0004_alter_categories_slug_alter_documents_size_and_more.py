# Generated by Django 4.0.6 on 2022-07-31 23:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_remove_documents_admin_remove_downloadlink_expired_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(blank=True, default='', editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='documents',
            name='size',
            field=models.BigIntegerField(blank=True, default=0, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='admin',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, default='', editable=False, max_length=255, unique=True),
        ),
    ]