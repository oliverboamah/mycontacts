from django.test import TestCase, Client
from model_mommy import mommy
from django.forms.models import model_to_dict
from django.urls import reverse
from contacts.models import Contact


class ContactViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_create_contact(self):
        self.assertEqual(Contact.objects.filter(is_deleted=False).count(), 0)
        contact = mommy.make(Contact)
        data = model_to_dict(contact)

        response = self.client.post(reverse('contacts:create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Contact.objects.filter(is_deleted=False).count(), 1)

    def test_update_contact(self):
        # create new contact
        self.assertEqual(Contact.objects.filter(is_deleted=False).count(), 0)
        contact = mommy.make(Contact)
        contact_dict = model_to_dict(contact)

        response = self.client.post(reverse('contacts:create'), contact_dict)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Contact.objects.filter(is_deleted=False).count(), 1)

        # retrieve created contact
        contact = Contact.objects.filter(pk=1, is_deleted=False).first()

        # update contact
        contact.email = 'oliverboamah@yahoo.com'
        contact.name = 'Oliver'
        contact.phone_number = '0553290000'

        # save updated contact
        contact_dict = model_to_dict(contact)

        response = self.client.post(reverse('contacts:update', kwargs={'contact_id': contact.id}), contact_dict)
        self.assertEqual(response.status_code, 302)

        # retrieve updated contact
        contact = Contact.objects.filter(pk=1, is_deleted=False).first()

        # assert that the contact was updated
        self.assertEqual(contact.email, 'oliverboamah@yahoo.com')
        self.assertEqual(contact.name, 'Oliver')
        self.assertEqual(contact.phone_number, '0553290000')

    def test_delete_contact(self):
        # create new contact
        self.assertEqual(Contact.objects.filter(is_deleted=False).count(), 0)
        contact = mommy.make(Contact)
        contact_dict = model_to_dict(contact)

        # assert that the contact was created
        response = self.client.post(reverse('contacts:create'), contact_dict)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Contact.objects.filter(is_deleted=False).count(), 1)

        # retrieve created contact
        contact = Contact.objects.filter(pk=1, is_deleted=False).first()

        # delete contact
        response = self.client.post(reverse('contacts:delete', kwargs={'contact_id': contact.id}), contact_dict)
        self.assertEqual(response.status_code, 302)

        # assert that the contact was deleted
        self.assertEqual(Contact.objects.filter(is_deleted=False).count(), 0)

    def test_show_contact_detail(self):
        # create new contact
        self.assertEqual(Contact.objects.filter(is_deleted=False).count(), 0)
        contact = mommy.make(Contact)
        contact_dict = model_to_dict(contact)

        # assert that the contact was created
        response = self.client.post(reverse('contacts:create'), contact_dict)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Contact.objects.filter(is_deleted=False).count(), 1)

        # retrieve created contact
        contact = Contact.objects.filter(pk=1, is_deleted=False).first()

        # go to contact detail page
        response = self.client.get(reverse('contacts:show', kwargs={'contact_id': contact.id}))
        self.assertEqual(response.status_code, 200)

        # assert that the contact details is shown in the template
        self.assertEqual(response.context['contact'].phone_number, contact.phone_number)
        self.assertEqual(response.context['contact'].name, contact.name)
        self.assertEqual(response.context['contact'].email, contact.email)

    def test_all_contacts_view(self):
        # create 10 new contacts
        i = 0
        while i < 10:
            # create new contact
            self.assertEqual(Contact.objects.filter(is_deleted=False).count(), 0 + i)
            contact = mommy.make(Contact)
            contact_dict = model_to_dict(contact)

            # assert that the contact was created
            response = self.client.post(reverse('contacts:create'), contact_dict)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(Contact.objects.filter(is_deleted=False).count(), 1 + i)

            i += 1

        # go to index template (it shows list of all contacts)
        response = self.client.get(reverse('contacts:index'))

        # assert that the template shows 10 contacts
        self.assertEqual(len(response.context['contacts']), 10)
