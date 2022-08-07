$(function () {
    $(document).ready(function () {
        var averageDraftOrderTable = $('#averageDraftOrderTable').DataTable({
            "ajax": $('#averageDraftOrderTable').data('url'),
            "columns": [{
                    "className": "stat-right stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "className": "stat-center stat-inset-border strong-text",
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
                    "className": "stat-right stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "className": "stat-center stat-inset-border strong-text",
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
                    "className": "stat-right stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "className": "stat-center stat-inset-border strong-text",
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
                    "className": "stat-right stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "className": "stat-center stat-inset-border strong-text",
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
                    "className": "stat-right stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "className": "stat-center stat-inset-border strong-text",
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
                    "className": "stat-right stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "className": "stat-center stat-inset-border strong-text",
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
                    "className": "stat-right stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "className": "stat-center stat-inset-border strong-text",
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

        var expectedDraftOrderCaptainTable = $('#expectedDraftOrderWinrateCaptainTable').DataTable({
            "ajax": $('#expectedDraftOrderWinrateCaptainTable').data('url'),
            "columns": [{
                    "className": "stat-right stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "className": "stat-center stat-inset-border strong-text",
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