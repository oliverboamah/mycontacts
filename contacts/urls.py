from django.conf.urls import url

from contacts.views import contact_views

urlpatterns = [

    url('', contact_views.get_all_tasks),
    url('contacts/create', contact_views.create_task),
    url('contacts/update/<int:id>', contact_views.update_task),
    url('contacts/delete/<int:id>', contact_views.delete_task),
    url('contacts/contacts-detail/<int:id>', contact_views.get_task),

    # json get request
    url('contacts/get-contact-json/<int:id>', contact_views.get_task_json)
]
