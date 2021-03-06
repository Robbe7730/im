# Generated by Django 2.1.1 on 2018-09-16 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pantryitem',
            name='category',
            field=models.CharField(choices=[('UC', 'UNCATEGORIZED'), ('GS', 'GENRAL_STOCK'), ('CANS', 'CANS'), ('BR', 'BREAKFAST'), ('SAV', 'SAVORIES'), ('SW', 'SWEETS'), ('SN', 'SNACKS'), ('SP', 'SPICES')], default='UN', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pantryitemline',
            name='expiry_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='pantryitemline',
            name='pantry_item',
            field=models.ForeignKey(default='UN', on_delete=django.db.models.deletion.PROTECT, to='inventory.PantryItem'),
        ),
    ]
