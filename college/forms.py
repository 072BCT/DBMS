from django import forms

from college.models import AssignSubjectTeacher, Batch, Semester, Programme


class ExportForm(forms.ModelForm):
    batch = forms.ModelChoiceField(queryset=Batch.objects.all(), required=False)
    programme = forms.ModelChoiceField(queryset=Programme.objects.all(), required=False)
    semester = forms.ModelChoiceField(queryset=Semester.objects.all(), required=False)

    class Meta:
        model = AssignSubjectTeacher
        fields = ('batch','programme', 'semester',)
