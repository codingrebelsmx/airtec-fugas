const ID_HIDDEN_FIELD_URL_AREA = "UrlApiAreaListSelect";
const ID_HIDDEN_FIELD_URL_MACHINE = "UrlApiMaquinaListSelect";
const ID_HIDDEN_FIELD_URL_LOCATION = "UrlApiUbicacionListSelect";
const ID_HIDDEN_FIELD_URL_CATEGORY = "UrlApiCategoriaListSelect";
const ID_HIDDEN_FIELD_URL_SUGGESTION = "UrlApiRecomendacionFugaListSelect";

$(document).ready(function () {
    InitSelects();
    InitModalEvents();
});


function InitSelects() {
    DownloadFromApiToSelect("id_area", $("#" + ID_HIDDEN_FIELD_URL_AREA).val(), "Selecciona una área...");

    // EventHandler OnChange Cliente's Select
    $("#id_area").on("change", function () {
        DownloadFromApiToSelect("id_maquina", $("#" + ID_HIDDEN_FIELD_URL_MACHINE).val().replace("0", $("#id_area").val()), "Selecciona una máquina...");
    });

    DownloadFromApiToSelect("id_ubicacion", $("#" + ID_HIDDEN_FIELD_URL_LOCATION).val(), "Selecciona una ubicación...");
    DownloadFromApiToSelect("id_categoria", $("#" + ID_HIDDEN_FIELD_URL_CATEGORY).val(), "Selecciona una categoría...");
    DownloadFromApiToSelect("id_recomendacion", $("#" + ID_HIDDEN_FIELD_URL_SUGGESTION).val(), "Selecciona una recomendación...");
}


function InitModalEvents() {
    $('#genericModal').on('show.bs.modal', function (e) {
        var url = $(e.relatedTarget).data("url");
        var action = $(e.relatedTarget).data("action");

        if (url != undefined && url != null) {
            $("#GenericModalBody").load(url, function (response, status, xhr) {
                if (status != "error") {
                    if (action == "AddNewArea")
                        InitForm("idFormCreateNewArea", AlwaysCallBackAfterFormHasBeenSent);
                    if (action == "AddNewMachine")
                        InitForm("idFormCreateNewMachine", AlwaysCallBackAfterFormHasBeenSent);
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
    //DownloadFromApiToSelect("id_cliente", $("#idUrlApiEmpresaListSelect").val(), "Selecciona un Cliente...");
}

