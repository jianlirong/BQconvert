import sys
# Get the list of Tables based on inputs (get_table_col_list)
def sql_table_filter(sh_whitlist,sh_blocklist,tbl_whitelist,tbl_blocklist,source):
    if str(sh_whitlist) == 'None':
        if str(source) == 'redshift':
            schema_name_in = " and table_schema='public'"
        else:
            print('Please specify the schema')
            sys.exit(1)
    else:
        schema_name_in = ' and table_schema in ({})'.format("'" + str(sh_whitlist).replace(',','\',\'') + "'")
    if str(sh_blocklist) == 'None':
        schema_name_not_in = ''
    else:
        schema_name_not_in = ' and table_schema not in ({})'.format("'" + str(sh_blocklist).replace(',','\',\'') + "'")
    
    if str(tbl_whitelist) == 'None':
        table_name_in = ''
    else:
        table_name_in = ' and table_name in ({})'.format("'" + str(tbl_whitelist).replace(',','\',\'') + "'")

    if str(tbl_blocklist) == 'None':
        table_name_not_in = ''
    else:
        table_name_not_in = ' and table_name not in ({})'.format("'" + str(tbl_blocklist).replace(',','\',\'') + "'")
    sql_filtered_tables = '''{}{}{}{}'''.format(schema_name_in,schema_name_not_in,table_name_in,table_name_not_in)   
    return sql_filtered_tables