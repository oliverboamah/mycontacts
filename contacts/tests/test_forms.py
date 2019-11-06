from django.test import TestCase
from contacts.forms.create_contact_form import CreateContactForm
from contacts.forms.update_contact_form import UpdateContactForm


class ContactFormTestCase(TestCase):
    valid_form_data = {
        'phone_number': '0234110022',
        'name': 'Ronaldo',
        'email': 'ronaldo@yahoo.com'
    }

    invalid_form_data = {
        'phone_number': '0234110022',
        'name': 'Ronaldo',
        'email': 'ronaldo'
    }

    def test_create_contact_form_accepts_valid_data(self):
        create_contact_form = CreateContactForm(data=self.valid_form_data)
        self.assertEqual(create_contact_form.is_valid(), True)

        self.assertEqual(create_contact_form.cleaned_data['phone_number'], self.valid_form_data['phone_number'])
        self.assertEqual(create_contact_form.cleaned_data['name'], self.valid_form_data['name'])
        self.assertEqual(create_contact_form.cleaned_data['email'], self.valid_form_data['email'])

    def test_create_contact_form_rejects_invalid_data(self):
        create_contact_form = CreateContactForm(data=self.invalid_form_data)
        self.assertEqual(create_contact_form.is_valid(), False)

    def test_update_contact_form_accepts_valid_data(self):
        update_contact_form = UpdateContactForm(data=self.valid_form_data)
        self.assertEqual(update_contact_form.is_valid(), True)

        self.assertEqual(update_contact_form.cleaned_data['phone_number'], self.valid_form_data['phone_number'])
        self.assertEqual(update_contact_form.cleaned_data['name'], self.valid_form_data['name'])
        self.assertEqual(update_contact_form.cleaned_data['email'], self.valid_form_data['email'])

    def test_update_contact_form_rejects_invalid_data(self):
        update_contact_form = UpdateContactForm(data=self.invalid_form_data)
        self.assertEqual(update_contact_form.is_valid(), False)
