# Generated by Django 2.0.6 on 2018-06-21 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThemeBlog',
            fields=[
                ('blog_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='weblog.Blog')),
                ('theme', models.CharField(max_length=200)),
            ],
            bases=('weblog.blog',),
        ),
    ]
