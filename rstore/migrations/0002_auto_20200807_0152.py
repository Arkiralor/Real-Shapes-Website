# Generated by Django 3.0.8 on 2020-08-06 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cust',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='serv',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='servcost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='servqnt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='servtotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='serv',
            name='servcost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trans',
            name='cust',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trans',
            name='serv',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trans',
            name='servcost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trans',
            name='servqnt',
            field=models.IntegerField(default=0),
        ),
    ]