$(document).ready(function () {
    ajax_chat_message_loading();
    id_chat_message_form_loading();
});

function ajax_chat_message_loading() {
    $('#id_chat_message_list').load("{% url 'discussions:discussion_post' discussion_id %}", refreshForm1);
    setTimeout("ajax_chat_message_loading()", 5000);
}

function id_chat_message_form_loading() {
    $('#id_chat_message_form').load("{% url 'discussions:discussion_post_form' %}", refreshForm);
}

function refreshForm() {
    $("#ChatMessageForm").on("submit", function (event) {
        event.preventDefault();

        var time = new Date();
        var new_date = time.getFullYear() + '-' + add0(time.getMonth() + 1) + '-' + add0(time.getDate()) + ' ' + add0(time.getHours()) + ':' + add0(time.getMinutes()) + ':' + add0(time.getSeconds());
        document.getElementById("time").value = new_date;

        $.ajax({
            data: $(this).serialize(),
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            success: function (response) {
                console.log(response.success)
                id_chat_message_form_loading();
            },
            error: function (data) {
                // @Todo
            }
        });
    });
}

function refreshForm1() {
    $(".DeleteFormClass").on("submit", function (event) {
        event.preventDefault();

        $.ajax({
            data: $(this).serialize(),
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            success: function (response) {
                console.log(response.success)
                $('#id_chat_message_list').load("{% url 'discussions:discussion_post' discussion_id %}", refreshForm1);
            },
            error: function (data) {
                // @Todo
            }
        });
    });
}

function add0(m) {
    return m < 10 ? '0' + m : m
}

function botton_click() {
    var time = new Date();
    var new_date = time.getFullYear() + '-' + add0(time.getMonth() + 1) + '-' + add0(time.getDate()) + ' ' + add0(time.getHours()) + ':' + add0(time.getMinutes()) + ':' + add0(time.getSeconds());

    document.getElementById("time").value = new_date;
    document.getElementById("ChatMessageForm").submit()
}

function GetRequest() {
    var url = location.search;
    $("#success").load(url);
    console.log("hello");
    self.location = document.referrer;
    return false;
}


