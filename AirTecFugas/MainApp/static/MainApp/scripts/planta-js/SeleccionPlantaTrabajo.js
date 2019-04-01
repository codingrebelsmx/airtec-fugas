const ID_HIDDEN_FIELD_URL_EMPRESA = "idUrlApiEmpresaListSelect";
const ID_HIDDEN_FIELD_URL_PLANTA = "idUrlApiPlantaListSelect";


$(document).ready(function () {
    InitSelects();
    InitModalEvents();
});

function InitSelects() {
    DownloadFromApiToSelect("id_cliente", $("#idUrlApiEmpresaListSelect").val(), "Selecciona un Cliente...");

    // EventHandler OnChange Cliente's Select
    $("#id_cliente").on("change", function () {
        $LoadingBlockUI.fadeIn(750);
        $("#id_planta").attr("disabled", "disabled");
        DownloadFromApiToSelect("id_planta", $("#idUrlApiPlantaListSelect").val().replace("0", $("#id_cliente").val())
            , "Selecciona una planta...", function () {
                $("#id_planta").removeAttr("disabled");
                $LoadingBlockUI.fadeOut(1500);
            });
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
    DownloadFromApiToSelect("id_cliente", $("#idUrlApiEmpresaListSelect").val(), "Selecciona un Cliente...");
}

