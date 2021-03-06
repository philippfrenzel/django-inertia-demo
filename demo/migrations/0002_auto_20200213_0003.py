# Generated by Django 3.0.3 on 2020-02-13 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('first_name', 'last_name')},
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': ('name',)},
        ),
        migrations.RemoveField(
            model_name='contact',
            name='state',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='state',
        ),
        migrations.AddField(
            model_name='contact',
            name='country',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contact',
            name='postal_code',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='region',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='country',
            field=models.CharField(default='MX', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organization',
            name='postal_code',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='region',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='organization',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='organization',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
