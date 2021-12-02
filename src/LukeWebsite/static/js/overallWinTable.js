$(function () {
    $(document).ready(function () {
        var winrateTable = $('#overallWinrateTable').DataTable({
            "ajax": $('#overallWinrateTable').data('url'),
            "columns": [
                {
                    "className": "stat-center stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "className": "stat-center stat-inset-border",
                    "data": "top"
                },
                {
                    "className": "stat-center stat-inset-border",
                    "data": "jungle"
                },
                {
                    "className": "stat-center stat-inset-border",
                    "data": "mid"
                },
                {
                    "className": "stat-center stat-inset-border",
                    "data": "bot"
                },
                {
                    "className": "stat-center stat-inset-border",
                    "data": "supp"
                },
                {
                    "className": "stat-center stat-inset-border",
                    "data": "overall"
                },
                {
                    "className": "stat-center stat-inset-border",
                    "data": "topAlpha"
                },
                {
                    "className": "stat-center stat-inset-border",
                    "data": "jungleAlpha"
                },
                {
                    "className": "stat-center stat-inset-border",
                    "data": "midAlpha"
                },
                {
                    "className": "stat-center stat-inset-border",
                    "data": "botAlpha"
                },
                {
                    "className": "stat-center stat-inset-border",
                    "data": "suppAlpha"
                },
                {
                    "className": "stat-center stat-inset-border",
                    "data": "overallAlpha"
                },
                {
                    "className": "stat-center stat-inset-border",
                    "data": "playerID"
                }
            ],
            columnDefs: [{
                    type: "natural",
                    targets: [1, 2, 3, 4, 5, 6],
                    createdCell: function (td, cellData, rowData, row, col) {
                        $(td).attr('data-alpha', winrateTable.cell(row, col+6).data())
                    }
                },
                {
                    targets: [7,8,9,10,11,12,13],
                    visible: false
                }
            ],
            paging: false,
            searching: false,
            info: false
        });

        winrateTable.on('draw', function () {
            winrateTable.cells().every(function () {
                if (typeof (this.data()) === "number") {
                    $(this.node()).css('background-color', getRGBHeatmapColorFromHex(this.data(), getComputedStyle(document.documentElement).getPropertyValue('--tenmansred'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansyellow'), $(this.node()).data('alpha'), true, 0, 50, 100, false));
                } else if (this.data() === "N/A") {
                    $(this.node()).css('color', getComputedStyle(document.documentElement).getPropertyValue('--tenmansgrey'));
                }
            });
        });

    });

});