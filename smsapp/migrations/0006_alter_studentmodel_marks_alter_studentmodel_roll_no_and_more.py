# Generated by Django 4.2.5 on 2023-10-29 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0005_alter_studentmodel_upload_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='marks',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='roll_no',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='upload_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
