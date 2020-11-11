# Generated by Django 2.1.13 on 2020-11-11 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanalberto', '0008_activity_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='has_registration',
            field=models.BooleanField(default=True, verbose_name='necesaria inscripción'),
        ),
        migrations.AddField(
            model_name='activityregistration',
            name='comments',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='comentarios'),
        ),
        migrations.AddField(
            model_name='activityregistration',
            name='payment_id',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='ID de pago'),
        ),
    ]
