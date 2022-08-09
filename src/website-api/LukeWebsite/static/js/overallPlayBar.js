$(function () {

    var $overallPlaytimeChart = $("#overallPlaytimeChart");
    $.ajax({
        url: $overallPlaytimeChart.data("url"),
        success: function (data) {

            var ctx = $overallPlaytimeChart;

            var overallPlaytime = new Chart(ctx, {
                type: 'horizontalBar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Overall',
                        data: data.overall,
                        backgroundColor: function (context) {
                            var index = context.dataIndex;
                            var value = context.dataset.data[index];
                            return getRGBHeatmapColorFromHex(value, getComputedStyle(document.documentElement).getPropertyValue('--tenmanswhite'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansyellow'), 1, false, 0, 50, data.max)
                        },
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen'),
                        borderWidth: 1,
                        minBarLength: 5
                    }, {
                        label: 'Top',
                        data: data.top,
                        hidden: true,
                        backgroundColor: function (context) {
                            var index = context.dataIndex;
                            var value = context.dataset.data[index];
                            return getRGBHeatmapColorFromHex(value, getComputedStyle(document.documentElement).getPropertyValue('--tenmanswhite'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansyellow'), 1, false, 0, 50, data.max)
                        },
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen'),
                        borderWidth: 1,
                        minBarLength: 5
                    }, {
                        label: 'Jungle',
                        data: data.jungle,
                        hidden: true,
                        backgroundColor: function (context) {
                            var index = context.dataIndex;
                            var value = context.dataset.data[index];
                            return getRGBHeatmapColorFromHex(value, getComputedStyle(document.documentElement).getPropertyValue('--tenmanswhite'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansyellow'), 1, false, 0, 50, data.max)
                        },
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen'),
                        borderWidth: 1,
                        minBarLength: 5
                    }, {
                        label: 'Middle',
                        data: data.mid,
                        hidden: true,
                        backgroundColor: function (context) {
                            var index = context.dataIndex;
                            var value = context.dataset.data[index];
                            return getRGBHeatmapColorFromHex(value, getComputedStyle(document.documentElement).getPropertyValue('--tenmanswhite'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansyellow'), 1, false, 0, 50, data.max)
                        },
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen'),
                        borderWidth: 1,
                        minBarLength: 5
                    }, {
                        label: 'Bottom',
                        data: data.bot,
                        hidden: true,
                        backgroundColor: function (context) {
                            var index = context.dataIndex;
                            var value = context.dataset.data[index];
                            return getRGBHeatmapColorFromHex(value, getComputedStyle(document.documentElement).getPropertyValue('--tenmanswhite'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansyellow'), 1, false, 0, 50, data.max)
                        },
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen'),
                        borderWidth: 1,
                        minBarLength: 5
                    }, {
                        label: 'Support',
                        data: data.support,
                        hidden: true,
                        backgroundColor: function (context) {
                            var index = context.dataIndex;
                            var value = context.dataset.data[index];
                            return getRGBHeatmapColorFromHex(value, getComputedStyle(document.documentElement).getPropertyValue('--tenmanswhite'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen'), getComputedStyle(document.documentElement).getPropertyValue('--tenmansyellow'), 1, false, 0, 50, data.max)
                        },
                        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen'),
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
                        text: 'Playtime Bar Chart'
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