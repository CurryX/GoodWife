function listRowClick() {
    var id = $(this).data('id');
    window.location.href = '/order/' + id;
}

$(document)
    .on('click', '.list-row', listRowClick);
