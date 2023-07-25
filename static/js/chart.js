// Variabel menyimpan temporary data dari Chart
let currentChart = null;
// Variabel menyimpan temporary data-id dari Chart
let currentId = null;

const csvButton = document.getElementById('generateCSV');

function displayChart(chartId, Id) {
    if (currentId && currentChart) {
        delete currentId;
        currentChart.destroy();
    }

    currentId = Id;
    console.log(currentId);

    if (chartId === 'chart-button1') {
        // Membuat grafik 1
        $.getJSON("/sentiment/getTrenTotalSentiment/", function (response) {
            var options = {
                chart: {
                    width: "100%",
                    height: "90%",
                    type: "area",
                },
                dataLabels: {
                    enabled: false
                },
                series: response.total_sentiment_per_day[Id],
                stroke: {
                    width: [2, 2, 2], // mengatur lebar garis
                },
                fill: {
                    type: "gradient",
                    gradient: {
                        shadeIntensity: 1,
                        opacityFrom: 0,
                        opacityTo: 0,
                        stops: [0, 90, 100]
                    }
                },
                xaxis: {
                    categories: response.dates
                },
                colors: ['#FF0000', '#00FF0A', '#7B7B7B'],
                strokeColors: ['#FF0000', '#00FF0A', '#7B7B7B'],
            };
            const chart1 = new ApexCharts(document.getElementById('chart-display'), options);
            chart1.render();
            currentChart = chart1;
        })
    } else if (chartId === 'chart-button2') {
        // Membuat grafik 2
        $.getJSON("/sentiment/getTrenTotalSentiment/", function (response) {
            var options = {
                series: response.total_sentiment_per_day[Id],
                chart: {
                    type: 'bar',
                    width: "100%",
                    height: "90%",
                    stacked: true,
                },
                plotOptions: {
                    bar: {
                        horizontal: true,
                        dataLabels: {
                            total: {
                                enabled: true,
                                offsetX: 0,
                                style: {
                                    fontSize: '13px',
                                    fontWeight: 900
                                }
                            }
                        }
                    },
                },
                colors: ['#FF0000', '#00FF0A', '#7B7B7B'],
                stroke: {
                    width: 2,
                    colors: ['#fff']
                },
                xaxis: {
                    categories: response.dates,
                    labels: {
                        formatter: function (val) {
                            return val
                        }
                    }
                },
                yaxis: {
                    title: {
                        text: undefined
                    },
                },
                tooltip: {
                    y: {
                        formatter: function (val) {
                            return val
                        }
                    }
                },
                fill: {
                    opacity: 1
                },
                legend: {
                    position: 'top',
                    horizontalAlign: 'left',
                    offsetX: 40
                }
            };
            const chart2 = new ApexCharts(document.getElementById('chart-display'), options);
            chart2.render();
            currentChart = chart2;
        })
    }

    const buttons = document.querySelectorAll('.chart-button');
    buttons.forEach(button => {
        button.classList.remove('activeTren');
        if (button.id === chartId) {
            button.classList.add('activeTren');
        }
    });
}

// Grafik Tren All Tweet
function displayChartTotal() {
    $.getJSON("/sentiment/getTrenTotalTweet/", function (response) {
        var options = {
            chart: {
                width: "100%",
                height: "90%",
                type: "area",
            },
            dataLabels: {
                enabled: false
            },
            series: response.bacapres_total_tweet_per_day,
            fill: {
                type: "gradient",
                gradient: {
                    shadeIntensity: 1,
                    opacityFrom: 0,
                    opacityTo: 0,
                    stops: [0, 90, 100]
                }
            },
            stroke: {
                width: 2,
            },
            xaxis: {
                categories: response.dates,
            },
        };
        const chart = new ApexCharts(document.querySelector("#chart-display-Total"), options);
        chart.render();
    })  
}

document.addEventListener("DOMContentLoaded", function () {
    displayChartTotal();
});

// Menampilkan grafik default saat halaman dimuat
document.addEventListener("DOMContentLoaded", function () {
    var chartType = getCurrentChartType();
    var displayOption = getSelectedBacapresOption();
    displayChart(chartType, displayOption);
    displayTotalTweet(displayOption);
    }
);

document.querySelectorAll(".chart-button").forEach(function(button) {
    button.addEventListener("click", function() {
        var chartType = button.getAttribute("id");
        console.log(chartType)
        var displayOption = getSelectedBacapresOption();
        console.log(displayOption)
        displayChart(chartType, displayOption);
    });
});

document.querySelectorAll(".rankingButton").forEach(function(button) {
    button.addEventListener("click", function() {
        var chartType = getCurrentChartType();
        console.log(chartType)
        var displayOption = button.getAttribute("data-id");
        console.log(displayOption)
        displayChart(chartType, displayOption);
        // Mengambil data-id yang baru untuk jumlah tweet dan sentiment
        displayTotalTweet(displayOption)
        // Display data tweet
        getDataDashboard(displayOption, 1)
    });
});

function getCurrentChartType() {
    var activeButton = document.querySelector(".chart-button.activeTren");
    return activeButton ? activeButton.getAttribute("id") : null;
}

function getSelectedBacapresOption() {
    var activeButton = document.querySelector(".rankingButton.activeRanking");
    console.log(activeButton)
    return activeButton ? activeButton.getAttribute("data-id") : null;
}

// function menampilkan jumlah tweet dan sentiment
let currentTotal = null;
function displayTotalTweet(Id) {
    if (currentTotal) {
        delete currentTotal;
    }
    currentTotal = Id;
    $.getJSON("/sentiment/getTotalTweet/", function (response) {
        // Menampilkan data total tweet
        document.getElementById("total-display").innerText = response.bacapres_total_tweet[currentTotal];
        // Menampilkan data sentiment positive
        document.getElementById("total-positive").innerText = response.bacapres_total_sentiment[currentTotal]['positive'];
        // Menampilkan data sentiment neutral
        document.getElementById("total-neutral").innerText = response.bacapres_total_sentiment[currentTotal]['neutral'];
        // Menampilkan data sentiment negative
        document.getElementById("total-negative").innerText = response.bacapres_total_sentiment[currentTotal]['negative'];
    })
}

csvButton.addEventListener('click', function() {
    // Make the AJAX request using getJSON
    var id = getSelectedBacapresOption();
    var xhr = new XMLHttpRequest();
    xhr.open('GET', `/sentiment/generateCSV?bacapres=${id}`, true);
    xhr.responseType = 'blob';

    xhr.onload = function() {
        if (xhr.status === 200) {
            // Create a download link for the CSV file
            var downloadLink = document.createElement('a');
            downloadLink.href = window.URL.createObjectURL(xhr.response);
            downloadLink.download = 'data.csv';
            downloadLink.click();
        }
    };

    xhr.send();
  });