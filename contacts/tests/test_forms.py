from django.test import TestCase
from contacts.forms.create_contact_form import CreateContactForm


class ContactFormTestCase(TestCase):

    def test_create_contact_form_accepts_valid_data(self):
        valid_form_data = {
            'phone_number': '0234110022',
            'name': 'Ronaldo',
            'email': 'ronaldo@yahoo.cm'
        }

        create_contact_form = CreateContactForm(data=valid_form_data)
        self.assertEqual(create_contact_form.is_valid(), True)

    def test_create_contact_form_rejects_valid_data(self):
        pass

    def test_update_contact_form_accepts_valid_data(self):
        pass

    def test_update_contact_form_rejects_valid_data(self):
        pass