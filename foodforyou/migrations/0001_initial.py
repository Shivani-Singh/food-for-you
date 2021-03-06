# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-07 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import foodforyou.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default='1')),
                ('amount', models.IntegerField(default='00')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('item_id', models.UUIDField(default=foodforyou.models.generateUUID, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='JoinTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodforyou.Items')),
            ],
        ),
        migrations.CreateModel(
            name='ManageOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('PL', 'Placed'), ('ON', 'Ongoing'), ('DP', 'Dispatched'), ('DL', 'Delivered')], default='Placed', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('menu_id', models.UUIDField(default=foodforyou.models.generateUUID, editable=False, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.UUIDField(default=foodforyou.models.generateUUID, editable=False, primary_key=True, serialize=False)),
                ('order_amount', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('restro_id', models.UUIDField(default=foodforyou.models.generateUUID, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('phone_num', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('cuisine', models.CharField(choices=[('AFG', 'Afghani'), ('ARB', 'Arabian'), ('ASM', 'Assamese'), ('AWD', 'Awadhi'), ('BNG', 'Bengali'), ('CHN', 'Chinese'), ('CNT', 'Continental'), ('DSR', 'Dessserts'), ('FRN', 'French'), ('GUJ', 'Gujarati'), ('HYD', 'Hyderabadi'), ('ITL', 'Italian'), ('JPN', 'Japanese'), ('KSH', 'Kashmiri'), ('KOR', 'Korean'), ('LEB', 'Lebanese'), ('MEX', 'Mexican'), ('NRI', 'North Indian'), ('RAJ', 'Rajasthani'), ('SIN', 'Sindhi'), ('SOI', 'South Indian'), ('THI', 'Thai')], default='SELECT', max_length=50)),
                ('time_start', models.CharField(choices=[('000', '00:00'), ('001', '01:00'), ('002', '02:00'), ('003', '03:00'), ('004', '04:00'), ('005', '05:00'), ('006', '06:00'), ('007', '07:00'), ('008', '08:00'), ('009', '09:00'), ('010', '10:00'), ('011', '11:00'), ('012', '12:00'), ('013', '13:00'), ('014', '14:00'), ('015', '15:00'), ('016', '16:00'), ('017', '17:00'), ('018', '18:00'), ('019', '19:00'), ('020', '20:00'), ('021', '21:00'), ('022', '22:00'), ('023', '23:00')], default='SELECT', max_length=50)),
                ('time_end', models.CharField(choices=[('000', '00:00'), ('001', '01:00'), ('002', '02:00'), ('003', '03:00'), ('004', '04:00'), ('005', '05:00'), ('006', '06:00'), ('007', '07:00'), ('008', '08:00'), ('009', '09:00'), ('010', '10:00'), ('011', '11:00'), ('012', '12:00'), ('013', '13:00'), ('014', '14:00'), ('015', '15:00'), ('016', '16:00'), ('017', '17:00'), ('018', '18:00'), ('019', '19:00'), ('020', '20:00'), ('021', '21:00'), ('022', '22:00'), ('023', '23:00')], default='SELECT', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(default=foodforyou.models.generateUUID, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone_num', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodforyou.User'),
        ),
        migrations.AddField(
            model_name='menus',
            name='restro_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodforyou.Restaurant'),
        ),
        migrations.AddField(
            model_name='manageorder',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodforyou.Orders'),
        ),
        migrations.AddField(
            model_name='manageorder',
            name='restro_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodforyou.Restaurant'),
        ),
        migrations.AddField(
            model_name='jointable',
            name='menu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodforyou.Menus'),
        ),
        migrations.AddField(
            model_name='jointable',
            name='restro_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodforyou.Restaurant'),
        ),
        migrations.AddField(
            model_name='cart',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodforyou.Items'),
        ),
        migrations.AddField(
            model_name='cart',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodforyou.Orders'),
        ),
    ]
