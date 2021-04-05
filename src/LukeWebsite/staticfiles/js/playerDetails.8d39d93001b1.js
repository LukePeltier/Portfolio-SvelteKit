$(function () {
    $(document).ready(function () {
        var laneCountTable = $('#playerLaneCountTable').DataTable({
            "ajax": $('#playerLaneCountTable').data('url'),
            "columns": [{
                    "data": "lane"
                },
                {
                    "data": "playCount"
                },
                {
                    "data": "averageKDA"
                }
            ],
            paging: false,
            searching: false,
            info: false,
            "order": [[1, "desc"]]
        });

    });

});