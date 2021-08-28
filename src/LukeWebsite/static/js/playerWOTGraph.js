$(function () {
    window.chartColors = {
        red: 'rgb(255, 99, 132)',
        orange: 'rgb(255, 159, 64)',
        yellow: 'rgb(255, 205, 86)',
        green: 'rgb(92, 184, 92)',
        blue: 'rgb(54, 162, 235)',
        purple: 'rgb(153, 102, 255)',
        grey: 'rgb(201, 203, 207)',
        white: 'rgb(255, 255, 255)'
    };

    var $winrateOverTimeChart = $("#winrateOverTimeChart");
    $.ajax({
        url: $winrateOverTimeChart.data("url"),
        success: function (data) {

            var ctx = $winrateOverTimeChart;

            Chart.defaults.global.defaultFontColor='white';
            Chart.defaults.global.defaultFontFamily = 'Gill Sans Light';
            var overallWinrate = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Overall',
                        data: data.overall,
                        fill: false,
                        backgroundColor: window.chartColors.purple,
                        borderColor: window.chartColors.purple
                    }, {
                        label: 'Top',
                        data: data.top,
                        fill: false,
                        backgroundColor: window.chartColors.red,
                        borderColor: window.chartColors.red
                    }, {
                        label: 'Jungle',
                        data: data.jungle,
                        fill: false,
                        backgroundColor: window.chartColors.orange,
                        borderColor: window.chartColors.orange
                    }, {
                        label: 'Middle',
                        data: data.mid,
                        fill: false,
                        backgroundColor: window.chartColors.yellow,
                        borderColor: window.chartColors.yellow
                    }, {
                        label: 'Bottom',
                        data: data.bot,
                        fill: false,
                        backgroundColor: window.chartColors.green,
                        borderColor: window.chartColors.green
                    }, {
                        label: 'Support',
                        data: data.support,
                        fill: false,
                        backgroundColor: window.chartColors.blue,
                        borderColor: window.chartColors.blue
                    }]
                },
                options: {
                    responsive: true,
                    legend: {
                        position: 'right'
                    },
                    title: {
                        display: true,
                        text: 'Winrate Over Time'
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
                                suggestedMax: 100
                            }
                        }]
                    }
                }
            });


        }
    });

});