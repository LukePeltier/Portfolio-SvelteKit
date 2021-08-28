$(function () {

    var $championPlaytimeChart = $("#championPlaytimeChart");
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
        url: $championPlaytimeChart.data("url"),
        success: function (data) {

            var ctx = $championPlaytimeChart;

            Chart.defaults.global.defaultFontColor='white';
            Chart.defaults.global.defaultFontFamily = 'Gill Sans Light';

            var championPlaytime = new Chart(ctx, {
                type: 'bar',
                data: {
                    datasets: [{
                        label: 'Overall',
                        data: data.overall,
                        fill: false,
                        borderWidth: 1,
                        minBarLength: 5,
                        backgroundColor: window.chartColors.purpleTransparent,
                        borderColor: window.chartColors.purple
                    }, {
                        label: 'Top',
                        data: data.top,
                        fill: false,
                        borderWidth: 1,
                        minBarLength: 5,
                        backgroundColor: window.chartColors.redTransparent,
                        borderColor: window.chartColors.red
                    }, {
                        label: 'Jungle',
                        data: data.jungle,
                        fill: false,
                        borderWidth: 1,
                        minBarLength: 5,
                        backgroundColor: window.chartColors.orangeTransparent,
                        borderColor: window.chartColors.orange
                    }, {
                        label: 'Middle',
                        data: data.mid,
                        fill: false,
                        borderWidth: 1,
                        minBarLength: 5,
                        backgroundColor: window.chartColors.yellowTransparent,
                        borderColor: window.chartColors.yellow
                    }, {
                        label: 'Bottom',
                        data: data.bot,
                        fill: false,
                        borderWidth: 1,
                        minBarLength: 5,
                        backgroundColor: window.chartColors.greenTransparent,
                        borderColor: window.chartColors.green
                    }, {
                        label: 'Support',
                        data: data.support,
                        fill: false,
                        borderWidth: 1,
                        minBarLength: 5,
                        backgroundColor: window.chartColors.blueTransparent,
                        borderColor: window.chartColors.blue
                    }]
                },
                options: {
                    responsive: true,
                    title: {
                        display: true,
                        text: 'Playtime Bar Chart'
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                suggestedMin: 0,
                                suggestedMax: 5
                            }
                        }]
                    }
                }
            });


        }
    });

    var playerChampCountTable = $('#playerChampCountTable').DataTable({
        "ajax": $('#playerChampCountTable').data('url'),
        "columns": [
            {
                "className": "stat-center stat-leftcol-border",
                "data": "name",
                "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                    $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                }
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "playCount"
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "averageKDA"
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "winrate",
                "render": $.fn.dataTable.render.number(',', '.', 0, '', '%')
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "playerID"
            }
        ],
        columnDefs: [
            {
                targets: [4],
                visible: false
            }
        ],
        paging: false,
        searching: false,
        info: false,
        "order": [
            [1, "desc"]
        ]
    });

    var champGameTable = $('#champGamesTable').DataTable({
        "ajax": $('#champGamesTable').data('url'),
        "columns": [{
                "className": "stat-center stat-leftcol-border",
                "data": "gameNum",
                "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                    $(nTd).html("<a href='/ten_mans/game/"+oData.gameID+"'>"+sData+"</a>");
                }
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "player",
                "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                    $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                }

            },
            {
                "className": "stat-center stat-inset-border",
                "data": "lane",
                "render": $.fn.dataTable.render.text()
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "winLoss",
                "render": $.fn.dataTable.render.text()
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "duration",
                "render": function(data, type){
                    if(type==='display'){
                        var sec_num = parseInt(data); // don't forget the second param
                        var hours   = Math.floor(sec_num / 3600);
                        var minutes = Math.floor((sec_num - (hours * 3600)) / 60);
                        var seconds = sec_num - (hours * 3600) - (minutes * 60);
                        var fewHours = false;
                        if (hours   < 10) {
                            hours   = "0"+hours;
                            fewHours = true;
                        }
                        if (minutes < 10) {minutes = "0"+minutes;}
                        if (seconds < 10) {seconds = "0"+seconds;}
                        if(fewHours && hours==="00"){
                            return  minutes + ':' + seconds;
                        }
                        return hours+':'+minutes+':'+seconds;
                    }
                    return data
                }
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "team",
                "render": $.fn.dataTable.render.text()
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "kills"
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "deaths"
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "assists"
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "largestKillingSpree"
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "largestMultiKill"
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "doubleKills"
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "tripleKills"
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "quadraKills"
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "pentaKills"
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "totalDamageDealtToChampions",
                "render": $.fn.dataTable.render.number(',', '.')
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "visionScore"
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "crowdControlScore",
                "render": $.fn.dataTable.render.number(',', '.')
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "totalDamageTaken",
                "render": $.fn.dataTable.render.number(',', '.')
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "goldEarned",
                "render": $.fn.dataTable.render.number(',', '.')
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "turretKills"
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "inhibitorKills"
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "cs"
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "teamJungleMinionsKilled"
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "enemyJungleMinionsKilled"
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "controlWardsPurchased"
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "firstBlood"
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "firstTower"
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "csRateFirstTen",
                "render": $.fn.dataTable.render.number(',', '.', 1)
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "csRateSecondTen",
                "render": $.fn.dataTable.render.number(',', '.', 1)
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "gameID"
            },
            {
                "className": "stat-center stat-inset-border",
                "data": "playerID"
            }
        ],
        columnDefs: [
            {
                targets: [30, 31],
                visible: false
            }
        ],
        paging: false,
        searching: false,
        info: false,
        "order": [[0, "asc"]],
        "scrollX": true
    })

});