from django.test import TestCase
from .models import Student

class StudentTestCase(TestCase):
    def test_create_student(self):
        student = Student.objects.create(name="Alice", address="C streets")
        self.assertEqual(student.name, "Alice")
        self.assertEqual(student.address, "C streets")


class StudentControllerTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # هذه الدالة تنفذ مرة واحدة قبل كل الاختبارات
        cls.student = Student.objects.create(name="Charlie", address="Algeria")

    def test_should_save_student(self):
        # تأكد من أن الطالب تم حفظه
        count = Student.objects.count()
        self.assertEqual(count, 1)

    def test_should_find_all_students(self):
        # تأكد من استرجاع جميع الطلاب
        students = Student.objects.all()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].name, "Charlie")