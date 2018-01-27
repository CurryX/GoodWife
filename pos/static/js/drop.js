var items = [];
var selected = -1;
var dummyItem = {name: '', count: 1, unitPrice: 0, tags: '', comment: ''};
var editName, editTags;

function selectionToString(data) {
    var str = '';
    $(data).each(function () {
        str += this.id + '；'
    });
    return str.length > 0 ? str.slice(0, -1) : '';
}

function stringToSelection(str) {
    if (str === '') return [];
    var data = [];
    $(str.split('；')).each(function () {
        data.push({'id': this, 'name': this});
    });
    return data;
}

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
            '    <div class="pull-right">' + item.count + '&nbsp;&times;&nbsp;￥' + item.unitPrice + '</div>\n' +
            '    <div class="clearfix"></div>\n' +
            '    <div>' + item.tags + '</div>\n' +
            '    <div class="text-muted">' + item.comment + '</div>' +
            '</div>';
        $('#items').append(html);
    });
    $('#total-count').html(totalCount + '件');
    $('#total-price').html('￥' + totalPrice);
}

function showItemDetail() {
    var editing = selected >= 0;
    var item = editing ? items[selected] : dummyItem;
    editName.setSelection(stringToSelection(item.name));
    $('#edit-count').val(item.count);
    $('#edit-unit-price').val(item.unitPrice);
    editTags.setSelection(stringToSelection(item.tags));
    $('#edit-comment').val(item.comment);
}

function updateSelection() {
    showItemList();
    showItemDetail();
    if (selected >= 0) {
        $('#add-item').removeClass('btn-info').addClass('btn-default');
        $('#card-item-' + selected).addClass('bg-info').addClass('card-item-active');
    } else {
        $('#add-item').removeClass('btn-default').addClass('btn-info');
    }
}

function addItemClicked() {
    selected = -1;
    updateSelection();
}

function cardItemClicked() {
    selected = parseInt($(this).data('id'));
    updateSelection();
}

function cardRemoveClicked(event) {
    event.stopPropagation();
    items.splice(parseInt($(this).data('id')), 1);
    selected = -1;
    updateSelection();
}

function editOkClicked() {
    var item;
    if (selected >= 0) item = items[selected];
    else {
        item = {};
        items.push(item);
    }
    item.name = selectionToString(editName.getSelection());
    item.count = parseFloat($('#edit-count').val());
    item.unitPrice = parseFloat($('#edit-unit-price').val());
    item.tags = selectionToString(editTags.getSelection());
    item.comment = $('#edit-comment').val();
    addItemClicked();
}

function editCancelClicked() {
    addItemClicked();
}

function initNameInput(value) {
    editName = $('#edit-name').magicSuggest({
        data: '/get_cloth_names',
        method: 'GET',
        typeDelay: 0,
        maxSelection: 1,
        resultAsString: true,
        placeholder: '',
        infoMsgCls: 'hidden',
        renderer: function(data){
            return data.id + '&nbsp;<small>￥' + data.price + '</small>';
        },
        selectionRenderer: function(data){
            return data.id;
        }
    });
    $(editName).on('selectionchange', function(e, m){
        var data = this.getSelection();
        if (data.length > 0 && data[0].price) $('#edit-unit-price').val(data[0].price);
    });
}

function initTagsInput(value) {
    editTags = $('#edit-tags').magicSuggest({
        data: '/get_tags',
        method: 'GET',
        typeDelay: 0,
        placeholder: '',
        infoMsgCls: 'hidden',
        renderer: function(data){
            return data.id;
        },
        selectionRenderer: function(data){
            return data.id;
        }
    });
}

function documentReady() {
    initNameInput();
    initTagsInput();
    showItemList();
    addItemClicked();
}

$(document)
    .ready(documentReady)
    .on('click', '#add-item', addItemClicked)
    .on('click', '#edit-ok', editOkClicked)
    .on('click', '#edit-cancel', editCancelClicked)
    .on('click', '.card-item', cardItemClicked)
    .on('click', '.card-remove', cardRemoveClicked);
