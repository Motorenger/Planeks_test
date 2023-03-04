from django.contrib import admin

from data_schemas.models import DataSchema, Column, DataType, Arguments


class ColumnInline(admin.TabularInline):
    model = DataSchema.columns.through


@admin.register(Column)
class DataSchemaAdmin(admin.ModelAdmin):
    fields = ("name", "data_type", "order")


@admin.register(DataSchema)
class DataSchemaAdmin(admin.ModelAdmin):
    exclude = ('columns',)
    inlines = [
        ColumnInline,
    ]


admin.site.register(DataType)
admin.site.register(Arguments)
