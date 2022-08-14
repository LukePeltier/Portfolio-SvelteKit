$(function () {
    $(document).ready(function () {
        var playtimeTable = $('#overallPlaytimeTable').DataTable({
            "ajax": $('#overallPlaytimeTable').data('url') + location.search,
            "columns": [
                {
                    "className": "stat-right stat-leftcol-border",
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
                    "data": "playerID"
                }
            ],
            columnDefs: [{
                    type: "natural",
                    targets: [1, 2, 3, 4, 5, 6]
                },
                {
                    targets: [7],
                    visible: false
                }
            ],
            paging: false,
            searching: false,
            info: false
        });

        playtimeTable.on('draw', function () {
            var values = playtimeTable.column(6).data().toArray();
            var maxNum = Math.max(...values);
            playtimeTable.cells().every(function () {
                if (typeof (this.data()) === "number") {
                    $(this.node()).css('background-color', getRGBHeatmapColorFromHex(this.data(), getComputedStyle(document.documentElement).getPropertyValue('--tenmanswhite'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansyellow'), 1, false, 0, 50, maxNum));
                }
            });
        });

    });

});