$(function () {
    $(document).ready(function () {
        window.chartColors = {
            red: 'rgb(255, 99, 132)',
            orange: 'rgb(255, 159, 64)',
            yellow: 'rgb(255, 205, 86)',
            green: 'rgb(92, 184, 92)',
            blue: 'rgb(54, 162, 235)',
            purple: 'rgb(153, 102, 255)',
            grey: 'rgb(201, 203, 207)',
            white: 'rgb(255, 255, 255)',
            redTransparent: 'rgb(255, 99, 132, 0.2)',
            orangeTransparent: 'rgb(255, 159, 64, 0.2)',
            yellowTransparent: 'rgb(255, 205, 86, 0.2)',
            greenTransparent: 'rgb(92, 184, 92, 0.2)',
            blueTransparent: 'rgb(54, 162, 235, 0.2)',
            purpleTransparent: 'rgb(153, 102, 255, 0.2)',
            greyTransparent: 'rgb(201, 203, 207, 0.2)',
            whiteTransparent: 'rgb(255, 255, 255, 0.2)'
        };
        var powerRankings = $('#powerRankingsTable').DataTable({
            "ajax": $('#powerRankingsTable').data('url'),
            "columns": [
                {
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "data": "tournamentsPlayed"
                },
                {
                    "data": "holesPlayed"
                },
                {
                    "data": "topPercent"
                },
                {
                    "data": "topPercentAlpha"
                },
                {
                    "data": "playerID"
                }
            ],
            columnDefs: [{
                    type: "natural",
                    targets: [3],
                    createdCell: function (td, cellData, rowData, row, col) {
                        $(td).attr('data-alpha', powerRankings.cell(row, col+1).data())
                    }
                },
                {
                    targets: [4,5],
                    visible: false
                }
            ],
            paging: false,
            searching: false,
            info: false,
            "order": [
                [3, "asc"]
            ]
        });

        powerRankings.on('draw', function () {
            powerRankings.cells().every(function () {
                if ($(this.node()).parent().children().index($(this.node()))===3) {
                    $(this.node()).css('background-color', getRGBHeatmapColor(100-this.data(), window.chartColors.red, window.chartColors.green, window.chartColors.yellow, $(this.node()).data('alpha'), true, 0, 50, 100));
                } else if (this.data() === "N/A") {
                    $(this.node()).css('color', window.chartColors.grey);
                }
            });
        });

    });

});