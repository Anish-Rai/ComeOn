# Generated by Django 3.0.1 on 2019-12-30 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_testimonials_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_desc', models.TextField()),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]
