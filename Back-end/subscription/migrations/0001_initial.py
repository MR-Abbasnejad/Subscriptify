# Generated by Django 4.2.1 on 2023-06-08 14:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import subscription.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('is_adult', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('discription', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('like', models.PositiveBigIntegerField()),
                ('view', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('discription', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('wallet_address', models.CharField(max_length=255, verbose_name='Wallet Address')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last Login')),
                ('like', models.PositiveBigIntegerField()),
                ('view', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('discription', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserTagMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscription.tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscription.user')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='tag',
            field=models.ManyToManyField(through='subscription.UserTagMap', to='subscription.tag'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_status',
            field=models.OneToOneField(on_delete=models.SET(0), to='subscription.userstatus'),
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_format', models.CharField(max_length=7, verbose_name='File Format')),
                ('is_video', models.BooleanField()),
                ('is_document', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Upload Date')),
                ('description', models.TextField(blank=True)),
                ('file', models.FileField(upload_to=subscription.models.Repository.file_path_and_extention)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repositories', to='subscription.content')),
            ],
        ),
        migrations.CreateModel(
            name='ContentTagMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscription.content')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscription.tag')),
            ],
        ),
        migrations.CreateModel(
            name='ContentCategoryMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscription.category')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscription.content')),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='category',
            field=models.ManyToManyField(through='subscription.ContentCategoryMap', to='subscription.category'),
        ),
        migrations.AddField(
            model_name='content',
            name='tag',
            field=models.ManyToManyField(through='subscription.ContentTagMap', to='subscription.tag'),
        ),
        migrations.AddField(
            model_name='content',
            name='user',
            field=models.ForeignKey(on_delete=models.SET(0), related_name='contents', to='subscription.user'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('like', models.PositiveBigIntegerField()),
                ('comment_status', models.OneToOneField(on_delete=models.SET(0), related_name='comments', to='subscription.commentstatus')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='subscription.content')),
                ('user', models.ForeignKey(on_delete=models.SET(0), related_name='comments', to='subscription.user')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('email', 'wallet_address')},
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Subscribe Date')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to='subscription.user')),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='subscription.user')),
            ],
            options={
                'unique_together': {('subscriber', 'subscription')},
            },
        ),
    ]
