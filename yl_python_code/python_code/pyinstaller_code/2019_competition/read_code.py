import xlrd


def read_file(num):
    file_path = r'./2019竞赛公开题库.xls'
    xls_file = xlrd.open_workbook(file_path)
    xls_sheet = xls_file.sheets()[0]
    row_value = xls_sheet.row_values(num)  # 2313
    return row_value


def get_nrows():
    file_path = r'./2019竞赛公开题库.xls'
    xls_file = xlrd.open_workbook(file_path)
    xls_sheet = xls_file.sheets()[0]
    tihao_list = list()
    for i in range(0, xls_sheet.nrows):
        tihao_list.append(xls_sheet.row_values(i)[0])
    return tihao_list

if __name__ == '__main__':
    read_file(1)
