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

        var playerGameTable = $('#playerGamesTable').DataTable({
            "ajax": $('#playerGamesTable').data('url'),
            "columns": [{
                    "data": "gameNum"
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

    $("#playerGamesTable tbody tr").on('click',function(event) {
        $("#playerGamesTable tbody tr").removeClass('row_selected');
        $(this).addClass('row_selected');
    });

});