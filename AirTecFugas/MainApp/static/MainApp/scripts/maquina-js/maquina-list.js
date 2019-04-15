const ID_HIDDEN_FIELD_URL_AREA = "idUrlApiAreaListSelect";

$(document).ready(
    function () {
        InitDataTable();
        InitModalEvents();
    });


function InitDataTable() {

    $('#TableMaquinaList').DataTable({
        'iDisplayLength': 10,
    });
}

function InitSelectsModalPartialEditArea() {
    $("#id_area").empty();

    DownloadFromApiToSelect("id_area", $("#" + ID_HIDDEN_FIELD_URL_AREA).val(), "Selecciona una área...");
}


function InitModalEvents() {
    $('#genericModal').on('show.bs.modal', function (e) {
        $LoadingBlockUI.fadeIn(750);
        var url = $(e.relatedTarget).data("url");
        var action = $(e.relatedTarget).data("action");
        if (url != undefined && url != null) {
            $("#idModalContent").load(url, function (response, status, xhr) {
                if (status != "error") {
                    if (action == "EditMaquina") {
                        InitSelectsModalPartialEditArea();
                        InitForm("idFormPartialEditMaquina", AlwaysCallBackAfterFormHasBeenSent, function () {
                            $LoadingBlockUI.fadeIn(750);
                            window.location = $("#idUrlMaquinaList").val();
                        });
                    }
                    else if (action == "DeleteMaquina") {
                        InitForm("idFormDeleteMaquina", AlwaysCallBackAfterFormHasBeenSent, function () {
                            $LoadingBlockUI.fadeIn(750);
                            window.location = $("#idUrlMaquinaList").val();
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

//function InitModalEvents() {
//    $('#genericModal').on('show.bs.modal', function (e) {
//        $LoadingBlockUI.fadeIn(500);
//        var url = $(e.relatedTarget).data("url");
//        var action = $(e.relatedTarget).data("action");
//        if (url != undefined && url != null) {
//            $("#GenericModalBody").load(url, function (response, status, xhr) {
//                if (status != "error") {
//                    if (action == "AddNewArea")
//                        InitForm("idFormCreateNewArea", AlwaysCallBackAfterFormHasBeenSent);
//                    if (action == "AddNewMachine")
//                        InitForm("idFormCreateNewMachine", AlwaysCallBackAfterFormHasBeenSent);
//                    globalAction = action;
//                }
//                else {
//                    Swal.fire(
//                        'Error',
//                        "Ups! hubo un error en el servidor... Servicio no disponible por el momento.",
//                        'error'
//                    );
//                }
//                $LoadingBlockUI.fadeOut(1000);
//            });
//        }
//    });
//}


function AlwaysCallBackAfterFormHasBeenSent() {
    $('#genericModal').modal('hide');
    $LoadingBlockUI.fadeOut(750);
}


