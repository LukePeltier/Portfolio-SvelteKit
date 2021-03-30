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
        ],
        columnDefs: [
            { type: 'percent', targets: [1,2,3,4,5,6]}
        ],
        paging: false,
        searching: false,
        info: false
    });
} );

$('#overallWinrateTable').hottie()

});