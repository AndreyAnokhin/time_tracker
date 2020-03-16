from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase

from .models import TimeTracking


class TestIndexPage(TestCase):
    def test_home_page_works(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'time_tracker_site/index.html')
        self.assertContains(response, 'Time tracking web service')


class TestTimeTrackingModel(TestCase):

    def setUp(self):
        self.test_user = User.objects.create_user('Test User', 'test@test.com', 'testpassword')

    def test_whatever_creation(self):
        project = TimeTracking.objects.create(
            author=self.test_user,
            title='project1',
            description='project1 description',
            hours=1)
        self.assertTrue(isinstance(project, TimeTracking))
        self.assertEqual('project1', project.title)
        self.assertEqual('project1 description', project.description)
        self.assertEqual(1, project.hours)
        self.assertEqual(date.today(), project.date_created.date())

    def tearDown(self):
        self.test_user.delete()
