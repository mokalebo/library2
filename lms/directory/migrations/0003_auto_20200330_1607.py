# Generated by Django 2.2.11 on 2020-03-30 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
