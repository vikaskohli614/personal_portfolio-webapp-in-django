# Generated by Django 4.0.1 on 2022-02-25 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_fname_contact_name_remove_contact_lname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]