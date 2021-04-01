$(function () {
    $(document).ready(function () {
        var laneCountTable = $('#playerLaneCountTable').DataTable({
            "ajax": $('#playerLaneCountTable').data('url'),
            "columns": [{
                    "data": "lane"
                },
                {
                    "data": "playCount"
                }
            ],
            paging: false,
            searching: false,
            info: false,
            "order": [[1, "desc"]]
        });

    });

});