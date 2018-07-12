from django import forms

from college.models import AssignSubjectTeacher, Batch, Programme, Year

Semester_Choices = {("", '----'), ('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth')}


def set_field_html_name(cls, new_name):
    """
    This creates wrapper around the normal widget rendering,
    allowing for a custom field name (new_name).
    """
    old_render = cls.widget.render

    def _widget_render_wrapper(name, value, attrs=None):
        return old_render(new_name, value, attrs)

    cls.widget.render = _widget_render_wrapper


class ExportForm(forms.ModelForm):
    year = forms.ModelChoiceField(queryset=Year.objects.all(), required=False)
    batch = forms.ModelChoiceField(queryset=Batch.objects.all(), required=False)
    programme = forms.ModelChoiceField(queryset=Programme.objects.all(), required=False)
    part = forms.ChoiceField(choices={("", '----'), ('Even', 'Even'), ('Odd', 'Odd')}, required=False)
    semester = forms.ChoiceField(choices=Semester_Choices, required=False)

    set_field_html_name(year, 'Academic Year')

    class Meta:
        model = AssignSubjectTeacher
        fields = ('year', 'batch', 'programme', 'semester', 'part')


class CloneForm(forms.ModelForm):
    Academic_year_from = forms.ModelChoiceField(queryset=Year.objects.all(), required=True)
    Academic_year_to = forms.ModelChoiceField(queryset=Year.objects.all(), required=True)

    class Meta:
        model = AssignSubjectTeacher
        fields = ('Academic_year_from', 'Academic_year_to')