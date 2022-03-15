$(function () {

    var $winrateOverTimeChart = $("#winrateOverTimeChart");
    $.ajax({
        url: $winrateOverTimeChart.data("url"),
        success: function (data) {

            var ctx = $winrateOverTimeChart;

            // Chart.defaults.global.defaultFontColor='white';
            // Chart.defaults.global.defaultFontFamily = 'Gill Sans Light';
            Chart.defaults.color='white';
            Chart.defaults.font.family='Gill Sans Light';
            var overallWinrate = new Chart(ctx, {
                data: {
                    labels: data.labels,
                    datasets: [{
                        type:'line',
                        label: 'Overall',
                        data: data.overall,
                        fill: false,
                        backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmanspurple'),
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmanspurple')
                    }, {
                        type:'line',
                        label: 'Top',
                        data: data.top,
                        fill: false,
                        backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansred'),
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansred')
                    }, {
                        type:'line',
                        label: 'Jungle',
                        data: data.jungle,
                        fill: false,
                        backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansorange'),
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansorange')
                    }, {
                        type:'line',
                        label: 'Middle',
                        data: data.mid,
                        fill: false,
                        backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansyellow'),
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansyellow')
                    }, {
                        type:'line',
                        label: 'Bottom',
                        data: data.bot,
                        fill: false,
                        backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen'),
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen')
                    }, {
                        type:'line',
                        label: 'Support',
                        data: data.support,
                        fill: false,
                        backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansblue'),
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansblue')
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'right'
                        }
                    },
                    title: {
                        display: true,
                        text: 'Winrate Over Time'
                    },
                    tooltips: {
                        mode: 'intersect',
                        intersect: false,
                    },
                    interaction: {
                        mode: 'nearest',
                        intersect: false
                    },
                    scales: {
                        y: {
                            min: 0,
                            max: 100
                        },
                        x:{
                            grid: {
                                color: function(context) {
                                    console.log(data.seasons)
                                    console.log(context.tick.value)
                                    if(data.seasons.indexOf(context.tick.value+1)!==-1){
                                        return getComputedStyle(document.documentElement).getPropertyValue('--tenmanshighlightbold');
                                    }
                                    return '#000000';
                                }
                            }
                        }
                    }
                }
            });


        }
    });

});