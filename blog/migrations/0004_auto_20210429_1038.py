# Generated by Django 3.2 on 2021-04-29 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='a_icu_bed',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='post',
            name='a_oxy_bed',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='post',
            name='doc',
            field=models.CharField(default='Dr', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='doc_add',
            field=models.CharField(default='Clinic Centre', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='doc_phone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='post',
            name='oxy',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='post',
            name='qual',
            field=models.CharField(default='M.B.B.S.', max_length=12),
        ),
        migrations.AddField(
            model_name='post',
            name='rem',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='post',
            name='t_icu_bed',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='post',
            name='t_oxy_bed',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='post',
            name='update_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
