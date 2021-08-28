$(function () {
    $(document).ready(function () {
        var laneCountTable = $('#playerLaneCountTable').DataTable({
            "ajax": $('#playerLaneCountTable').data('url'),
            "columns": [
                {
                    "className": "stat-right-large stat-leftcol-border",
                    "data": "lane"
                },
                {
                    "className": "stat-center-large stat-inset-border strong-text",
                    "data": "playCount"
                },
                {
                    "className": "stat-center-large stat-inset-border strong-text",
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
            "columns": [
                {
                    "className": "stat-right stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        if(oData.riotChampionName!=undefined){
                            $(nTd).html("<a href='/ten_mans/champion/" + oData.championID+"'> <img src='https://ddragon.leagueoflegends.com/cdn/" + oData.championVersion +"/img/champion/"+oData.riotChampionName+".png' style='width:20px; height:20px;'/> "+sData+"</a>");
                        }
                    }
                },
                {
                    "className": "stat-center stat-inset-border strong-text",
                    "data": "playCount"
                },
                {
                    "className": "stat-center stat-inset-border strong-text",
                    "data": "winrate",
                    "render": $.fn.dataTable.render.number(',', '.', 0, '', '%')
                },
                {
                    "className": "stat-center stat-inset-border strong-text",
                    "data": "averageKDA"
                },
                {
                    "data": "championID"
                },
                {
                    "data": "riotChampionName"
                },
                {
                    "data": "championVersion"
                },
            ],
            columnDefs: [
                {
                    targets: [4,5,6],
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

        var playerGameTable = $('#playerGamesTable').DataTable({
            "ajax": $('#playerGamesTable').data('url'),
            "columns": [
                {
                    "className": "stat-center cellnowrap stat-leftcol-border",
                    "data": "gameNum",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/game/"+oData.gameID+"'>"+sData+"</a>");
                    }
                },
                {
                    "className": "stat-inset-border cellnowrap",
                    "data": "champion",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        if(oData.riotChampionName!=undefined){
                            $(nTd).html("<a href='/ten_mans/champion/" + oData.championID+"'> <img src='https://ddragon.leagueoflegends.com/cdn/" + oData.championVersion +"/img/champion/"+oData.riotChampionName+".png' style='width:20px; height:20px;'/> "+sData+"</a>");
                        }


                    }

                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "lane",
                    "render": $.fn.dataTable.render.text()
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "winLoss",
                    "render": $.fn.dataTable.render.text()
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
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
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "team",
                    "render": $.fn.dataTable.render.text()
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "kills"
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "deaths"
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "assists"
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "largestKillingSpree"
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "largestMultiKill"
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "doubleKills"
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "tripleKills"
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "quadraKills"
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "pentaKills"
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "totalDamageDealtToChampions",
                    "render": $.fn.dataTable.render.number(',', '.')
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "visionScore"
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "crowdControlScore",
                    "render": $.fn.dataTable.render.number(',', '.')
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "totalDamageTaken",
                    "render": $.fn.dataTable.render.number(',', '.')
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "goldEarned",
                    "render": $.fn.dataTable.render.number(',', '.')
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "turretKills"
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "inhibitorKills"
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "cs"
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "teamJungleMinionsKilled"
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "enemyJungleMinionsKilled"
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "controlWardsPurchased"
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "firstBlood"
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "firstTower"
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "csRateFirstTen",
                    "render": $.fn.dataTable.render.number(',', '.', 1)
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "csRateSecondTen",
                    "render": $.fn.dataTable.render.number(',', '.', 1)
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "gameID"
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "championID"
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "riotChampionName"
                },
                {
                    "className": "stat-center stat-inset-border cellnowrap",
                    "data": "championVersion"
                },
            ],
            columnDefs: [
                {
                    targets: [30, 31, 32, 33],
                    visible: false
                }
            ],
            paging: false,
            searching: false,
            info: false,
            "order": [[0, "asc"]],
            "scrollX": true
        });

    });


});
