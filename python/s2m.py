import csv
import xlrd
import codecs

m = {
    'pm_mt_rec_help_ios_tipone': 'components.0.components.0.text',
    'pm_mt_rec_help_ios_tipone_text': 'components.0.components.1.text',
    'pm_mt_rec_help_ios_pic_title': 'components.0.components.3.text',
    'pm_mt_rec_help_ios_pic_button': 'components.0.components.4.text',
    'pm_mt_rec_help_ios_tiptwo': 'components.0.components.5.text',
    'pm_mt_rec_help_ios_tiptwo_text': 'components.0.components.6.text',
    'pm_mt_rec_help_ios_tipthree': 'components.0.components.7.text',
    'pm_mt_rec_help_ios_tipthree_text': 'components.0.components.8.text',
    'pm_mt_rec_help_ios_tipfour': 'components.0.components.9.text',
    'pm_mt_rec_help_ios_tipfour_text': 'components.0.components.10.text',
    # 'pm_mt_rec_help_android_tipone': 'components.0.components.0.text',
    # 'pm_mt_rec_help_android_tipone_text': 'components.0.components.1.text',
    # 'pm_mt_rec_help_android_tiptwo': 'components.0.components.2.text',
    # 'pm_mt_rec_help_android_tiptwo_text': 'components.0.components.3.text',
}
def xlsx_to_csv():
    workbook = xlrd.open_workbook('1.xlsx')
    table = workbook.sheet_by_index(0)
    arr = []
    key = table.col_values(0)
    text = table.col_values(1)
    
    # IOS
    stratIndex = 2
    endIndex = 12

    keyForMagic = []
    for i in range(stratIndex, len(key)):
        if key[i] in m:
        #     key[i] = m[key[i]]
            keyForMagic.append(m[key[i]])
    
    arr.append(keyForMagic[:])
    arr.append(text[stratIndex:endIndex])
    col_names = table.row_values(0)
    header = ["key", "text", "result"]
    for col_num in range(3, table.ncols-1):
        with codecs.open('{}.csv'.format(col_names[col_num]), 'w', encoding='utf-8') as f:
            write = csv.writer(f)
            cur = arr[:]
            trans = table.col_values(col_num)
            cur.append(trans[stratIndex:endIndex])

            ret = [header]
            for i in zip(*cur):
                ret.append(i)
            # write.writerows(ret)
            for r in ret:
                write.writerow(r)

        cur = arr[:]



if __name__ == '__main__':
    xlsx_to_csv()