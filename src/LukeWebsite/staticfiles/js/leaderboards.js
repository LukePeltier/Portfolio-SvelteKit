$(function () {
    $(document).ready(function () {
        var mostKillsGameTable = $('#mostKillsGameTable').DataTable({
            "ajax": $('#mostKillsGameTable').data('url'),
            "columns": [
                {
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "data": "kills"
                },
                {
                    "data": "game",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/game/"+oData.gameID+"'>"+sData+"</a>");
                    }
                },
                {
                    "data": "gameID"
                }
            ],
            columnDefs: [
                {
                    targets: [3],
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

        var mostDeathsGameTable = $('#mostDeathsGameTable').DataTable({
            "ajax": $('#mostDeathsGameTable').data('url'),
            "columns": [
                {
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "data": "deaths"
                },
                {
                    "data": "game",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/game/"+oData.gameID+"'>"+sData+"</a>");
                    }
                },
                {
                    "data": "gameID"
                }
            ],
            columnDefs: [
                {
                    targets: [3],
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

        var mostAssistsGameTable = $('#mostAssistsGameTable').DataTable({
            "ajax": $('#mostAssistsGameTable').data('url'),
            "columns": [
                {
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "data": "assists"
                },
                {
                    "data": "game",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/game/"+oData.gameID+"'>"+sData+"</a>");
                    }
                },
                {
                    "data": "gameID"
                }
            ],
            columnDefs: [
                {
                    targets: [3],
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

    });
});