$(function () {
    var color = Chart.helpers.color;
    window.chartColors = {
        red: 'rgb(255, 99, 132)',
        orange: 'rgb(255, 159, 64)',
        yellow: 'rgb(255, 205, 86)',
        green: 'rgb(92, 184, 92)',
        blue: 'rgb(54, 162, 235)',
        purple: 'rgb(153, 102, 255)',
        grey: 'rgb(201, 203, 207)',
        white: 'rgb(255, 255, 255)'
    };
    $(document).ready(function () {
        var playtimeTable = $('#overallPlaytimeTable').DataTable({
            "ajax": $('#overallPlaytimeTable').data('url'),
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
                    $(this.node()).css('background-color', getRGBHeatmapColor(this.data(), window.chartColors.white, window.chartColors.green, window.chartColors.yellow, 1, false, 0, 50, maxNum));
                }
            });
        });

    });

});