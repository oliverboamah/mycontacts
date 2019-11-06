from django.conf.urls import url

from contacts.views import contact_views

app_name = 'contacts'

urlpatterns = [
    url(
        regex=r'^$',
        view=contact_views.get_all_contacts,
        name='index'
    ),

    url(
        regex=r'^create/$',
        view=contact_views.create_contact,
        name='create'
    ),

    url(
        regex=r'^update/(?P<contact_id>\d+)$',
        view=contact_views.update_contact,
        name='update'
    ),

    url(
        regex=r'^delete/(?P<contact_id>\d+)$',
        view=contact_views.delete_contact,
        name='delete'
    ),
    url(
        regex=r'^show/(?P<contact_id>\d+)$',
        view=contact_views.get_contact,
        name='show'
    ),
    url(
        regex=r'^get-contact-json/(?P<contact_id>\d+)$',
        view=contact_views.get_contact_json,
        name='get-contact-json'
    ),
    url(
        regex=r'^test_redis/$',
        view=contact_views.test_redis,
        name='index'
    ),
]
