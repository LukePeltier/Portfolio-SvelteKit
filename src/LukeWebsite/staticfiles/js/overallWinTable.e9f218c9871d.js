$(function () {
$(document).ready( function () {
    $('#overallWinrateTable').DataTable({
        "ajax": $('#overallWinrateTable').data('url'),
        "columns": [
            {"data": "name"},
            {"data": "top"},
            {"data": "jungle"},
            {"data": "mid"},
            {"data": "bot"},
            {"data": "supp"},
            {"data": "overall"}
        ]
    });
} );

});