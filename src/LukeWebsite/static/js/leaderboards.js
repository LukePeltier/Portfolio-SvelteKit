$(function () {
    $(document).ready(function () {
        var mostKillsGameTable = $('#mostKillsGameTable').DataTable({
            "ajax": $('#mostKillsGameTable').data('url'),
            "columns": [
                {
                    "className": "stat-right-large stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "className": "stat-center-large stat-inset-border strong-text",
                    "data": "data"
                },
                {
                    "className": "stat-center-large stat-inset-border strong-text",
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
                    "className": "stat-right-large stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "className": "stat-center-large stat-inset-border strong-text",
                    "data": "data"
                },
                {
                    "className": "stat-center-large stat-inset-border strong-text",
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
                    "className": "stat-right-large stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "className": "stat-center-large stat-inset-border strong-text",
                    "data": "data"
                },
                {
                    "className": "stat-center-large stat-inset-border strong-text",
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
                    "className": "stat-right-large stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "className": "stat-center-large stat-inset-border strong-text",
                    "data": "data",
                    "render": $.fn.dataTable.render.number(',', '.')
                },
                {
                    "className": "stat-center-large stat-inset-border strong-text",
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
                    "className": "stat-right-large stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "className": "stat-center-large stat-inset-border strong-text",
                    "data": "data"
                },
                {
                    "className": "stat-center-large stat-inset-border strong-text",
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
                    "className": "stat-right-large stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "className": "stat-center-large stat-inset-border strong-text",
                    "data": "data"
                },
                {
                    "className": "stat-center-large stat-inset-border strong-text",
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
                    "className": "stat-right-large stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "className": "stat-center-large stat-inset-border strong-text",
                    "data": "data"
                },
                {
                    "className": "stat-center-large stat-inset-border strong-text",
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
                    "className": "stat-right-large stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "className": "stat-center-large stat-inset-border strong-text",
                    "data": "data"
                },
                {
                    "className": "stat-center-large stat-inset-border strong-text",
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
                    "className": "stat-right-large stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "className": "stat-center-large stat-inset-border strong-text",
                    "data": "data"
                },
                {
                    "className": "stat-center-large stat-inset-border strong-text",
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
                    "className": "stat-right-large stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "className": "stat-center-large stat-inset-border strong-text",
                    "data": "data"
                },
                {
                    "className": "stat-center-large stat-inset-border strong-text",
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
                    "className": "stat-right-large stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "className": "stat-center-large stat-inset-border strong-text",
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
                    "className": "stat-right-large stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "className": "stat-center-large stat-inset-border strong-text",
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
                    "className": "stat-right-large stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "className": "stat-center-large stat-inset-border strong-text",
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
                    "className": "stat-right-large stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "className": "stat-center-large stat-inset-border strong-text",
                    "data": "data",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        if(oData.isCurrent){
                            $(nTd).html("<span class=\"badge rounded-pill bg-success\">"+ sData + "</span>");
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
                    "className": "stat-right-large stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "className": "stat-center-large stat-inset-border strong-text",
                    "data": "data",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        if(oData.isCurrent){
                            $(nTd).html("<span class=\"badge rounded-pill bg-danger\">"+ sData + "</span>");
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
                    "className": "stat-right-large stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "className": "stat-center-large stat-inset-border strong-text",
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
                    "className": "stat-right-large stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "className": "stat-center-large stat-inset-border strong-text",
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
                    "className": "stat-right-large stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "className": "stat-center-large stat-inset-border strong-text",
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
                    "className": "stat-right-large stat-leftcol-border",
                    "data": "name",
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='/ten_mans/player/" + oData.playerID + "'>" + sData + "</a>");
                    }
                },

                {
                    "className": "stat-center-large stat-inset-border strong-text",
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