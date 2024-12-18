from rest_framework import serializers
from .models import Student,SUBJECTS 


class StudentSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()
    print(subjects)

    class Meta:
        model = Student 
        fields = ['id', 'name', 'roll_no', 'course', 'student_image', 'email', 'address', 'phone', 'marks', 'subjects','bookmarked','date','time']

        
    def get_subjects(self,data):
        print(data)
        return SUBJECTS.get(data.course,[])
    
    def create(self,validated_data):
        marks = {}

        course = validated_data.get('course')
        print(course)
        subjects = SUBJECTS.get(course,[])
        print(subjects)
        for subject in subjects:
            marks[subject] = validated_data.get(f"marks_{subject}",None)
        validated_data['marks'] = marks
        print(marks)
        return super().create(validated_data)

    def update(self,instance,validated_data):
        marks = {}
        course = validated_data.get('course',instance.course)
        subjects = SUBJECTS.get(course, [])
        for subject in subjects:
            marks[subject] = validated_data.get(f"marks_{subject}",instance.marks.get(subject,None))
        validated_data['marks'] = marks 
        print(marks)
        return super().update(instance,validated_data)    

