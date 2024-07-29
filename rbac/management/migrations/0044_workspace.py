# Generated by Django 4.2.11 on 2024-07-18 06:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import management.rbac_fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0014_auto_20220726_1743"),
        ("management", "0043_auditlog"),
    ]

    operations = [
        migrations.CreateModel(
            name="Workspace",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ("parent", models.UUIDField(blank=True, editable=False, null=True)),
                ("description", models.CharField(max_length=255, blank=True, editable=False, null=True)),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                ("modified", management.rbac_fields.AutoDateTimeField(default=django.utils.timezone.now)),
                ("tenant", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.tenant")),
            ],
            options={
                "ordering": ["name", "modified"],
            },
        ),
        migrations.AddConstraint(
            model_name="workspace",
            constraint=models.UniqueConstraint(
                fields=("name", "tenant", "parent"),
                name="The combination of 'name', 'tenant', and 'parent' must be unique.",
            ),
        ),
    ]
