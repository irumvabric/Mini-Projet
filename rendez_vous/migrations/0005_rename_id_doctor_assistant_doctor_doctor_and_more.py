# Generated by Django 5.1 on 2025-02-04 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rendez_vous', '0004_assistant_doctor_created_availability_created_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assistant_doctor',
            old_name='id_doctor',
            new_name='doctor',
        ),
        migrations.RenameField(
            model_name='rendez_vous',
            old_name='id_doctor',
            new_name='doctor',
        ),
        migrations.RenameField(
            model_name='rendez_vous',
            old_name='id_patient',
            new_name='patient',
        ),
    ]
