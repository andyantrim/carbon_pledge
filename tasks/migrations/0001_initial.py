# Generated by Django 2.1.7 on 2019-05-01 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('decription', models.CharField(blank=True, max_length=5000, null=True)),
                ('image_link', models.CharField(default='http://www.worldwideprotective.com/Public/images/product/recycle.jpg', max_length=1024)),
            ],
        ),
    ]
