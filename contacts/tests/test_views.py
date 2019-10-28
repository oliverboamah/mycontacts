from django.test import TestCase, Client
from model_mommy import mommy
from django.forms.models import model_to_dict
from django.urls import reverse
from contacts.models import Contact


class ContactViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_create_contact(self):
        self.assertEqual(Contact.objects.count(), 0)
        contact = mommy.make(Contact)
        data = model_to_dict(contact)

        response = self.client.post(reverse('contacts:create'), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Contact.objects.count(), 1)
