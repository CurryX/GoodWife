var items = [];
var selected = -1;
var dummyItem = {name: '', count: 1, unitPrice: 0, tags: '', comment: ''};

function showItemList() {
    $('#items').empty();
    var totalCount = 0;
    var totalPrice = 0;
    $(items).each(function (index, item) {
        totalCount += item.count;
        totalPrice += item.unitPrice * item.count;
        var html =
            '<div class="card-item" id="card-item-' + index + '" data-id="' + index + '">\n' +
            '    <button type="button" class="close card-remove">&times;</button>\n' +
            '    <div class="pull-left"><strong>' + item.name + '</strong></div>\n' +
            '    <div class="pull-right">' + item.count + '&nbsp;&times;&nbsp;&yen;' + item.unitPrice + '</div>\n' +
            '    <div class="clearfix"></div>\n' +
            '    <div>' + item.tags + '</div>\n' +
            '</div>';
        $('#items').append(html);
    });
    $('#total-count').html(totalCount + '件');
    $('#total-price').html('&yen;' + totalPrice);
}

function showItemDetail() {
    var editing = selected >= 0;
    var item = editing ? items[selected] : dummyItem;
    $('#edit-name').val(item.name);
    $('#edit-count').val(item.count);
    $('#edit-unit-price').val(item.unitPrice);
    $('#edit-tags').val(item.tags);
    $('#edit-comment').val(item.comment);
}

function updateSelection() {
    $('.card-item').removeClass('bg-info');
    if (selected >= 0) {
        $('#add-item').removeClass('btn-info').addClass('btn-default');
        $('#card-item-' + selected).addClass('bg-info');
    } else {
        $('#add-item').removeClass('btn-default').addClass('btn-info');
    }
    showItemDetail();
}

function addItemClicked() {
    selected = -1;
    updateSelection();
}

function cardItemClicked() {
    selected = parseInt($(this).parent().data('id'));
    updateSelection();
}

function documentReady() {
    showItemList();
    addItemClicked();
}

$(document)
    .ready(documentReady)
    .on('click', '#add-item', addItemClicked)
    .on('click', '.card-item', cardItemClicked);
