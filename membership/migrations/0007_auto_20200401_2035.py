# Generated by Django 3.0.4 on 2020-04-01 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_book_summary'),
        ('membership', '0006_loan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='library.BookInstance'),
        ),
    ]
