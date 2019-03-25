var csrftoken = getCookie("csrftoken");

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


