df_csv = load_data_from_file("../data/other_db.csv", file_type='csv')  
summary_csv = get_general_summary(df_csv)  
print(summary_csv)