$(function () {
    var $laneMatchupChart = $("#laneMatchupChart");
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
                        backgroundColor: window.chartColors.blueTransparent,
                        borderColor: window.chartColors.blue
                    }, {
                        label: data.player2Name,
                        data: data.player2Data,
                        borderWidth: 1,
                        backgroundColor: window.chartColors.redTransparent,
                        borderColor: window.chartColors.red
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