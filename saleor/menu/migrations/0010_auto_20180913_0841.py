# Generated by Django 2.0.8 on 2018-09-13 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("menu", "0009_remove_menu_json_content")]

    operations = [
        migrations.RenameField(
            model_name="menu", old_name="json_content_new", new_name="json_content"
        )
    ]
