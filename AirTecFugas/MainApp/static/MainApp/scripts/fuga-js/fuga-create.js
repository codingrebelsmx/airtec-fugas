const ID_HIDDEN_FIELD_URL_AREA = "UrlApiAreaListSelect";
const ID_HIDDEN_FIELD_URL_MACHINE = "UrlApiMaquinaListSelect";
const ID_HIDDEN_FIELD_URL_LOCATION = "UrlApiUbicacionListSelect";
const ID_HIDDEN_FIELD_URL_CATEGORY = "UrlApiCategoriaListSelect";
const ID_HIDDEN_FIELD_URL_SUGGESTION = "UrlApiRecomendacionFugaListSelect";

var globalAction = "";

$(document).ready(function () {
    InitSelects();
    InitModalEvents();
    InitForm("idFormCreateFuga", function () {
        LimpiarControles();
    });
});

function LimpiarControles() {
    InitSelects();
    $("#id_refacciones_comentarios").val("");
    $("#id_nadp").removeAttr("checked");
}


function InitSelects() {
    $("#id_area").off("change");
    $("#id_area").empty();
    $("#id_maquina").empty();
    $("#id_maquina").append('<option value="">Selecciona una máquina...</option>');
    $("#id_ubicacion").empty();
    $("#id_categoria").empty();
    $("#id_recomendacion").empty();

    DownloadFromApiToSelect("id_area", $("#" + ID_HIDDEN_FIELD_URL_AREA).val(), "Selecciona una área...");
    // EventHandler OnChange Cliente's Select
    $("#id_area").on("change", function () {
        if ($(this).val() != null && $(this).val() != "") {
            $("#id_maquina").attr("disabled", "disabled");
            DownloadFromApiToSelect("id_maquina", $("#" + ID_HIDDEN_FIELD_URL_MACHINE).val().replace("0", $("#id_area").val()),
                "Selecciona una máquina...", function () {
                    $("#id_maquina").removeAttr("disabled");
                });
        }
        else {
            var $objSelect = $("#id_maquina");
            $objSelect.empty();
            $objSelect.append('<option value="">' + "Selecciona una máquina..." + '</option>');
        }
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
                    globalAction = action;
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
    if (globalAction == "AddNewArea")
        DownloadFromApiToSelect("id_area", $("#" + ID_HIDDEN_FIELD_URL_AREA).val(), "Selecciona una área...");
    if (globalAction == "AddNewMachine") {
        let idArea = $("#id_area").val();
        if (idArea != undefined && idArea != null && idArea != "")
            $("#id_area").trigger("change");
        //DownloadFromApiToSelect("id_maquina", $("#" + ID_HIDDEN_FIELD_URL_MACHINE).val().replace("0", $("#id_area").val()), "Selecciona una máquina...");
    }
    //DownloadFromApiToSelect("id_cliente", $("#idUrlApiEmpresaListSelect").val(), "Selecciona un Cliente...");
}

