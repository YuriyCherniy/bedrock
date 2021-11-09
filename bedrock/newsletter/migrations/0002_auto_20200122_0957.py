# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Generated by Django 2.2.8 on 2020-01-22 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newsletter", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newsletter",
            name="slug",
            field=models.SlugField(help_text="The ID for the newsletter that will be used by clients", unique=True),
        ),
    ]
