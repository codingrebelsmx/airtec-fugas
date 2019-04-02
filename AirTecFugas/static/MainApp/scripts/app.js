var csrftoken = getCookie("csrftoken");
var $LoadingBlockUI = $("#loading-wrapper");

/**
 * AJUSTES Y PLUGINS
 */
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


/**
 * UTILERIAS
 */
function getCookie(a) {
    var c = null;
    if (document.cookie && "" != document.cookie) {
        for (var d = document.cookie.split(";"), b = 0; b < d.length; b++) {
            var e = jQuery.trim(d[b]);
            // Does this cookie string begin with the name we want?
            if (e.substring(0, a.length + 1) == a + "=") {
                c = decodeURIComponent(e.substring(a.length + 1));
                break;
            }
        }
    }
    return c;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// ---------------- ------ ------- ----------------
// ---------------- COMMON METHODS ----------------

// Inicializa un formulario para ser enviado por ajas según sus
// propios atributos

function InitForm(idForm, alwaysCallBack, onCloseModalCallBack) {
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
            processData: false
        }).done(function (data, textStatus, jqXHR) {
            if (textStatus == "success") {
                Swal.fire({
                    'title': "Operación Exitosa!",
                    'text': "Se registró correctamente.",
                    'type': "success",
                    'onClose': function () {
                        if (onCloseModalCallBack != undefined && onCloseModalCallBack != null)
                            onCloseModalCallBack();
                    }
                });
            } else {
                Swal.fire({
                    'title': 'Error',
                    'text': "Hubo un error y no se regitró.",
                    'type': 'error',
                    'onClose': function () {
                        if (onCloseModalCallBack != undefined && onCloseModalCallBack != null)
                            onCloseModalCallBack();
                    }
                });
            }
        }).fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 403) {
                text = 'No cuenta con los permisos para realizar esta operación.';
            } else {
                text = "Ha ocurrido un problema al intentar realizar la operación. Intente de nuevo.";
            }
            Swal.fire({
                'title': 'Advertencia',
                'text': text,
                'type': 'warning',
                'onClose': function () {
                    if (onCloseModalCallBack != undefined && onCloseModalCallBack != null)
                        onCloseModalCallBack();
                }
            });
        }).always(function () {
            $LoadingBlockUI.fadeOut(750);
            if (alwaysCallBack != null)
                alwaysCallBack();
        });
    });
}

// Descarga datos de una API para ser incrustados como opciones de un select

function DownloadFromApiToSelect(idSelect, theURL, emptyLabel, alwaysCallBack) {
    var $objSelect = $("#" + idSelect);
    var defaultValue = $objSelect.data("value");
    $objSelect.empty();
    $objSelect.append('<option value="">' + emptyLabel + '</option>');


    $.ajax({
        type: "GET",
        url: theURL,
    }).done(function (data, textStatus, jqXHR) {
        if (data != undefined) {
            if (data.length > 0) {
                data.map(function (obj, index) {

                    let strOption = '<option value="' + obj.id + '" ' + ReturnSelectedAttr(defaultValue) + '>';
                    strOption += (obj.nombre + '</option>');
                    $objSelect.append(strOption);
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
        if (alwaysCallBack != undefined && alwaysCallBack != null)
            alwaysCallBack();
    });
}

function ReturnSelectedAttr(defaultValue) {
    let strSelected = "";

    if (defaultValue != undefined && defaultValue != null && defaultValue != "") {
        strSelected = "selected";
    }

    return strSelected;
}