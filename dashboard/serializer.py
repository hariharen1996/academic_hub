from rest_framework import serializers
from .models import Student,SUBJECTS,Subject,StudentMarks

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id','name','course']

class StudentMarksSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    
    class Meta:
        model = StudentMarks
        fields = ['subject','score']


class StudentSerializer(serializers.ModelSerializer):
    subjects_marks = serializers.SerializerMethodField()

    class Meta:
        model = Student 
        fields = ['id', 'name', 'roll_no', 'course', 'student_image', 'email', 'address', 'phone', 'bookmarked', 'date', 'time', 'subjects_marks']

    def get_subjects_marks(self,obj):
        marks_dict = obj.get_marks()

        marks = []

        for subject_name, score in marks_dict.items():
            subject = Subject.objects.get(name=subject_name,course=obj.course)
            marks.append({
                'subject':SubjectSerializer(subject).data, 
                'score':score
            })

        return marks
        
    