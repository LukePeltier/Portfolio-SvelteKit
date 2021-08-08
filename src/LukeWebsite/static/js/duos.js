$(function () {
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


    $(document).ready(function () {
        var duoGamesTable = $('#duoGamesTable').DataTable({
            "ajax": $('#duoGamesTable').data('url'),
            "columns": [{
                    "data": "gameNum",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/game/" + oData.gameID + "'>" + sData + "</a>");
                    }
                },
                {
                    "data": "leftchampion",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        if (oData.leftriotChampionName != undefined) {
                            $(nTd).html("<a href='/ten_mans/champion/" + oData.leftchampionID + "'>" + sData + " <img src='https://ddragon.leagueoflegends.com/cdn/" + oData.championVersion + "/img/champion/" + oData.leftriotChampionName + ".png' style='width:20px; height:20px;'/> " + "</a>");
                        }


                    }

                },
                {
                    "data": "leftcs"
                },
                {
                    "data": "leftkda",
                    "render": $.fn.dataTable.render.text()
                },
                {
                    "data": "leftlane",
                    "render": $.fn.dataTable.render.text()
                },
                {
                    "data": "leftwinLoss",
                    "render": $.fn.dataTable.render.text()
                },
                {
                    "data": "rightlane",
                    "render": $.fn.dataTable.render.text()
                },
                {
                    "data": "rightkda",
                    "render": $.fn.dataTable.render.text()
                },

                {
                    "data": "rightcs"
                },
                {
                    "data": "rightchampion",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        if (oData.rightriotChampionName != undefined) {
                            $(nTd).html("<a href='/ten_mans/champion/" + oData.rightchampionID + "'> <img src='https://ddragon.leagueoflegends.com/cdn/" + oData.championVersion + "/img/champion/" + oData.rightriotChampionName + ".png' style='width:20px; height:20px;'/> " + sData + "</a>");
                        }


                    }

                },
                {
                    "data": "gameID"
                },
                {
                    "data": "leftchampionID"
                },
                {
                    "data": "leftriotChampionName"
                },
                {
                    "data": "rightchampionID"
                },
                {
                    "data": "rightriotChampionName"
                },
                {
                    "data": "championVersion"
                },
                {
                    "data": "highlightRow"
                }
            ],
            columnDefs: [
                {
                    targets: [10, 11, 12, 13, 14, 15, 16],
                    visible: false
                },
                {
                    targets: [1, 2, 3, 4],
                    className: 'text-end'
                },
                {
                    targets: 5,
                    className: 'text-end rightBorder leftBorder'
                },
                {
                    targets: [0],
                    className: 'rightBorder'
                },
            ],
            paging: false,
            searching: false,
            info: false,
            "order": [
                [0, "asc"]
            ],
            "scrollX": true,
            "createdRow": function (row, data, dataIndex) {
                if (data.highlightRow == true) {
                    $(row).addClass('yellowRow');
                }
            }
        });
    });
});