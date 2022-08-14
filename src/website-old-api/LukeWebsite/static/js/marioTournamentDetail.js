$(function () {
    $(document).ready(function () {
        var tournamentLeaderboardTable = $('#tournamentLeaderboardTable').DataTable({
            "ajax": $('#tournamentLeaderboardTable').data('url'),
            "columns": [{
                    "data": "placement"
                },
                {
                    "data": "playerName",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/mario_golf/players/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },
                {
                    "data": "character",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/mario_golf/characters/" + oData.characterID + "'>" + sData + "</a>");
                    }
                },
                {
                    "data": "score"
                },
                {
                    "data": "shotsTaken"
                },
                {
                    "data": "playerID"
                },
                {
                    "data": "characterID"
                }
            ],
            columnDefs: [{
                targets: [5, 6],
                visible: false
            }],
            paging: false,
            searching: false,
            info: false,
            "order": [
                [0, "asc"]
            ],
            "pageResize": true
        });
    });


});

function getRGBGolfScorecardColor(val, par) {
    console.log("Value: " + val);
    console.log("Par: " + par);
    console.log("Result: " + val-par);


    if (val == 1 || val - par == -3) {
        return 'rgb(0,255,255)';
    }
    if (val - par == -2) {
        return 'rgb(252, 236, 0)';
    }
    if (val - par == -1) {
        return 'rgb(255, 170, 1)';
    }
    if (val - par > 0) {
        return 'rgb(161, 161, 161)';
    }

    return 'rgb(255,255,255)';

}