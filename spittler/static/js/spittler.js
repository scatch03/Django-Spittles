function shakeIt() {
    var counter = 0;
    $(".ui-widget-content").each(function () {
        scheduleAction(600 * counter++, $(this));
    });

    setTimeout(shakeIt, 8000)
}

function scheduleAction(time, object) {
    var action = function () {
        object.effect(Math.random() > 0.5 ? 'bounce' : 'shake', {}, 500, null);
    };

    setTimeout(action, time);
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    var host = document.location.host;
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        !(/^(\/\/|http:|https:).*/.test(url));
}

function deleteSpittle(id) {
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend:function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $("#item-" + id).fadeOut(500, function () {
        $(this).remove();
    });

    $.ajax({
        url:"/spittler/delete/" + id,
        type:"post",
        success:function (response, textStatus, jqXHR) {
            document.location = '/spittler/spittlers/';
        },
        error:function (jqXHR, textStatus, errorThrown) {
            alert('Error occurred while deleting spittle!');
        },
        complete:function () {
        }
    });

}
