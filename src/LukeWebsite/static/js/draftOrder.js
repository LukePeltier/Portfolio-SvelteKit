$(function () {
    $(document).ready(function () {
        var playtimeTable = $('#averageDraftOrderTable').DataTable({
            "ajax": $('#averageDraftOrderTable').data('url'),
            "columns": [{
                    "data": "name"
                },
                {
                    "data": "draftOrder"
                }
            ],
            paging: false,
            searching: false,
            info: false
        });

    });

});