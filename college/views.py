import os

import openpyxl
from django.http import HttpResponse
# Create your views here.
from openpyxl import Workbook

from .models import Teacher, Subject


def generate_xlsx(context):
    file_path = os.path.join(os.path.dirname(os.path.realpath(__name__)), 'python_spreadsheet.xlsx')
    output_path = os.path.join(os.path.dirname(os.path.realpath(__name__)), 'temp_python_spreadsheet.xlsx')
    wb = Workbook()
    book = openpyxl.load_workbook(file_path)

    sheet = book.get_sheet_by_name('Sheet1')

    row = 4
    col = 2

    for Subject.name in Subject.objects.all():
        sheet[colnum_string(col) + str(row)] = str(Subject.name.name)

        # TODO add other methods to dump in xlsx here

        row += 1

    book.save(output_path)

    response = HttpResponse(open(output_path, 'rb').read())
    response['Content-Type'] = 'mimetype/submimetype'
    response['Content-Disposition'] = 'attachment; filename=DownloadedEval.xlsx'
    return response


def colnum_string(n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string
