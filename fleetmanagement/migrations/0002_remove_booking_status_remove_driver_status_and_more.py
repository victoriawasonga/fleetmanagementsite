# Generated by Django 4.1.5 on 2023-01-13 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleetmanagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='STATUS',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='STATUS',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='STATUS',
        ),
        migrations.RemoveField(
            model_name='repair',
            name='STATUS',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='STATUS',
        ),
        migrations.RemoveField(
            model_name='task',
            name='STATUS',
        ),
        migrations.RemoveField(
            model_name='tool',
            name='STATUS',
        ),
        migrations.RemoveField(
            model_name='tool_issuing',
            name='STATUS',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='STATUS',
        ),
        migrations.RemoveField(
            model_name='vehicle_owner',
            name='STATUS',
        ),
        migrations.AlterField(
            model_name='driver',
            name='Email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='driver',
            name='First_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='driver',
            name='Last_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='driver',
            name='Other_names',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='driver',
            name='Phone_number',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='driver',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='driver',
            name='national_ID',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='staff',
            name='Email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='staff',
            name='First_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='staff',
            name='Last_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='staff',
            name='Other_names',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='staff',
            name='Phone_number',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='staff',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='staff',
            name='national_ID',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicle_owner',
            name='Email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicle_owner',
            name='First_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='vehicle_owner',
            name='Last_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='vehicle_owner',
            name='Other_names',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='vehicle_owner',
            name='Phone_number',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='vehicle_owner',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicle_owner',
            name='national_ID',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('N', 'Not Active')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='driver',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('N', 'Not Active')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='journey',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('N', 'Not Active')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='repair',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('N', 'Not Active')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='staff',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('N', 'Not Active')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('N', 'Not Active')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='tool',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('N', 'Not Active')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='tool_issuing',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('N', 'Not Active')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('N', 'Not Active')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='vehicle_owner',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('N', 'Not Active')], default='A', max_length=1),
        ),
    ]
