# Generated by Django 3.0.4 on 2020-04-01 18:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_book_summary'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('membership', '0005_auto_20200401_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_loan', models.DateField(default=datetime.date(2020, 4, 1))),
                ('date_of_return', models.DateField(default=datetime.date(2020, 4, 22))),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.BookInstance')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
