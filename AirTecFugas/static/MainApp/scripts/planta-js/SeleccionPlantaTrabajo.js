const ID_HIDDEN_FIELD_URL_EMPRESA = "idUrlApiEmpresaListSelect";
const ID_HIDDEN_FIELD_URL_PLANTA = "idUrlApiPlantaListSelect";


$(document).ready(function () {
    InitSelects();
    InitModalEvents();
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


function InitModalEvents() {
    $('#genericModal').on('show.bs.modal', function (e) {
        var url = $(e.relatedTarget).data("url");
        var action = $(e.relatedTarget).data("action");

        if (url != undefined && url != null) {
            $("#GenericModalBody").load(url, function (response, status, xhr) {
                if (status != "error") {
                    if (action == "AddNewCustomer") {
                        InitForm("createEmpresaForm", AlwaysCallBackAfterFormHasBeenSent);
                    }
                    else if (action == "AddNewPlant") {
                        InitForm("createPlantaForm", AlwaysCallBackAfterFormHasBeenSent);
                    }
                }
                else {
                    Swal.fire(
                        'Error',
                        "Ups! hubo un error en el servidor... Servicio no disponible por el momento.",
                        'error'
                    );
                }
            });
        }
    });
}

function AlwaysCallBackAfterFormHasBeenSent() {
    $('#genericModal').modal('hide');
    InitSelects();
}

function InitForm(idForm, alwaysCallBack) {
    var $form = $("#" + idForm);
    $form.submit(function (event) {
        event.preventDefault();
        var formData = new FormData(this);

        $.ajax({
            url: $form.attr("action"),
            method: $form.attr("method"),
            data: formData,
            cache: false,
            contentType: false,
            processData: false
        }).done(function (data, textStatus, jqXHR) {
            if (textStatus == "success") {
                Swal.fire("Operación Exitosa!", "Se registró correctamente.", "success");
            } else {
                Swal.fire(
                    'Error',
                    "Hubo un error y no se regitró.",
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
            alwaysCallBack();
            //HideContentLoading();
            //BlockWaitingSelector(false, $form.selector);
        });
    });
}


function InitFormCreateEmpresa() {
    var $form = $("#createEmpresaForm");
    $form.submit(function (event) {
        event.preventDefault();
        var formData = new FormData(this);

        $.ajax({
            url: $form.attr("action"),
            method: $form.attr("method"),
            data: formData,
            cache: false,
            contentType: false,
            processData: false
        }).done(function (data, textStatus, jqXHR) {
            if (textStatus == "success") {
                Swal.fire("Operación Exitosa!", "Se registró correctamente el nuevo Cliente", "success");
            } else {
                Swal.fire(
                    'Error',
                    "Hubo un error y no se regitró el nuevo cliente.",
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
    });
}


function InitFormCreatePlanta() {
    var $form = $("#createPlantaForm");
    $form.submit(function (event) {
        event.preventDefault();
    });
}