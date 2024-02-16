# Generated by Django 5.0.2 on 2024-02-16 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_app', '0004_book_displayed_identity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='displayed_identity',
        ),
        migrations.AddField(
            model_name='book',
            name='displayed_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Displayed Name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='author_pseudonym',
            field=models.CharField(blank=True, help_text='Enter author pseudonym (max 100 characters).', max_length=100, null=True, verbose_name='Author Pseudonym'),
        ),
    ]
