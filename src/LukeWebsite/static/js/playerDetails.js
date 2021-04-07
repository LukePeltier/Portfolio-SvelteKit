$(function () {
    $(document).ready(function () {
        var laneCountTable = $('#playerLaneCountTable').DataTable({
            "ajax": $('#playerLaneCountTable').data('url'),
            "columns": [{
                    "data": "lane"
                },
                {
                    "data": "playCount"
                },
                {
                    "data": "averageKDA"
                }
            ],
            paging: false,
            searching: false,
            info: false,
            "order": [
                [1, "desc"]
            ]
        });
        var championCountTable = $('#playerChampionCountTable').DataTable({
            "ajax": $('#playerChampionCountTable').data('url'),
            "columns": [{
                    "data": "name"
                },
                {
                    "data": "playCount"
                },
                {
                    "data": "winrate",
                    "render": $.fn.dataTable.render.number(',', '.', 0, '', '%')
                },
                {
                    "data": "averageKDA"
                }
            ],
            paging: false,
            searching: false,
            info: false,
            "order": [
                [1, "desc"]
            ]
        });

        var playerGameTable = $('#playerGamesTable').DataTable({
            "ajax": $('#playerGamesTable').data('url'),
            "columns": [{
                    "data": "gameNum",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/game/"+oData.gameID+"'>"+sData+"</a>");
                    }
                },
                {
                    "data": "champion",
                    "render": $.fn.dataTable.render.text()
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
                }
            ],
            columnDefs: [
                {
                    targets: [30],
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


});
