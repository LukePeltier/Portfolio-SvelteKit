$(function () {
    $(document).ready(function () {
        var blueTeamTable = $('#blueTeamTable').DataTable({
            "ajax": $('#blueTeamTable').data('url'),
            "columns": [
                {
                    "className": "stat-right stat-leftcol-border",
                    "data": "playerName",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "champion",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        if(oData.riotChampionName!=undefined){
                            $(nTd).html("<a href='/ten_mans/champion/" + oData.championID+"'> <img src='https://ddragon.leagueoflegends.com/cdn/" + oData.championVersion +"/img/champion/"+oData.riotChampionName+".png' style='width:20px; height:20px;'/> "+sData+"</a>");
                        }
                    }
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
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
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "draftOrder"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "kills"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "deaths"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "assists"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "largestKillingSpree"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "largestMultiKill"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "doubleKills"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "tripleKills"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "quadraKills"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "pentaKills"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "totalDamageDealtToChampions",
                    "render": $.fn.dataTable.render.number(',', '.')
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "visionScore"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "crowdControlScore",
                    "render": $.fn.dataTable.render.number(',', '.')
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "totalDamageTaken",
                    "render": $.fn.dataTable.render.number(',', '.')
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "goldEarned",
                    "render": $.fn.dataTable.render.number(',', '.')
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "turretKills"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "inhibitorKills"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "cs"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "teamJungleMinionsKilled"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "enemyJungleMinionsKilled"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "controlWardsPurchased"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "firstBlood",
                    "render": function (data, type, row) {
                        return (data === true) ? '<p>&#9989;</p>' : '<p>&#10060</p>';
                    }
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "firstTower",
                    "render": function (data, type, row) {
                        return (data === true) ? '<p>&#9989;</p>' : '<p>&#10060</p>';
                    }
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "csRateFirstTen",
                    "render": $.fn.dataTable.render.number(',', '.', 1)
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "csRateSecondTen",
                    "render": $.fn.dataTable.render.number(',', '.', 1)
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
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
            "scrollX": true
        });

        var redTeamTable = $('#redTeamTable').DataTable({
            "ajax": $('#redTeamTable').data('url'),
            "columns": [
                {
                    "className": "stat-right stat-leftcol-border",
                    "data": "playerName",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "champion",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        if(oData.riotChampionName!=undefined){
                            $(nTd).html("<a href='/ten_mans/champion/" + oData.championID+"'> <img src='https://ddragon.leagueoflegends.com/cdn/" + oData.championVersion +"/img/champion/"+oData.riotChampionName+".png' style='width:20px; height:20px;'/> "+sData+"</a>");
                        }
                    }
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
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
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "draftOrder"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "kills"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "deaths"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "assists"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "largestKillingSpree"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "largestMultiKill"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "doubleKills"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "tripleKills"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "quadraKills"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "pentaKills"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "totalDamageDealtToChampions",
                    "render": $.fn.dataTable.render.number(',', '.')
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "visionScore"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "crowdControlScore",
                    "render": $.fn.dataTable.render.number(',', '.')
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "totalDamageTaken",
                    "render": $.fn.dataTable.render.number(',', '.')
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "goldEarned",
                    "render": $.fn.dataTable.render.number(',', '.')
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "turretKills"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "inhibitorKills"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "cs"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "teamJungleMinionsKilled"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "enemyJungleMinionsKilled"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "controlWardsPurchased"
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "firstBlood",
                    "render": function (data, type, row) {
                        return (data === true) ? '<p>&#9989;</p>' : '<p>&#10060</p>';
                    }
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "firstTower",
                    "render": function (data, type, row) {
                        return (data === true) ? '<p>&#9989;</p>' : '<p>&#10060</p>';
                    }
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
                    "data": "csRateFirstTen",
                    "render": $.fn.dataTable.render.number(',', '.', 1)
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
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
            "scrollX": true
        });

        var blueTeamBansTable = $('#blueTeamBansTable').DataTable({
            "ajax": $('#blueTeamBansTable').data('url'),
            "columns": [
                {
                    "className": "stat-right cellnowrap stat-leftcol-border",
                    "data": "champion",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        if(oData.riotChampionName!=undefined){
                            $(nTd).html("<a href='/ten_mans/champion/" + oData.championID+"'> <img src='https://ddragon.leagueoflegends.com/cdn/" + oData.championVersion +"/img/champion/"+oData.riotChampionName+".png' style='width:20px; height:20px;'/> "+sData+"</a>");
                        }
                    }
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
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
        });

        var redTeamBansTable = $('#redTeamBansTable').DataTable({
            "ajax": $('#redTeamBansTable').data('url'),
            "columns": [
                {
                    "className": "stat-right cellnowrap stat-leftcol-border",
                    "data": "champion",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        if(oData.riotChampionName!=undefined){
                            $(nTd).html("<a href='/ten_mans/champion/" + oData.championID+"'> <img src='https://ddragon.leagueoflegends.com/cdn/" + oData.championVersion +"/img/champion/"+oData.riotChampionName+".png' style='width:20px; height:20px;'/> "+sData+"</a>");
                        }
                    }
                },
                {
                    "className": "stat-center-auto stat-inset-border cellnowrap strong-text",
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
        });

    });


});