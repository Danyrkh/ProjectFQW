import pandas


def cleaner(df, my_list):
    for i in my_list:
        del df[i]
    return df


wb = pandas.read_excel('/Users/hamster/Desktop/ВКР/Выгрузка данных.xlsx')
wb_pfk = wb[wb['Фирма-производитель'] == 'ОБНОВЛЕНИЕ ПФК АО']
wb_pfk['Дата'] = '1' + ' ' + wb_pfk['Месяц'].astype(str) + ' ' + wb_pfk['Год'].astype(str)
wb_pfk = cleaner(wb_pfk,
                 ['Регион', 'Объем (розница), упак.', 'Полное наименование', 'Бренд', 'Год', 'Месяц', 'Дозировка'])
wb_pfk['Дата'] = pandas.to_datetime(wb_pfk['Дата']).dt.date
wb_pfk = wb_pfk.reset_index(drop=True)
mnn_pfk = list(set(wb_pfk['МНН']))

with pandas.ExcelWriter('/Users/hamster/Desktop/ВКР/ClearData.xlsx') as writer:
    for i in mnn_pfk:
        if len(i) >= 31:
            wb_pfk[wb_pfk['МНН'] == i].to_excel(writer, sheet_name='{}'.format(i.split(' ')[0]), index=False)
        else:
            wb_pfk[wb_pfk['МНН'] == i].to_excel(writer, sheet_name='{}'.format(i.partition('+')[0]), index=False)

print('Operation completed successfully')
