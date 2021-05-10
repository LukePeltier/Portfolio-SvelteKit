$(function () {
    $(document).ready(function () {
        var blueTeamTable = $('#blueTeamTable').DataTable({
            "ajax": $('#blueTeamTable').data('url'),
            "columns": [{
                    "data": "playerName",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "data": "champion",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        if(oData.riotChampionName!=undefined){
                            $(nTd).html("<a href='/ten_mans/champion/" + oData.championID+"'> <img src='https://ddragon.leagueoflegends.com/cdn/" + oData.championVersion +"/img/champion/"+oData.riotChampionName+".png' style='width:20px; height:20px;'/> "+sData+"</a>");
                        }
                    }
                },
                {
                    "data": "lane",
                    "render": function (data, type) {
                        if (type === 'sort') {
                            if (data === "Top") {
                                return 0;
                            }
                            if (data === "Jungle") {
                                return 1;
                            }
                            if (data === "Mid") {
                                return 2;
                            }
                            if (data === "Bot") {
                                return 3;
                            }
                            if (data === "Support") {
                                return 4;
                            }

                        }
                        return data;
                    }
                },
                {
                    "data": "draftOrder"
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
                    "data": "firstBlood",
                    "render": function (data, type, row) {
                        return (data === true) ? '<p>&#9989;</p>' : '<p>&#10060</p>';
                    }
                },
                {
                    "data": "firstTower",
                    "render": function (data, type, row) {
                        return (data === true) ? '<p>&#9989;</p>' : '<p>&#10060</p>';
                    }
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
                    "data": "playerID"
                }
            ],
            columnDefs: [{
                targets: [28],
                visible: false
            }],
            paging: false,
            searching: false,
            info: false,
            "order": [
                [2, "asc"]
            ],
            "pageResize": true,
            "scrollX": true,
            "fixedColumns": {
                leftColumns: 3
            }
        })

        var redTeamTable = $('#redTeamTable').DataTable({
            "ajax": $('#redTeamTable').data('url'),
            "columns": [{
                    "data": "playerName",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "data": "champion",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        if(oData.riotChampionName!=undefined){
                            $(nTd).html("<a href='/ten_mans/champion/" + oData.championID+"'> <img src='https://ddragon.leagueoflegends.com/cdn/" + oData.championVersion +"/img/champion/"+oData.riotChampionName+".png' style='width:20px; height:20px;'/> "+sData+"</a>");
                        }
                    }
                },
                {
                    "data": "lane",
                    "render": function (data, type) {
                        if (type === 'sort') {
                            if (data === "Top") {
                                return 0;
                            }
                            if (data === "Jungle") {
                                return 1;
                            }
                            if (data === "Mid") {
                                return 2;
                            }
                            if (data === "Bot") {
                                return 3;
                            }
                            if (data === "Support") {
                                return 4;
                            }

                        }
                        return data;
                    }
                },
                {
                    "data": "draftOrder"
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
                    "data": "firstBlood",
                    "render": function (data, type, row) {
                        return (data === true) ? '<p>&#9989;</p>' : '<p>&#10060</p>';
                    }
                },
                {
                    "data": "firstTower",
                    "render": function (data, type, row) {
                        return (data === true) ? '<p>&#9989;</p>' : '<p>&#10060</p>';
                    }
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
                    "data": "playerID"
                }
            ],
            columnDefs: [{
                    targets: [28],
                    visible: false
                },
                {
                    targets: [1],
                    class: "cellnowrap"
                }
            ],
            paging: false,
            searching: false,
            info: false,
            "order": [
                [2, "asc"]
            ],
            "pageResize": true,
            "scrollX": true,
            "fixedColumns": {
                leftColumns: 3
            }
        })

        var blueTeamBansTable = $('#blueTeamBansTable').DataTable({
            "ajax": $('#blueTeamBansTable').data('url'),
            "columns": [
                {
                    "data": "champion",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        if(oData.riotChampionName!=undefined){
                            $(nTd).html("<a href='/ten_mans/champion/" + oData.championID+"'> <img src='https://ddragon.leagueoflegends.com/cdn/" + oData.championVersion +"/img/champion/"+oData.riotChampionName+".png' style='width:20px; height:20px;'/> "+sData+"</a>");
                        }
                    }
                },
                {
                    "data": "playerName",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "data": "playerID"
                }
            ],
            columnDefs: [{
                targets: [2],
                visible: false
            }],
            paging: false,
            searching: false,
            info: false,
            "order": [
                [1, "asc"]
            ],
            "pageResize": true
        })

        var redTeamBansTable = $('#redTeamBansTable').DataTable({
            "ajax": $('#redTeamBansTable').data('url'),
            "columns": [
                {
                    "data": "champion",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        if(oData.riotChampionName!=undefined){
                            $(nTd).html("<a href='/ten_mans/champion/" + oData.championID+"'> <img src='https://ddragon.leagueoflegends.com/cdn/" + oData.championVersion +"/img/champion/"+oData.riotChampionName+".png' style='width:20px; height:20px;'/> "+sData+"</a>");
                        }
                    }
                },
                {
                    "data": "playerName",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "data": "playerID"
                }
            ],
            columnDefs: [{
                targets: [2],
                visible: false
            }],
            paging: false,
            searching: false,
            info: false,
            "order": [
                [1, "asc"]
            ],
            "pageResize": true
        })

    });


});