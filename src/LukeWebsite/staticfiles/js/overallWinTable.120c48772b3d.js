$(function () {
$(document).ready( function () {
    var table = $('#overallWinrateTable').DataTable({
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
    table.cells().every( function() {
        console.log("Checking");
        if(!Number.isNaN(this.data())){
            console.log("Number found");
            this.css('background-color', getRGBHeatmapColor(this.value, window.chartColors.red, window.chartColors.green, window.chartColors.yellow, true, 0, 50, 100));
        }
        else if (this.value === "N/A"){

        }
        else{
            console.log("Not applicable");
        }
    })
} );

});