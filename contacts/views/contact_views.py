# Django imports
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.core.cache import cache

# My App imports
from contacts.forms.create_contact_form import CreateContactForm
from contacts.forms.update_contact_form import UpdateContactForm
from contacts.models.contact_model import Contact


# create contact
def create_contact(request):
    try:
        form = CreateContactForm(data=request.POST)
        form.is_valid()
        form.save()
        messages.success(request, "Contact created successfully!")
    except Exception as e:
        messages.error(request, e)

    return redirect('contacts:index')


# delete contact
def delete_contact(request, contact_id):
    try:
        contact = Contact.objects.get(pk=contact_id)
        contact.is_deleted = True
        contact.save()
        messages.success(request, "Contact deleted successfully!")
    except Exception as e:
        messages.error(request, e)

    return redirect('contacts:index')


# update contact
def update_contact(request, contact_id):
    if request.method == 'POST':
        try:
            contact = Contact.objects.get(pk=contact_id)
            form = UpdateContactForm(data=request.POST, instance=contact)
            form.save()
            messages.success(request, 'Contact has been updated successfully!')
        except Exception as e:
            messages.error(request, e)

        return redirect('contacts:index')


# retrieve all contacts
def get_all_contacts(request):
    contacts = Contact.objects.filter(is_deleted=False).order_by('id')
    create_contact_form = CreateContactForm()
    update_contact_form = UpdateContactForm()

    context = {
        'contacts': contacts,
        'create_contact_form': create_contact_form,
        'update_contact_form': update_contact_form
    }
    return render(request=request, template_name='contacts/index.html', context=context)


# show single contact
def get_contact(request, contact_id):
    contact = Contact.objects.filter(pk=contact_id).first()

    context = {
        'contact': contact
    }
    return render(request=request, template_name='contacts/contact-detail.html', context=context)


# get contact as json
def get_contact_json(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    contact_dict = {
        'id': contact.id,
        'phone_number': contact.phone_number,
        'name': contact.name,
        'email': contact.email
    }
    return JsonResponse(data=contact_dict, safe=True)


# test redis
def test_redis(request):
    try:
        cache.__setattr__('key', 'value')
    except Exception as e:
        messages.error(request, e)

    return HttpResponse('Key: ' + cache.__getattr__('key'))
