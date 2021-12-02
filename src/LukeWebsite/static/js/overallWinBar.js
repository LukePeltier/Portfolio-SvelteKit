$(function () {

    var $overallWinrateChart = $("#overallWinrateChart");
    var color = Chart.helpers.color;
    $.ajax({
        url: $overallWinrateChart.data("url"),
        success: function (data) {

            var ctx = $overallWinrateChart;

            var overallWinrate = new Chart(ctx, {
                type: 'horizontalBar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Overall',
                        data: data.overall,
                        backgroundColor: function (context) {
                            var index = context.dataIndex;
                            var value = context.dataset.data[index];
                            if(value==="N/A"){
                                return "rgba(255, 255, 255, 0)";
                            }
                            return getRGBHeatmapColorFromHex(value, getComputedStyle(document.documentElement).getPropertyValue('--tenmansred'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansyellow'), data.overallAlpha[index], true, 0, 50, 100)
                        },
                        borderWidth: 1,
                        minBarLength: 5
                    }, {
                        label: 'Top',
                        data: data.top,
                        hidden: true,
                        backgroundColor: function (context) {
                            var index = context.dataIndex;
                            var value = context.dataset.data[index];
                            return getRGBHeatmapColorFromHex(value, getComputedStyle(document.documentElement).getPropertyValue('--tenmansred'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansyellow'), data.topAlpha[index], true, 0, 50, 100)
                        },
                        borderWidth: 1,
                        minBarLength: 5
                    }, {
                        label: 'Jungle',
                        data: data.jungle,
                        hidden: true,
                        backgroundColor: function (context) {
                            var index = context.dataIndex;
                            var value = context.dataset.data[index];
                            return getRGBHeatmapColorFromHex(value, getComputedStyle(document.documentElement).getPropertyValue('--tenmansred'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansyellow'), data.jungleAlpha[index], true, 0, 50, 100)
                        },
                        borderWidth: 1,
                        minBarLength: 5
                    }, {
                        label: 'Middle',
                        data: data.mid,
                        hidden: true,
                        backgroundColor: function (context) {
                            var index = context.dataIndex;
                            var value = context.dataset.data[index];
                            return getRGBHeatmapColorFromHex(value, getComputedStyle(document.documentElement).getPropertyValue('--tenmansred'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansyellow'), data.midAlpha[index], true, 0, 50, 100)
                        },
                        borderWidth: 1,
                        minBarLength: 5
                    }, {
                        label: 'Bottom',
                        data: data.bot,
                        hidden: true,
                        backgroundColor: function (context) {
                            var index = context.dataIndex;
                            var value = context.dataset.data[index];
                            return getRGBHeatmapColorFromHex(value, getComputedStyle(document.documentElement).getPropertyValue('--tenmansred'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansyellow'), data.botAlpha[index], true, 0, 50, 100)
                        },
                        borderWidth: 1,
                        minBarLength: 5
                    }, {
                        label: 'Support',
                        data: data.support,
                        hidden: true,
                        backgroundColor: function (context) {
                            var index = context.dataIndex;
                            var value = context.dataset.data[index];
                            return getRGBHeatmapColorFromHex(value, getComputedStyle(document.documentElement).getPropertyValue('--tenmansred'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansyellow'), data.supportAlpha[index], true, 0, 50, 100)
                        },
                        borderWidth: 1,
                        minBarLength: 5
                    }]
                },
                options: {
                    responsive: true,
                    legend: {
                        position: 'right',
                        labels: {
                            boxWidth: 15,
                            generateLabels: function (chart) {
                                labels = Chart.defaults.global.legend.labels.generateLabels(chart);
                                for (var key in labels) {
                                    labels[key].fillStyle = getComputedStyle(document.documentElement).getPropertyValue('--tenmansblue');
                                    labels[key].strokeStyle = getComputedStyle(document.documentElement).getPropertyValue('--tenmansblue');
                                }
                                return labels;
                            }
                        }

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
                    },
                    scales: {
                        xAxes: [{
                            ticks: {
                                min: 0,
                                max: 100
                            }
                        }]
                    }
                }
            });




        },
        complete: function (data){
            $("#loadingText").remove();
        }
    });


});