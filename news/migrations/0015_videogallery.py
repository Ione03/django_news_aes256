# Generated by Django 4.0.6 on 2023-01-11 05:44

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0014_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoGallery',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('view_count', models.PositiveIntegerField(default=0, editable=False)),
                ('title', models.CharField(max_length=500)),
                ('embed', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('embed_video', models.URLField(blank=True, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=20)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
