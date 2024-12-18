from django import forms 
from .models import SUBJECTS,Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_no', 'course', 'student_image', 'email', 'address', 'phone', 'marks']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        course = self.instance.course if self.instance.course else None 
        #print(course)
        if course:
            subjects = SUBJECTS.get(course,[])
            for subject in subjects:
                self.fields[f"marks_{subject}"] = forms.IntegerField(required=False,label=subject,initial=None)
    
    def save(self,commit=True):
        instance = super().save(commit=False)
        marks = {}
        for subject in SUBJECTS.get(instance.course,[]):
            subject_fields = f"marks_{subject}"
            marks[subject] = self.cleaned_data.get(subject_fields)
        instance.marks = marks 
        if commit:
            instance.save()
        return instance