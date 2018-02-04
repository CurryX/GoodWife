function modify(data) {
    data['id'] = id;
    $.ajax({
        url: '/order_modify',
        data: data,
        complete: function () {
            window.location.reload();
        }
    });
}

function orderUncomplete() {
    modify({'action': 'uncomplete'});
}

function orderComplete() {
    modify({'action': 'complete'});
}

function orderDelete() {
    window.location.href = '/order_delete/' + id;
}

function orderPrint() {
    $('.no-print').hide();
    window.print();
    $('.no-print').show();
}

$(document)
    .on('click', '#order-uncomplete', orderUncomplete)
    .on('click', '#order-complete', orderComplete)
    .on('click', '#order-delete', orderDelete)
    .on('click', '#order-print', orderPrint);
