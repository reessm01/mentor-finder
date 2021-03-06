# Generated by Django 2.2.6 on 2019-10-02 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Personality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=4, unique=True)),
                ('detail', models.TextField()),
                ('related', models.ManyToManyField(related_name='_personality_related_+', to='mentor_finder.Personality')),
            ],
        ),
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('headline', models.TextField(max_length=280)),
                ('photo_link', models.CharField(max_length=255)),
                ('is_mentor', models.BooleanField(default=False)),
                ('industry', models.CharField(max_length=100)),
                ('goals', models.ManyToManyField(to='mentor_finder.Goal', verbose_name='Goals')),
                ('messages', models.ManyToManyField(to='mentor_finder.Message')),
                ('personality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentor_finder.Personality')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
