$(function () {

    var $overallWinrateChart = $("#overallWinrateChart");
    var color = Chart.helpers.color;
    window.chartColors = {
        red: 'rgb(255, 99, 132)',
        orange: 'rgb(255, 159, 64)',
        yellow: 'rgb(255, 205, 86)',
        green: 'rgb(92, 184, 92)',
        blue: 'rgb(54, 162, 235)',
        purple: 'rgb(153, 102, 255)',
        grey: 'rgb(201, 203, 207)'
    };
    $.ajax({
        url: $overallWinrateChart.data("url"),
        success: function (data) {

            var ctx = $overallWinrateChart;

            var overallWinrate = new Chart(ctx, {
                type: 'horizontalBar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Winrate',
                        data: data.overall,
                        backgroundColor: function (context) {
                            var index = context.dataIndex;
                            var value = context.dataset.data[index];
                            if (value < 50) {
                                var multiplier = ((50 - value) / 50);
                                var redVal = 255;
                                var greenVal = Math.floor((99 * multiplier) + (205 * (1 - multiplier)));
                                var blueVal = Math.floor((132 * multiplier) + (86 * (1 - multiplier)));
                                var colorString = 'rgb(' + [redVal, greenVal, blueVal].join(',') + ')';
                                return colorString;

                            } else {
                                var tempValue = value - 50;
                                var multiplier = ((50 - tempValue) / 50);
                                var redVal = Math.floor((255 * multiplier) + (92 * (1 - multiplier)));
                                var greenVal = Math.floor((205 * multiplier) + (184 * (1 - multiplier)));
                                var blueVal = Math.floor((86 * multiplier) + (92 * (1 - multiplier)));
                                var colorString = 'rgb(' + [redVal, greenVal, blueVal].join(',') + ')';
                                return colorString;
                            }
                        },
                        borderWidth: 1,
                        minBarLength: 2
                    }]
                },
                options: {
                    responsive: true,
                    legend: {
                        position: 'right',
                    },
                    title: {
                        display: true,
                        text: 'Winrate Bar Chart'
                    },
                    tooltips: {
                        mode: 'index',
                        intersect: false,
                    },
                    hover: {
                        mode: 'nearest',
                        intersect: true
                    }
                }
            });


        }
    });

});