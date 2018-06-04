import os
from datetime import datetime

import openpyxl
from django.http import HttpResponse
# Create your views here.
from openpyxl import Workbook

from .models import Subject


def generate_xlsx(context):
    file_path = os.path.join(os.path.dirname(os.path.realpath(__name__)), 'python_spreadsheet.xlsx')
    output_path = os.path.join(os.path.dirname(os.path.realpath(__name__)), 'temp_python_spreadsheet.xlsx')
    wb = Workbook()
    book = openpyxl.load_workbook(file_path)

    sheet = book.get_sheet_by_name('Sheet1')

    row = 4
    col = 0

    sheet['M1'] = datetime.today().strftime('%Y-%m-%d')

    for subjects in Subject.objects.all():
        sheet[colnum_string(col + 1) + str(row)] = str(subjects.program_code)
        sheet[colnum_string(col + 2) + str(row)] = str(subjects.name)
        # teacher id
        sheet[colnum_string(col + 3) + str(row)] = str(subjects.semester.getyearpart())
        sheet[colnum_string(col + 4) + str(row)] = str(subjects.subject_teacher.teacher_id)
        #
        # # teacher experience required
        sheet[colnum_string(col + 5) + str(row)] = str(subjects.subject_teacher.name)
        #
        sheet[colnum_string(col + 6) + str(row)] = str(subjects.subject_teacher.get_teacher_experience_years())
        #
        sheet[colnum_string(col + 7) + str(row)] = str(subjects.subject_teacher_teaching_experience_years)
        #
        sheet[colnum_string(col + 9) + str(row)] = str(subjects.subject_teacher.phone)
        #
        sheet[colnum_string(col + 10) + str(row)] = str(subjects.subject_teacher.email)
        #
        sheet[colnum_string(col + 11) + str(row)] = str(subjects.subject_teacher.affiliated_institute)
        #
        sheet[colnum_string(col + 12) + str(row)] = str(subjects.subject_teacher.upper_degree)
        #
        sheet[colnum_string(col + 13) + str(row)] = str(subjects.subject_teacher.aff_type)

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
