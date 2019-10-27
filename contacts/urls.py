from django.conf.urls import url

from contacts.views import contact_views

urlpatterns = [

    url('', contact_views.get_all_contacts),
    url('contacts/create', contact_views.create_contact),
    url('contacts/update/<int:id>', contact_views.update_contact),
    url('contacts/delete/<int:id>', contact_views.delete_contact),
    url('contacts/contacts-detail/<int:id>', contact_views.get_contact),

    # json get request
    url('contacts/get-contact-json/<int:id>', contact_views.get_contact_json)
]
