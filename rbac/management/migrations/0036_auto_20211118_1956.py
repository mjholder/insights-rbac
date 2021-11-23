# Generated by Django 2.2.24 on 2021-11-18 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("management", "0035_auto_20211014_1736")]

    operations = [
        migrations.AlterField(
            model_name="access",
            name="tenant",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.Tenant"),
        ),
        migrations.AlterField(
            model_name="group",
            name="tenant",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.Tenant"),
        ),
        migrations.AlterField(
            model_name="permission",
            name="tenant",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.Tenant"),
        ),
        migrations.AlterField(
            model_name="policy",
            name="tenant",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.Tenant"),
        ),
        migrations.AlterField(
            model_name="principal",
            name="tenant",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.Tenant"),
        ),
        migrations.AlterField(
            model_name="resourcedefinition",
            name="tenant",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.Tenant"),
        ),
        migrations.AlterField(
            model_name="role",
            name="tenant",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.Tenant"),
        ),
    ]
