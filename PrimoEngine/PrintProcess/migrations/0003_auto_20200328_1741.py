# Generated by Django 3.0.4 on 2020-03-28 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrintProcess', '0002_delete_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrintJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('stlText', models.TextField(blank=True)),
                ('plyText', models.TextField(blank=True)),
                ('usdzText', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
