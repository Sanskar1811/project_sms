# Generated by Django 4.2.5 on 2023-10-28 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentmodel',
            name='crdt',
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='marks',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='name',
            field=models.CharField(default='YourDefaultValueHere', max_length=20),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='rno',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]