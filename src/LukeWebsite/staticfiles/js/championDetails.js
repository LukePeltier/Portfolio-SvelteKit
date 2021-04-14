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

            var championPlaytime = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.labels,
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
                "data": "name",
                "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                    $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                }
            },
            {
                "data": "playCount"
            },
            {
                "data": "averageKDA"
            },
            {
                "data": "winrate",
                "render": $.fn.dataTable.render.number(',', '.', 0, '', '%')
            },
            {
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
                "data": "gameNum",
                "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                    $(nTd).html("<a href='/ten_mans/game/"+oData.gameID+"'>"+sData+"</a>");
                }
            },
            {
                "data": "player",
                "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                    $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                }

            },
            {
                "data": "lane",
                "render": $.fn.dataTable.render.text()
            },
            {
                "data": "winLoss",
                "render": $.fn.dataTable.render.text()
            },
            {
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
                "data": "team",
                "render": $.fn.dataTable.render.text()
            },
            {
                "data": "kills"
            },
            {
                "data": "deaths"
            },
            {
                "data": "assists"
            },
            {
                "data": "largestKillingSpree"
            },
            {
                "data": "largestMultiKill"
            },
            {
                "data": "doubleKills"
            },
            {
                "data": "tripleKills"
            },
            {
                "data": "quadraKills"
            },
            {
                "data": "pentaKills"
            },
            {
                "data": "totalDamageDealtToChampions",
                "render": $.fn.dataTable.render.number(',', '.')
            },
            {
                "data": "visionScore"
            },
            {
                "data": "crowdControlScore",
                "render": $.fn.dataTable.render.number(',', '.')
            },
            {
                "data": "totalDamageTaken",
                "render": $.fn.dataTable.render.number(',', '.')
            },
            {
                "data": "goldEarned",
                "render": $.fn.dataTable.render.number(',', '.')
            },
            {
                "data": "turretKills"
            },
            {
                "data": "inhibitorKills"
            },
            {
                "data": "cs"
            },
            {
                "data": "teamJungleMinionsKilled"
            },
            {
                "data": "enemyJungleMinionsKilled"
            },
            {
                "data": "controlWardsPurchased"
            },
            {
                "data": "firstBlood"
            },
            {
                "data": "firstTower"
            },
            {
                "data": "csRateFirstTen",
                "render": $.fn.dataTable.render.number(',', '.', 1)
            },
            {
                "data": "csRateSecondTen",
                "render": $.fn.dataTable.render.number(',', '.', 1)
            },
            {
                "data": "gameID"
            },
            {
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
        "scrollX": true,
        "fixedColumns":
        {
            leftColumns: 4
        }
    })

});