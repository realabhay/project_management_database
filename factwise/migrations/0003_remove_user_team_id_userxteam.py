# Generated by Django 4.2.3 on 2023-09-15 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('factwise', '0002_user_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='team_id',
        ),
        migrations.CreateModel(
            name='UserxTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factwise.team')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factwise.user')),
            ],
        ),
    ]
