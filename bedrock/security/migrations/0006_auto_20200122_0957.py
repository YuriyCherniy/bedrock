# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Generated by Django 2.2.8 on 2020-01-22 17:57

from django.db import migrations, models

import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("security", "0005_mitrecve_mfsa_ids"),
    ]

    operations = [
        migrations.AlterField(
            model_name="halloffamer",
            name="program",
            field=models.CharField(choices=[("web", "Web"), ("client", "Client")], max_length=10),
        ),
        migrations.AlterField(
            model_name="securityadvisory",
            name="last_modified",
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True),
        ),
    ]
