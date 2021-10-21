# Generated by Django 3.1.7 on 2021-05-27 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20210526_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trek_title', models.CharField(max_length=100)),
                ('trel_drive_link', models.CharField(max_length=250)),
                ('trek_days', models.IntegerField(default=0)),
                ('trek_description', models.TextField(blank=True)),
                ('trek_price', models.IntegerField(default=0)),
                ('trek_image', models.ImageField(default='', upload_to='tnt/images')),
            ],
        ),
    ]
