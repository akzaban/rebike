# Generated by Django 3.1.5 on 2021-02-22 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_report_imgaereport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentdetails',
            name='bikeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.bike'),
        ),
    ]
