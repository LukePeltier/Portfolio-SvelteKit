$(function () {

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
                        backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmanspurple'),
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmanspurple')
                    }, {
                        label: 'Top',
                        data: data.top,
                        fill: false,
                        backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansred'),
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansred')
                    }, {
                        label: 'Jungle',
                        data: data.jungle,
                        fill: false,
                        backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansorange'),
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansorange')
                    }, {
                        label: 'Middle',
                        data: data.mid,
                        fill: false,
                        backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansyellow'),
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansyellow')
                    }, {
                        label: 'Bottom',
                        data: data.bot,
                        fill: false,
                        backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen'),
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen')
                    }, {
                        label: 'Support',
                        data: data.support,
                        fill: false,
                        backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansblue'),
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansblue')
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