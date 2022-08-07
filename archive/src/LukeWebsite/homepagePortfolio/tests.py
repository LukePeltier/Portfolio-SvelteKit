from django.test import TestCase
from django.urls import reverse


class BasicViewsTest(TestCase):
    def test_dashboard_view(self):
        url = reverse("home")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
