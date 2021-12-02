$(function () {

    var $championPlaytimeChart = $("#championPlaytimeChart");
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
                        backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmanspurple')+ "33",
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmanspurple')
                    }, {
                        label: 'Top',
                        data: data.top,
                        fill: false,
                        borderWidth: 1,
                        minBarLength: 5,
                        backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansred')+ "33",
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansred')
                    }, {
                        label: 'Jungle',
                        data: data.jungle,
                        fill: false,
                        borderWidth: 1,
                        minBarLength: 5,
                        backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansorange')+ "33",
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansorange')
                    }, {
                        label: 'Middle',
                        data: data.mid,
                        fill: false,
                        borderWidth: 1,
                        minBarLength: 5,
                        backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansyellow')+ "33",
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansyellow')
                    }, {
                        label: 'Bottom',
                        data: data.bot,
                        fill: false,
                        borderWidth: 1,
                        minBarLength: 5,
                        backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen')+ "33",
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen')
                    }, {
                        label: 'Support',
                        data: data.support,
                        fill: false,
                        borderWidth: 1,
                        minBarLength: 5,
                        backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansblue')+ "33",
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansblue')
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