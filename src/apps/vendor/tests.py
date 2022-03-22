from http import HTTPStatus
from django.test import TestCase

# Create your tests here.
class finish_signup_tests(TestCase):
    def test_get(self):
        response = self.client.get("vendor/signup/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Create Your Vendor Profile")