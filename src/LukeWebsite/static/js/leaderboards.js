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
                    "data": "data"
                },
                {
                    "data": "game",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/game/"+oData.gameID+"'>"+sData+"</a>");
                    }
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
                    targets: [3, 4],
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
                    "data": "data"
                },
                {
                    "data": "game",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/game/"+oData.gameID+"'>"+sData+"</a>");
                    }
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
                    targets: [3, 4],
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
                    "data": "data"
                },
                {
                    "data": "game",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/game/"+oData.gameID+"'>"+sData+"</a>");
                    }
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
                    targets: [3, 4],
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

        var mostDamageGameTable = $('#mostDamageGameTable').DataTable({
            "ajax": $('#mostDamageGameTable').data('url'),
            "columns": [
                {
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "data": "data",
                    "render": $.fn.dataTable.render.number(',', '.')
                },
                {
                    "data": "game",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/game/"+oData.gameID+"'>"+sData+"</a>");
                    }
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
                    targets: [3, 4],
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

        var mostSpreeGameTable = $('#mostSpreeGameTable').DataTable({
            "ajax": $('#mostSpreeGameTable').data('url'),
            "columns": [
                {
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "data": "data"
                },
                {
                    "data": "game",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/game/"+oData.gameID+"'>"+sData+"</a>");
                    }
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
                    targets: [3, 4],
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

        var mostCSGameTable = $('#mostCSGameTable').DataTable({
            "ajax": $('#mostCSGameTable').data('url'),
            "columns": [
                {
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "data": "data"
                },
                {
                    "data": "game",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/game/"+oData.gameID+"'>"+sData+"</a>");
                    }
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
                    targets: [3, 4],
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

        var mostCSFirstTwentyGameTable = $('#mostCSFirstTwentyGameTable').DataTable({
            "ajax": $('#mostCSFirstTwentyGameTable').data('url'),
            "columns": [
                {
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "data": "data"
                },
                {
                    "data": "game",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/game/"+oData.gameID+"'>"+sData+"</a>");
                    }
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
                    targets: [3, 4],
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

        var mostVisionGameTable = $('#mostVisionGameTable').DataTable({
            "ajax": $('#mostVisionGameTable').data('url'),
            "columns": [
                {
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "data": "data"
                },
                {
                    "data": "game",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/game/"+oData.gameID+"'>"+sData+"</a>");
                    }
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
                    targets: [3, 4],
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

        var mostControlWardGameTable = $('#mostControlWardGameTable').DataTable({
            "ajax": $('#mostControlWardGameTable').data('url'),
            "columns": [
                {
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "data": "data"
                },
                {
                    "data": "game",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/game/"+oData.gameID+"'>"+sData+"</a>");
                    }
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
                    targets: [3, 4],
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

        var mostBanGameTable = $('#mostBanGameTable').DataTable({
            "ajax": $('#mostBanGameTable').data('url'),
            "columns": [
                {
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "data": "data"
                },
                {
                    "data": "game",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/game/"+oData.gameID+"'>"+sData+"</a>");
                    }
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
                    targets: [3, 4],
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

        var mostChampsTable = $('#mostChampsTable').DataTable({
            "ajax": $('#mostChampsTable').data('url'),
            "columns": [
                {
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "data": "data"
                },
                {
                    "data": "playerID"
                }
            ],
            columnDefs: [
                {
                    targets: [2],
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

        var captainWinrateTable = $('#captainWinrateTable').DataTable({
            "ajax": $('#captainWinrateTable').data('url'),
            "columns": [
                {
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "data": "data"
                },
                {
                    "data": "playerID"
                }
            ],
            columnDefs: [
                {
                    targets: [2],
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

        var captainCountTable = $('#captainCountTable').DataTable({
            "ajax": $('#captainCountTable').data('url'),
            "columns": [
                {
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "data": "data"
                },
                {
                    "data": "playerID"
                }
            ],
            columnDefs: [
                {
                    targets: [2],
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
        var winstreakTable = $('#winstreakTable').DataTable({
            "ajax": $('#winstreakTable').data('url'),
            "columns": [
                {
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "data": "data",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        if(oData.isCurrent){
                            $(nTd).html("<p>" + sData + " <span class=\"badge rounded-pill bg-success\">Current</span></p>");
                        }
                    }

                },
                {
                    "data": "playerID"
                },
                {
                    "data": "isCurrent"
                }
            ],
            columnDefs: [
                {
                    targets: [2,3],
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

        var lossstreakTable = $('#lossstreakTable').DataTable({
            "ajax": $('#lossstreakTable').data('url'),
            "columns": [
                {
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "data": "data",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        if(oData.isCurrent){
                            $(nTd).html("<p>" + sData + " <span class=\"badge rounded-pill bg-danger\">Current</span></p>");
                        }
                    }
                },
                {
                    "data": "playerID"
                },
                {
                    "data": "isCurrent"
                }
            ],
            columnDefs: [
                {
                    targets: [2,3],
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

        var pentakillsTable = $('#pentakillsTable').DataTable({
            "ajax": $('#pentakillsTable').data('url'),
            "columns": [
                {
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "data": "data"
                },
                {
                    "data": "playerID"
                }
            ],
            columnDefs: [
                {
                    targets: [2],
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
        var quadrakillsTable = $('#quadrakillsTable').DataTable({
            "ajax": $('#quadrakillsTable').data('url'),
            "columns": [
                {
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "data": "data"
                },
                {
                    "data": "playerID"
                }
            ],
            columnDefs: [
                {
                    targets: [2],
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
        var triplekillsTable = $('#triplekillsTable').DataTable({
            "ajax": $('#triplekillsTable').data('url'),
            "columns": [
                {
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "data": "data"
                },
                {
                    "data": "playerID"
                }
            ],
            columnDefs: [
                {
                    targets: [2],
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

        var doublekillsTable = $('#doublekillsTable').DataTable({
            "ajax": $('#doublekillsTable').data('url'),
            "columns": [
                {
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "data": "data"
                },
                {
                    "data": "playerID"
                }
            ],
            columnDefs: [
                {
                    targets: [2],
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