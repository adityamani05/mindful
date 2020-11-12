# Generated by Django 2.2 on 2020-09-14 13:48

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import mindful_api.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=16, unique=True)),
                ('password', models.CharField(max_length=252)),
                ('name', models.CharField(max_length=128, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('bio', models.CharField(max_length=256, null=True)),
                ('profile_picture', models.ImageField(null=True, upload_to='user_images/')),
                ('allow_posting', models.BooleanField(default=True)),
                ('last_active', models.DateTimeField(auto_now_add=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(max_length=256, null=True)),
                ('image', models.ImageField(null=True, upload_to='post_images/')),
                ('has_media', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tags', django.contrib.postgres.fields.jsonb.JSONField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReportPost',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('remarks', models.TextField(max_length=256)),
                ('report_time', models.DateTimeField(auto_now_add=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mindful_api.Post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('like_id', models.AutoField(primary_key=True, serialize=False)),
                ('like_time', models.DateTimeField(auto_now_add=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mindful_api.Post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Followings',
            fields=[
                ('following_id', models.AutoField(primary_key=True, serialize=False)),
                ('follow_time', models.DateTimeField(auto_now_add=True)),
                ('followed_by_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('follower_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('bookmark_id', models.AutoField(primary_key=True, serialize=False)),
                ('bookmark_time', models.DateTimeField(auto_now_add=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mindful_api.Post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
