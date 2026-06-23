from django.db import migrations, models


class Migration(migrations.Migration):
    # `choices=` lives in Django model state only; this migration emits no DDL.
    # `./manage.py sqlmigrate posthog 1234` returns no statements — verified.
    dependencies = [("posthog", "1233_backfill_duckgresserverteam")]

    operations = [
        migrations.AlterField(
            model_name="userintegration",
            name="kind",
            field=models.CharField(
                choices=[("github", "Github"), ("slack", "Slack")],
                max_length=32,
            ),
        ),
    ]
