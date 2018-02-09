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

function orderUnpickAll() {
    modify({'action': 'unpick_all'});
}

function orderPickAll() {
    modify({'action': 'pick_all'});
}

function orderWashAll() {
    modify({'action': 'wash_all'});
}

function unpickItem() {
    modify({'action': 'unpick_item', 'item': $(this).parent().data('id')});
}

function pickItem() {
    modify({'action': 'pick_item', 'item': $(this).parent().data('id')});
}

function washItem() {
    modify({'action': 'wash_item', 'item': $(this).parent().data('id')});
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
    .on('click', '#order-unpick-all', orderUnpickAll)
    .on('click', '#order-pick-all', orderPickAll)
    .on('click', '#order-wash-all', orderWashAll)
    .on('click', '.unpick-item', unpickItem)
    .on('click', '.pick-item', pickItem)
    .on('click', '.wash-item', washItem)
    .on('click', '#order-delete', orderDelete)
    .on('click', '#order-print', orderPrint);
