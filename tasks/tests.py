from django.test import TestCase
from tasks.models import Task
# Create your tests here.
class TestModel(TestCase):
    
    def setUp(self):
        test=Test(title="My test title")
        self.assertEqual(str(test),test.title)
