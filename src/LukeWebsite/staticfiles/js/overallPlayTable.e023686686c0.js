$(function () {
    $(document).ready(function () {
        var winrateTable = $('#overallWinrateTable').DataTable({
            "ajax": $('#overallWinrateTable').data('url'),
            "columns": [{
                    "data": "name"
                },
                {
                    "data": "top"
                },
                {
                    "data": "jungle"
                },
                {
                    "data": "mid"
                },
                {
                    "data": "bot"
                },
                {
                    "data": "supp"
                },
                {
                    "data": "overall"
                },
                {
                    "data": "topAlpha"
                },
                {
                    "data": "jungleAlpha"
                },
                {
                    "data": "midAlpha"
                },
                {
                    "data": "botAlpha"
                },
                {
                    "data": "suppAlpha"
                },
                {
                    "data": "overallAlpha"
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
                    targets: [7,8,9,10,11,12],
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
                    $(this.node()).css('background-color', getRGBHeatmapColor(this.data(), window.chartColors.red, window.chartColors.green, window.chartColors.yellow, $(this.node()).data('alpha'), true, 0, 50, 100));
                } else if (this.data() === "N/A") {
                    $(this.node()).css('color', window.chartColors.grey);
                }
            });
        });

    });

});