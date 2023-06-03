# Generated by Django 4.1.7 on 2023-06-01 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_category_name_en_us_category_name_ru_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostCategory_en_us',
            new_name='PostCategory_en',
        ),
        migrations.AlterModelOptions(
            name='postcategory_en',
            options={'verbose_name': 'post category [en]', 'verbose_name_plural': 'post categorys [en]'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name_en_us',
            new_name='name_en',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author_en_us',
            new_name='author_en',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='category_type_en_us',
            new_name='category_type_en',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='postCategory_en_us',
            new_name='postCategory_en',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='text_en_us',
            new_name='text_en',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title_en_us',
            new_name='title_en',
        ),
        migrations.AlterModelTable(
            name='postcategory_en',
            table='news_postcategory_en',
        ),
    ]