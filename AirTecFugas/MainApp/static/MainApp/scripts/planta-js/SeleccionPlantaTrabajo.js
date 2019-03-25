const ID_HIDDEN_FIELD_URL_EMPRESA = "idUrlApiEmpresaListSelect";
const ID_HIDDEN_FIELD_URL_PLANTA = "idUrlApiPlantaListSelect";


$(document).ready(function () {
    InitSelects();
});

function InitSelects() {
    DescargaApiSelect("id_cliente", $("#idUrlApiEmpresaListSelect").val(), "Selecciona un Cliente...");

    // EventHandler OnChange Cliente's Select
    $("#id_cliente").on("change", function () {
        DescargaApiSelect("id_planta", $("#idUrlApiPlantaListSelect").val().replace("0", $("#id_cliente").val()), "Selecciona una planta...");
    });
}

function DescargaApiSelect(idSelect, theURL, emptyLabel) {
    var $objSelect = $("#" + idSelect);
    $objSelect.empty();
    $objSelect.append('<option value="">' + emptyLabel + '</option>');
    $.ajax({
        type: "GET",
        url: theURL,
    }).done(function (data, textStatus, jqXHR) {
        if (data != undefined) {
            if (data.length > 0) {
                data.map(function (obj, index) {
                    $objSelect.append('<option value="' + obj.id + '">' + obj.nombre + '</option>');
                });
            }
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