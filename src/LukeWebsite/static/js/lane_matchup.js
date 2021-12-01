$(function () {
    var $laneMatchupChart = $("#laneMatchupChart");

    $.ajax({
        url: $laneMatchupChart.data("url"),
        success: function (data) {

            var ctx = $laneMatchupChart;

            Chart.defaults.global.defaultFontColor='white';
            Chart.defaults.global.defaultFontFamily = 'Gill Sans Light';
            var laneMatchup = new Chart(ctx, {
                type: 'horizontalBar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: data.player1Name,
                        data: data.player1Data,
                        borderWidth: 1,
                        backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansblue') + "33",
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansblue')
                    }, {
                        label: data.player2Name,
                        data: data.player2Data,
                        borderWidth: 1,
                        backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansred') + "33",
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansred')
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        xAxes: [{
                            stacked: true,
                            ticks: {
                                min: 0,
                                max: 100
                            }
                        }],
                        yAxes: [{
                            stacked: true,
                        }]
                    },
                    title: {
                        display: true,
                        text: 'Matchup Bar Chart'
                    },
                    tooltips: {
                        mode: 'index',
                        intersect: false,
                    }
                }
            });


        }
    });
    $(document).ready(function () {
        var matchupGamesTable = $('#matchupGamesTable').DataTable({
            "ajax": $('#matchupGamesTable').data('url'),
            "columns": [
                {
                    "className": "stat-center cellnowrap stat-leftcol-border rightBorder",
                    "data": "gameNum",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/game/" + oData.gameID + "'>" + sData + "</a>");
                    }
                },
                {
                    "className": "stat-center cellnowrap stat-inset-border",
                    "data": "leftchampion",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        if (oData.leftriotChampionName != undefined) {
                            $(nTd).html("<a href='/ten_mans/champion/" + oData.leftchampionID + "'>" + sData + " <img src='https://ddragon.leagueoflegends.com/cdn/" + oData.championVersion + "/img/champion/" + oData.leftriotChampionName + ".png' style='width:20px; height:20px;'/> " + "</a>");
                        }


                    }

                },
                {
                    "className": "stat-center cellnowrap stat-inset-border",
                    "data": "leftcs"
                },
                {
                    "className": "stat-center cellnowrap stat-inset-border",
                    "data": "leftkda",
                    "render": $.fn.dataTable.render.text()
                },
                {
                    "className": "stat-center cellnowrap stat-inset-border",
                    "data": "leftlane",
                    "render": $.fn.dataTable.render.text()
                },
                {
                    "className": "stat-center cellnowrap stat-inset-border rightBorder",
                    "data": "leftwinLoss",
                    "render": $.fn.dataTable.render.text()
                },
                {
                    "className": "stat-center cellnowrap stat-inset-border",
                    "data": "rightwinLoss",
                    "render": $.fn.dataTable.render.text()
                },
                {
                    "className": "stat-center cellnowrap stat-inset-border",
                    "data": "rightlane",
                    "render": $.fn.dataTable.render.text()
                },
                {
                    "className": "stat-center cellnowrap stat-inset-border",
                    "data": "rightkda",
                    "render": $.fn.dataTable.render.text()
                },

                {
                    "className": "stat-center cellnowrap stat-inset-border",
                    "data": "rightcs"
                },
                {
                    "className": "stat-center cellnowrap stat-inset-border",
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
                    targets: [11, 12, 13, 14, 15, 16, 17],
                    visible: false
                }
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
        var matchupCountTable = $('#matchupCountTable').DataTable({
            "ajax": $('#matchupCountTable').data('url'),
            "columns": [
                {
                    "className": "stat-right-large stat-leftcol-border",
                    "data": "lane"
                },
                {
                    "className": "stat-center-large cellnowrap stat-inset-border strong-text",
                    "data": "playCount"
                }
            ],
            paging: false,
            searching: false,
            info: false,
            "order": [
                [1, "desc"]
            ]
        });
    });
});