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
                        InitFormExportFugas("idFormExportCSVFugas", AlwaysCallBackAfterFormHasBeenSent, function () {
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


function InitFormExportFugas(idForm, alwaysCallBack) {
    var $form = $("#" + idForm);
    $form.submit(function (event) {
        $LoadingBlockUI.fadeIn(750);
        event.preventDefault();
        var formData = new FormData(this);

        $.ajax({
            url: $form.attr("action"),
            method: $form.attr("method"),
            data: formData,
            cache: false,
            contentType: false,
            processData: false,
            success: function (data) {
                var hiddenElement = document.createElement('a');
                hiddenElement.href = 'data:text/csv;charset=utf-8,%EF%BB%BF\uFEFF' + data;
                hiddenElement.target = '_blank';
                hiddenElement.download = 'fugas.csv';
                hiddenElement.click();
                //return data;
            }
        })
            //.done(function (data, textStatus, jqXHR) {
            //if (textStatus == "success") {
            //    Swal.fire({
            //        'title': "Operación Exitosa!",
            //        'text': "Se exportaron los datos correctamente correctamente.",
            //        'type': "success",
            //        'onClose': function () {
            //            return data;
            //        }
            //    });
            //} else {
            //    Swal.fire({
            //        'title': 'Error',
            //        'text': "Hubo un error.",
            //        'type': 'error'
            //    });
            //}
            //})
            .fail(function (jqXHR, textStatus) {
                if (jqXHR.status == 403) {
                    text = 'No cuenta con los permisos para realizar esta operación.';
                } else {
                    text = "Ha ocurrido un problema al intentar realizar la operación. Intente de nuevo.";
                }
                Swal.fire({
                    'title': 'Advertencia',
                    'text': text,
                    'type': 'warning'
                });
            }).always(function () {
                $LoadingBlockUI.fadeOut(750);
                if (alwaysCallBack != null)
                    alwaysCallBack();
            });
    });
}


function AlwaysCallBackAfterFormHasBeenSent() {
    $('#genericModal').modal('hide');
}


