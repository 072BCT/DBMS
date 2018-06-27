from django import forms

from college.models import AssignSubjectTeacher, Batch, Semester


class ExportForm(forms.ModelForm):
    batch = forms.ModelChoiceField(queryset=Batch.objects.all(), required=False)
    semester = forms.ModelChoiceField(queryset=Semester.objects.all(), required=False)

    class Meta:
        model = AssignSubjectTeacher
        fields = ('batch', 'semester',)
