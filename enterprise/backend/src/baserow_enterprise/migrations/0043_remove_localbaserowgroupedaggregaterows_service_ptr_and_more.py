# Generated by Django 5.0.9 on 2025-04-02 09:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("baserow_enterprise", "0042_localbaserowtableserviceaggregationsortby"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.RemoveField(
                    model_name="localbaserowgroupedaggregaterows",
                    name="service_ptr",
                ),
                migrations.RemoveField(
                    model_name="localbaserowgroupedaggregaterows",
                    name="table",
                ),
                migrations.RemoveField(
                    model_name="localbaserowgroupedaggregaterows",
                    name="view",
                ),
                migrations.RemoveField(
                    model_name="localbaserowtableserviceaggregationgroupby",
                    name="field",
                ),
                migrations.RemoveField(
                    model_name="localbaserowtableserviceaggregationgroupby",
                    name="service",
                ),
                migrations.RemoveField(
                    model_name="localbaserowtableserviceaggregationseries",
                    name="field",
                ),
                migrations.RemoveField(
                    model_name="localbaserowtableserviceaggregationseries",
                    name="service",
                ),
                migrations.RemoveField(
                    model_name="localbaserowtableserviceaggregationsortby",
                    name="service",
                ),
                migrations.DeleteModel(
                    name="ChartWidget",
                ),
                migrations.DeleteModel(
                    name="LocalBaserowGroupedAggregateRows",
                ),
                migrations.DeleteModel(
                    name="LocalBaserowTableServiceAggregationGroupBy",
                ),
                migrations.DeleteModel(
                    name="LocalBaserowTableServiceAggregationSeries",
                ),
                migrations.DeleteModel(
                    name="LocalBaserowTableServiceAggregationSortBy",
                ),
            ],
            database_operations=[
                migrations.AlterModelTable(
                    name="ChartWidget",
                    table="baserow_premium_chartwidget",
                ),
                migrations.AlterModelTable(
                    name="LocalBaserowGroupedAggregateRows",
                    table="baserow_premium_localbaserowgroupedaggregaterows",
                ),
                migrations.AlterModelTable(
                    name="LocalBaserowTableServiceAggregationGroupBy",
                    table="baserow_premium_localbaserowtableserviceaggregationgroupby",
                ),
                migrations.AlterModelTable(
                    name="LocalBaserowTableServiceAggregationSeries",
                    table="baserow_premium_localbaserowtableserviceaggregationseries",
                ),
                migrations.AlterModelTable(
                    name="LocalBaserowTableServiceAggregationSortBy",
                    table="baserow_premium_localbaserowtableserviceaggregationsortby",
                ),
            ],
        ),
    ]
