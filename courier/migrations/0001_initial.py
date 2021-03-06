# Generated by Django 3.2.4 on 2021-06-06 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Depot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название склада', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_now_add=True)),
                ('name', models.CharField(help_text='Имя', max_length=200)),
                ('surname', models.CharField(help_text='Фамилия', max_length=200)),
                ('phone', models.CharField(help_text='Номер телефона', max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(help_text='Широта')),
                ('lon', models.FloatField(help_text='Долгота')),
                ('address', models.CharField(blank=True, help_text='Адрес', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.FloatField(help_text='Объем заказа')),
                ('capacity', models.FloatField(help_text='Вес заказа')),
                ('title', models.CharField(help_text='Комментарий к заказу', max_length=200)),
                ('phone', models.CharField(help_text='Номер телефона получателя', max_length=14)),
                ('isDelivered', models.BooleanField(default=False, help_text='Заказ доставлен')),
                ('location_id', models.ForeignKey(help_text='Адрес заказа', on_delete=django.db.models.deletion.DO_NOTHING, to='courier.location')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.FloatField(help_text='Объем кузова')),
                ('capacity', models.FloatField(help_text='Грузоподъемность')),
                ('title', models.CharField(help_text='Название модели', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('number', models.CharField(help_text='Госномер', max_length=200, primary_key=True, serialize=False)),
                ('model_id', models.ForeignKey(help_text='Модель машины', on_delete=django.db.models.deletion.DO_NOTHING, to='courier.vehiclemodel')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Комментарий к маршруту', max_length=200)),
                ('date', models.DateField(auto_now_add=True, help_text='Дата маршрута')),
                ('courier', models.ForeignKey(help_text='Курьер', on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='courier.employee')),
                ('depots', models.ManyToManyField(to='courier.Depot')),
                ('logistician', models.ForeignKey(help_text='Логист', on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='courier.employee')),
                ('orders', models.ManyToManyField(to='courier.Order')),
                ('vehicle_number', models.ForeignKey(help_text='Машина', on_delete=django.db.models.deletion.DO_NOTHING, to='courier.vehicle')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='role_id',
            field=models.ForeignKey(help_text='Роль', on_delete=django.db.models.deletion.DO_NOTHING, to='courier.employeerole'),
        ),
        migrations.AddField(
            model_name='depot',
            name='location_id',
            field=models.ForeignKey(help_text='Адрес склада', on_delete=django.db.models.deletion.DO_NOTHING, to='courier.location'),
        ),
    ]
