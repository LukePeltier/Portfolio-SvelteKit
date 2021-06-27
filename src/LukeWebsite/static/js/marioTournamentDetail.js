$(function () {
    $(document).ready(function () {
        var tournamentLeaderboardTable = $('#tournamentLeaderboardTable').DataTable({
            "ajax": $('#tournamentLeaderboardTable').data('url'),
            "columns": [
                {
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
                        $(nTd).html("<a href='/mario_golf/characters/" + oData.characterID+"'>" + sData + "</a>");
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
                targets: [5,6],
                visible: false
            }],
            paging: false,
            searching: false,
            info: false,
            "order": [
                [0, "asc"]
            ],
            "pageResize": true
        })
    });


});