const ID_HIDDEN_FIELD_URL_EMPRESA = "idUrlApiEmpresaListSelect";
const ID_HIDDEN_FIELD_URL_PLANTA = "idUrlApiPlantaListSelect";


$(document).ready(function () {
    InitSelects();
});

function InitSelects() {
    DescargaApiSelect("id_cliente", $("#idUrlApiEmpresaListSelect").val(), null);

    // EventHandler OnChange Cliente's Select
    $("#id_cliente").on("change", function () {
        DescargaApiSelect("id_planta", $("#idUrlApiPlantaListSelect").val().replace("0", $("#id_cliente").val()), null);
    });
}

function DescargaApiSelect(idSelect, theURL, callbackOnChange) {
    var $objSelect = $("#" + idSelect);
    $.ajax({
        type: "POST",
        url: theURL,
    }).done(function (data, textStatus, jqXHR) {
        if (data != undefined) {
            console.log(data);
        } else {
            Swal.fire(
                'Advertencia',
                "error ajax data",
                'error'
            );
        }
    }).fail(function (jqXHR, textStatus) {
        if (jqXHR.status == 403) {
            text = 'No cuenta con los permisos para realizar esta operación.';
        } else {
            text = "Ha ocurrido un problema al intentar realizar la operación. Intente de nuevo.";
        }
        Swal.fire(
            'Advertencia',
            text,
            'warning'
        );
    }).always(function () {
        //HideContentLoading();
        //BlockWaitingSelector(false, $form.selector);
    });
}