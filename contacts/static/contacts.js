$(document).ready(function () {

    // update modal form with existing data
    $('.update-contact').click(function () {
        const id = $(this).attr('id');

        $.get('get-contact-json/' + id, function (data, status) {
            if (status === 'success') {

                console.log(data);

                // set form action url
                $('#update_contact_form').attr('action', 'update/' + data.id);

                // set form inputs with existing data
                $('#phone_number').val(data.phone_number);
                $('#name').val(data.name);
                $('#email').val(data.email);
            }
        })

    });

    // permission alert for contact deletion
    $('.delete-contact').click(function () {
        const id = $(this).attr('id');
        const message = 'Sure you want to delete this contact?';

        Swal.fire({
            title: 'Confirm Delete',
            text: message,
            type: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Yes, delete it!'
        }).then((result) => {
            if (result.value) {
                window.location = 'delete/' + id;
            }
        })
    });
});