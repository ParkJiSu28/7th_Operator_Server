# Generated by Django 2.2.3 on 2019-08-02 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='substitute',
            name='Requestor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='substitute_req', to='group.Participate'),
        ),
        migrations.AlterField(
            model_name='substitute',
            name='Responsor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='substitute_res', to='group.Participate'),
        ),
    ]