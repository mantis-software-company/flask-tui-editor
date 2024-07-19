function initializeToastUIEditor(fieldId, hiddenInputId, extented_options) {

    if(window.editors === undefined){
        window.editors = {}
    }

    let options = {
        el: document.querySelector(`#${fieldId}`),
        height: 'auto',
        initialEditType: 'wysiwyg',
        previewStyle: 'vertical',
        initialValue: document.querySelector(`#${hiddenInputId}`).value,
        events: {
            change: function (mode) {
                setTimeout(function () {
                    document.querySelector(`#${hiddenInputId}`).value = window.editors[fieldId].getMarkdown();
                }, 200);
            }
        },
    }

    window.editors[fieldId] = new toastui.Editor({...options, ...extented_options});
}