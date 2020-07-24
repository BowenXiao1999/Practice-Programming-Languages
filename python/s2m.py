import csv
import xlrd
import codecs

m = {

}
def xlsx_to_csv():
    workbook = xlrd.open_workbook('1.xlsx')
    table = workbook.sheet_by_index(0)
    arr = []
    key = table.col_values(0)
    text = table.col_values(1)
    arr.append(key[1:])
    for i in range(len(key)):
        if key[i] in m:
            key[i] = m[key[i]]
    arr.append(text[1:])
    col_names = table.row_values(0)
    header = ["key", "text", "result"]
    for col_num in range(2, table.ncols-1):
        with codecs.open('{}.csv'.format(col_names[col_num]), 'w', encoding='utf-8') as f:
            write = csv.writer(f)
            cur = arr[:]
            trans = table.col_values(col_num)
            cur.append(trans[1:])

            ret = [header]
            for i in zip(*cur):
                ret.append(i)
            # write.writerows(ret)
            for r in ret:
                write.writerow(r)

        cur = arr[:]



if __name__ == '__main__':
    xlsx_to_csv()