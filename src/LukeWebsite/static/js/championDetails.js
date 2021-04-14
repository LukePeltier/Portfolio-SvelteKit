$(function () {

    var $championPlaytimeChart = $("#championPlaytimeChart");
    window.chartColors = {
        red: 'rgb(255, 99, 132)',
        orange: 'rgb(255, 159, 64)',
        yellow: 'rgb(255, 205, 86)',
        green: 'rgb(92, 184, 92)',
        blue: 'rgb(54, 162, 235)',
        purple: 'rgb(153, 102, 255)',
        grey: 'rgb(201, 203, 207)',
        white: 'rgb(255, 255, 255)',
        redTransparent: 'rgb(255, 99, 132, 0.2)',
        orangeTransparent: 'rgb(255, 159, 64, 0.2)',
        yellowTransparent: 'rgb(255, 205, 86, 0.2)',
        greenTransparent: 'rgb(92, 184, 92, 0.2)',
        blueTransparent: 'rgb(54, 162, 235, 0.2)',
        purpleTransparent: 'rgb(153, 102, 255, 0.2)',
        greyTransparent: 'rgb(201, 203, 207, 0.2)',
        whiteTransparent: 'rgb(255, 255, 255, 0.2)'
    };
    $.ajax({
        url: $championPlaytimeChart.data("url"),
        success: function (data) {

            var ctx = $championPlaytimeChart;

            var championPlaytime = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Overall',
                        data: data.overall,
                        fill: false,
                        borderWidth: 1,
                        minBarLength: 5,
                        backgroundColor: window.chartColors.purpleTransparent,
                        borderColor: window.chartColors.purple
                    }, {
                        label: 'Top',
                        data: data.top,
                        fill: false,
                        borderWidth: 1,
                        minBarLength: 5,
                        backgroundColor: window.chartColors.redTransparent,
                        borderColor: window.chartColors.red
                    }, {
                        label: 'Jungle',
                        data: data.jungle,
                        fill: false,
                        borderWidth: 1,
                        minBarLength: 5,
                        backgroundColor: window.chartColors.orangeTransparent,
                        borderColor: window.chartColors.orange
                    }, {
                        label: 'Middle',
                        data: data.mid,
                        fill: false,
                        borderWidth: 1,
                        minBarLength: 5,
                        backgroundColor: window.chartColors.yellowTransparent,
                        borderColor: window.chartColors.yellow
                    }, {
                        label: 'Bottom',
                        data: data.bot,
                        fill: false,
                        borderWidth: 1,
                        minBarLength: 5,
                        backgroundColor: window.chartColors.greenTransparent,
                        borderColor: window.chartColors.green
                    }, {
                        label: 'Support',
                        data: data.support,
                        fill: false,
                        borderWidth: 1,
                        minBarLength: 5,
                        backgroundColor: window.chartColors.blueTransparent,
                        borderColor: window.chartColors.blue
                    }]
                },
                options: {
                    responsive: true,
                    title: {
                        display: true,
                        text: 'Playtime Bar Chart'
                    },
                    tooltips: {
                        mode: 'index',
                        intersect: false,
                    },
                    hover: {
                        mode: 'nearest',
                        intersect: true
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                suggestedMin: 0,
                                suggestedMax: 5
                            }
                        }]
                    }
                }
            });


        }
    });

});