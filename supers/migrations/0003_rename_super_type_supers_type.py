# Generated by Django 4.0.4 on 2022-05-01 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0002_alter_supers_super_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supers',
            old_name='super_type',
            new_name='type',
        ),
    ]