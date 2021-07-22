# Generated by Django 2.2.4 on 2021-07-22 11:56

from django.db import migrations


def set_ready_on_existing_data(apps, schema_editor):
    Tenant = apps.get_model("api", "Tenant")
    Tenant.objects.all().update(ready=True)


class Migration(migrations.Migration):

    dependencies = [("api", "0008_tenant_ready")]

    operations = [migrations.RunPython(set_ready_on_existing_data)]