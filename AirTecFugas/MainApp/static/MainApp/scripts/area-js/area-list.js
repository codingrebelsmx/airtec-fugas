const ID_HIDDEN_FIELD_URL_PLANTA = "idUrlApiPlantaListSelect";

$(document).ready(
    function () {
        InitDataTable();
        InitModalEvents();
    });


function InitDataTable() {

    $('#TableFugaList').DataTable({
        'iDisplayLength': 10,
    });
}

function InitSelectsModalPartialEditArea() {
    $("#id_planta").empty();

    DownloadFromApiToSelect("id_planta", $("#" + ID_HIDDEN_FIELD_URL_PLANTA).val(), "Selecciona una planta...");
}


function InitModalEvents() {
    $('#genericModal').on('show.bs.modal', function (e) {
        $LoadingBlockUI.fadeIn(750);
        var url = $(e.relatedTarget).data("url");
        var action = $(e.relatedTarget).data("action");
        if (url != undefined && url != null) {
            $("#idModalContent").load(url, function (response, status, xhr) {
                if (status != "error") {
                    if (action == "EditArea") {
                        InitSelectsModalPartialEditArea();
                        InitForm("idFormPartialEditArea", AlwaysCallBackAfterFormHasBeenSent, function () {
                            $LoadingBlockUI.fadeIn(750);
                            window.location = $("#idUrlAreaList").val();
                        });
                    }
                    else if (action == "DeleteArea") {
                        InitForm("idFormDeleteArea", AlwaysCallBackAfterFormHasBeenSent, function () {
                            $LoadingBlockUI.fadeIn(750);
                            window.location = $("#idUrlAreaList").val();
                        });
                    }
                    globalAction = action;
                }
                else {
                    Swal.fire(
                        'Error',
                        "Ups! hubo un error en el servidor... Servicio no disponible por el momento.",
                        'error'
                    );
                }
                $LoadingBlockUI.fadeOut(750);
            });
        }
    });
}


function AlwaysCallBackAfterFormHasBeenSent() {
    $('#genericModal').modal('hide');
    $LoadingBlockUI.fadeOut(750);
}


