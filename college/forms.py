from django import forms

from college.models import AssignSubjectTeacher, Batch, Programme, Year

Semester_Choices = {("", '----'), ('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth')}


class ExportForm(forms.ModelForm):
    year = forms.ModelChoiceField(queryset=Year.objects.all(), required=False)
    batch = forms.ModelChoiceField(queryset=Batch.objects.all(), required=False)
    programme = forms.ModelChoiceField(queryset=Programme.objects.all(), required=False)
    part = forms.ChoiceField(choices={("", '----'), ('Even', 'Even'), ('Odd', 'Odd')}, required=False)
    semester = forms.ChoiceField(choices=Semester_Choices, required=False)

    class Meta:
        model = AssignSubjectTeacher
        fields = ('year', 'batch', 'programme', 'semester', 'part')
