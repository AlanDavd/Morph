/* Project specific Javascript goes here. */

$().ready(function() {
    $("#bulkBtn").click(function() {
        if (confirm("Are you sure you want to delete these records?")) {
            var id = []
            var csrf = $("input[name=csrfmiddlewaretoken]").val()
            $(":checkbox:checked").each(function(i) {
                id[i] = $(this).val()
            })
            id.filter(it => it !== 'on')
            if (id.length === 0) {
                alert("Please select elements")
            } else {
                $.ajax({
                    url: "",
                    method: "POST",
                    data: {
                        id,
                        'csrfmiddlewaretoken': csrf,
                    },
                    success: function(response) {
                        $('#content').html(response)
                        location.reload()
                    }
                })
            }
        }
    })
})
