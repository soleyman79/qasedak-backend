# Generated by Django 4.2.3 on 2023-08-06 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consumption', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('summary', models.CharField(max_length=64)),
                ('text', models.TextField(max_length=512)),
                ('chanel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumption.chanel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='video',
            name='chanel',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
