$(function () {
    $(document).ready(function () {
        var averageDraftOrderTable = $('#averageDraftOrderTable').DataTable({
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
            "order": [
                [1, "asc"]
            ],
            paging: false,
            searching: false,
            info: false
        });

        var expectedDraftOrderTable = $('#expectedDraftOrderWinrateTable').DataTable({
            "ajax": $('#expectedDraftOrderWinrateTable').data('url'),
            "columns": [{
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "data": "minWinrate",
                    "render": $.fn.dataTable.render.number(',', '.', 0, '', '%')
                },
                {
                    "data": "playerID"
                }
            ],
            columnDefs: [{
                targets: [2],
                visible: false
            }],
            "order": [
                [1, "desc"]
            ],
            paging: false,
            searching: false,
            info: false
        });

        var expectedDraftOrderTopTable = $('#expectedDraftOrderWinrateTopTable').DataTable({
            "ajax": $('#expectedDraftOrderWinrateTopTable').data('url'),
            "columns": [{
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "data": "minWinrate",
                    "render": $.fn.dataTable.render.number(',', '.', 0, '', '%')
                },
                {
                    "data": "playerID"
                }
            ],
            columnDefs: [{
                targets: [2],
                visible: false
            }],
            "order": [
                [1, "desc"]
            ],
            paging: false,
            searching: false,
            info: false
        });

        var expectedDraftOrderJungTable = $('#expectedDraftOrderWinrateJungTable').DataTable({
            "ajax": $('#expectedDraftOrderWinrateJungTable').data('url'),
            "columns": [{
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "data": "minWinrate",
                    "render": $.fn.dataTable.render.number(',', '.', 0, '', '%')
                },
                {
                    "data": "playerID"
                }
            ],
            columnDefs: [{
                targets: [2],
                visible: false
            }],
            "order": [
                [1, "desc"]
            ],
            paging: false,
            searching: false,
            info: false
        });

        var expectedDraftOrderMidTable = $('#expectedDraftOrderWinrateMidTable').DataTable({
            "ajax": $('#expectedDraftOrderWinrateMidTable').data('url'),
            "columns": [{
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "data": "minWinrate",
                    "render": $.fn.dataTable.render.number(',', '.', 0, '', '%')
                },
                {
                    "data": "playerID"
                }
            ],
            columnDefs: [{
                targets: [2],
                visible: false
            }],
            "order": [
                [1, "desc"]
            ],
            paging: false,
            searching: false,
            info: false
        });

        var expectedDraftOrderBotTable = $('#expectedDraftOrderWinrateBotTable').DataTable({
            "ajax": $('#expectedDraftOrderWinrateBotTable').data('url'),
            "columns": [{
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "data": "minWinrate",
                    "render": $.fn.dataTable.render.number(',', '.', 0, '', '%')
                },
                {
                    "data": "playerID"
                }
            ],
            columnDefs: [{
                targets: [2],
                visible: false
            }],
            "order": [
                [1, "desc"]
            ],
            paging: false,
            searching: false,
            info: false
        });

        var expectedDraftOrderSuppTable = $('#expectedDraftOrderWinrateSuppTable').DataTable({
            "ajax": $('#expectedDraftOrderWinrateSuppTable').data('url'),
            "columns": [{
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "data": "minWinrate",
                    "render": $.fn.dataTable.render.number(',', '.', 0, '', '%')
                },
                {
                    "data": "playerID"
                }
            ],
            columnDefs: [{
                targets: [2],
                visible: false
            }],
            "order": [
                [1, "desc"]
            ],
            paging: false,
            searching: false,
            info: false
        });

    });

});