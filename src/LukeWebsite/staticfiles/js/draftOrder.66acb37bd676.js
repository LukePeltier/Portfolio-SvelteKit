$(function () {
    $(document).ready(function () {
        var playtimeTable = $('#averageDraftOrderTable').DataTable({
            "ajax": $('#averageDraftOrderTable').data('url'),
            "columns": [{
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "data": "draftOrder"
                },
                {
                    "data": "playerID"
                }
            ],
            columnDefs: [{
                targets: [2],
                visible: false
            }],
            paging: false,
            searching: false,
            info: false
        });

    });

});