import os
from datetime import datetime

import openpyxl
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from openpyxl import Workbook

from .models import AssignSubjectTeacher


def generate_xlsx(request, assignsubjectteacherlist="none"):
    if assignsubjectteacherlist == "none":
        assignsubjectteacherlist = AssignSubjectTeacher.objects.all()

    if not request.user.is_superuser:
        return HttpResponse('Sorry! You need to be authorized to access this link.'
                            + "<a href='../'>" + 'Login here.' +
                            "</a> <br> <br> <br> If you think this is a mistake contact WebAdmin.")

    file_path = os.path.join(os.path.dirname(os.path.realpath(__name__)), 'python_spreadsheet.xlsx')
    output_path = os.path.join(os.path.dirname(os.path.realpath(__name__)), 'temp_python_spreadsheet.xlsx')
    wb = Workbook()
    book = openpyxl.load_workbook(file_path)

    sheet = book.get_sheet_by_name('Sheet1')

    row = 4
    col = 0

    sheet['M1'] = datetime.today().strftime('%Y-%m-%d')

    for subjectteachers in assignsubjectteacherlist:
        sheet[colnum_string(col + 1) + str(row)] = str(subjectteachers.subject.subject_code)
        sheet[colnum_string(col + 2) + str(row)] = str(subjectteachers.subject.name)
        # teacher id
        sheet[colnum_string(col + 3) + str(row)] = str(subjectteachers.semester.getyearpart())
        sheet[colnum_string(col + 4) + str(row)] = str(subjectteachers.subject_teacher.teacher_id)
        #
        # # teacher experience required
        sheet[colnum_string(col + 5) + str(row)] = str(subjectteachers.subject_teacher.full_name())
        #
        sheet[colnum_string(col + 6) + str(row)] = str(subjectteachers.subject_teacher.get_teacher_experience_years())
        #
        sheet[colnum_string(col + 7) + str(row)] = str(subjectteachers.subject_teacher_teaching_experience_years)
        #
        sheet[colnum_string(col + 8) + str(row)] = str(subjectteachers.subject_teacher.home_phone)
        #
        sheet[colnum_string(col + 9) + str(row)] = str(subjectteachers.subject_teacher.mobile_phone)
        #
        sheet[colnum_string(col + 10) + str(row)] = str(subjectteachers.subject_teacher.email)
        #
        sheet[colnum_string(col + 11) + str(row)] = str(subjectteachers.subject_teacher.affiliated_institute.code)
        #
        sheet[colnum_string(col + 12) + str(row)] = str(subjectteachers.subject_teacher.upper_degree)
        #
        sheet[colnum_string(col + 13) + str(row)] = str(subjectteachers.subject_teacher.aff_type)

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


def exportform(request):
    if not request.user.is_superuser:
        return HttpResponse('Sorry! You need to be authorized to access this link.'
                            + "<a href='../'>" + 'Login here.' +
                            "</a> <br> <br> <br> If you think this is a mistake contact WebAdmin.")

    from college.forms import ExportForm
    if request.method == "POST":

        form = ExportForm(request.POST)

        if form.is_valid():
            # post = form.save(commit=False)
            # post.author = request.user
            # post.date_of_creation = datetime.now()
            # post.save()

            outputassignsubjectteacher = AssignSubjectTeacher.objects.all()

            if form.cleaned_data['batch'] is not None:
                outputassignsubjectteacher.filter(batch=form.cleaned_data['batch'])
            if form.cleaned_data['programme'] is not None:
                outputassignsubjectteacher.filter(programme=form.cleaned_data['programme'])
            if form.cleaned_data['semester'] is not None:
                outputassignsubjectteacher.filter(semester=form.cleaned_data['semester'])

            return generate_xlsx(request, outputassignsubjectteacher)

    else:

        form = ExportForm()

    return render(request, 'admin/exportform.html', {'form': form})
