$(function () {
    $(document).ready(function () {
        var duoGamesTable = $('#duoGamesTable').DataTable({
            "ajax": $('#duoGamesTable').data('url'),
            "columns": [
                {
                    "className": "stat-center stat-leftcol-border rightBorder",
                    "data": "gameNum",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/game/" + oData.gameID + "'>" + sData + "</a>");
                    }
                },
                {
                    "className": "stat-center stat-inset-border",
                    "data": "leftchampion",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        if (oData.leftriotChampionName != undefined) {
                            $(nTd).html("<a href='/ten_mans/champion/" + oData.leftchampionID + "'>" + sData + " <img src='https://ddragon.leagueoflegends.com/cdn/" + oData.championVersion + "/img/champion/" + oData.leftriotChampionName + ".png' style='width:20px; height:20px;'/> " + "</a>");
                        }


                    }

                },
                {
                    "className": "stat-center stat-inset-border",
                    "data": "leftcs"
                },
                {
                    "className": "stat-center stat-inset-border",
                    "data": "leftkda",
                    "render": $.fn.dataTable.render.text()
                },
                {
                    "className": "stat-center stat-inset-border",
                    "data": "leftlane",
                    "render": $.fn.dataTable.render.text()
                },
                {
                    "className": "stat-center text-center stat-leftcol-border rightBorder leftBorder",
                    "data": "leftwinLoss",
                    "render": $.fn.dataTable.render.text()
                },
                {
                    "className": "stat-center stat-inset-mirror-border",
                    "data": "rightlane",
                    "render": $.fn.dataTable.render.text()
                },
                {
                    "className": "stat-center stat-inset-mirror-border",
                    "data": "rightkda",
                    "render": $.fn.dataTable.render.text()
                },

                {
                    "className": "stat-center stat-inset-mirror-border",
                    "data": "rightcs"
                },
                {
                    "className": "stat-center stat-inset-mirror-border",
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
            "scrollY": false,
            "createdRow": function (row, data, dataIndex) {
                if (data.highlightRow == true) {
                    $(row).addClass('yellowRow');
                }
            }
        });
    });
});