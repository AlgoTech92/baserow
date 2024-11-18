# Generated by Django 5.0.9 on 2024-10-09 13:10

from django.db import migrations

update_password_tsv_index = """
do $$
declare
    tname text;
    cname text;
    schema_record information_schema.columns%rowtype;
begin
for tname, cname
    in select 'database_table_'||f.table_id, 'tsv_field_'||f.id
       from database_passwordfield p join database_field f on f.id = p.field_ptr_id
loop

    select into schema_record * from information_schema.columns where table_name = tname and column_name = cname;
    if schema_record.column_name is not null then
        raise notice '%.%', tname, cname;
        execute 'update '|| tname || ' set '|| cname || ' = null';
    end if;

end loop;

end
$$;
"""  # nosec B105


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0169_alter_galleryview_card_cover_image_field"),
    ]

    operations = [migrations.RunSQL(update_password_tsv_index)]