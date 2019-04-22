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


function InitModalEvents() {
    $('#genericModal').on('show.bs.modal', function (e) {
        $LoadingBlockUI.fadeIn(750);
        var url = $(e.relatedTarget).data("url");
        var action = $(e.relatedTarget).data("action");
        if (url != undefined && url != null) {
            $("#GenericModalBody").load(url, function (response, status, xhr) {
                if (status != "error") {
                    if (action == "EditFugaCorregida")
                        InitForm("idFormCorregirUpdateFuga", AlwaysCallBackAfterFormHasBeenSent, function () {
                            $LoadingBlockUI.fadeIn(750);
                            window.location = "/fuga/list/";
                        });
                    else if (action == "DeleteFugaCorregida")
                        InitForm("idFormFugaDelete", AlwaysCallBackAfterFormHasBeenSent, function () {
                            $LoadingBlockUI.fadeIn(750);
                            window.location = "/fuga/list/";
                        });
                    else if (action == "ExportCSVFuga") {
                        InitForm("idFormExportCSVFugas", AlwaysCallBackAfterFormHasBeenSent, function () {
                            //$LoadingBlockUI.fadeIn(750);
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
}


