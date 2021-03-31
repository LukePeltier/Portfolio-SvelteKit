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
                }
            ],
            columnDefs: [{
                type: "natural",
                targets: [1, 2, 3, 4, 5, 6]
            }],
            paging: false,
            searching: false,
            info: false
        });

        winrateTable.on('draw', function () {
            winrateTable.cells().every(function () {
                if (typeof(this.data())==="number") {
                    $(this.node()).css('background-color', getRGBHeatmapColor(this.data(), window.chartColors.red, window.chartColors.green, window.chartColors.yellow, 1, true, 0, 50, 100));
                } else if (this.data() === "N/A") {
                    $(this.node()).css('color', window.chartColors.grey);
                }
            });
        });

    });

});