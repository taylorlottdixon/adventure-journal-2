# Generated by Django 4.2.4 on 2023-08-12 05:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='next_game',
            field=models.DateTimeField(null=True, verbose_name='Next Game'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='npcs',
            field=models.ManyToManyField(to='main_app.npc'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='players',
            field=models.ManyToManyField(to='main_app.playercharacter'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='system',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.system'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='campaign',
            name='cover',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.photo'),
        ),
    ]