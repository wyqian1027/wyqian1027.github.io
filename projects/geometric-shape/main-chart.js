
// Create the chart
Highcharts.chart('shapeRecognition-main-chart', {
    // colors: ['#f45b5b', '#8085e9', '#8d4654', '#7798BF', '#aaeeee',
    //     '#ff0066', '#eeaaee', '#55BF3B', '#DF5353', '#7798BF', '#aaeeee'],
    
    chart: {
        type: 'column',
        borderColor: 'black',
        borderWidth: 1,
        // style: {
        //     fontFamily: 'Signika, serif'
        // }
    },
    title: {
        text: 'Error Rate of Different Methods in Shape Recognition',
        style: {
            color: 'black',
            fontSize: '20px',
            // fontWeight: 'bold',
        }
    },
    subtitle: {
        text: 'Click the columns to view each method in details. (Random Seed = 1)',
        style: {
            color: 'black',
            fontSize: '15px'
        }
    },
    xAxis: {
        type: 'category',
        labels: {
            style: {
                color: 'black',
                fontSize: '15px'
            }
        },

    },
    yAxis: {
        title: {
            text: 'Averaged Error Rate',
            style: {
                fontSize: '20px',
                color: 'black'
            }
        },
        labels: {
            style: {
                color: 'black',
                fontSize: '20px'
            }
        },
        // max: 15,
        min: 0
    },
    legend: {
        enabled: false
    },
    plotOptions: {
        series: {
            borderWidth: 0,
            dataLabels: {
                enabled: true,
                format: '{point.y:.1f}%',
                style: {
                    fontSize: '15px'
                }
            }
        }
    },

    tooltip: {
        style: {
            fontSize: '23px'
        },
        headerFormat: '<span style="font-size:19px">{series.name}</span><br>',
        pointFormat: '<span style="font-size:19px;color:{point.color}">{point.name}</span><span style="font-size:19px;">: <strong>{point.y:.3f}%</strong> of 160 test samples<br/> </span>'
    },

    "series": [
        {
            "name": "ML Methods",
            "colorByPoint": true,
            "data": [
                {
                    "name": "K Nearest Neighbor",
                    "y": 5.625,
                    "drilldown": "KNN"
                },
                {
                    "name": "Gaussian Generative Model",
                    "y": 0.625,
                    "drilldown": "GGM"
                },
                {
                    "name": "Multi-class Perceptron",
                    "y": 13.125,
                    "drilldown": "MP"
                },
                {
                    "name": "Support Vector Machine (Linear)",
                    "y": 8.125,
                    "drilldown": "SVM-lin"
                },
                {
                    "name": "Support Vector Machine (Quadratic)",
                    "y": 7.5,
                    "drilldown": "SVM-quad"
                },
                // {
                //     "name": "Artificial Neural Network",
                //     "y": 15.62,
                //     "drilldown": "Artificial Neural Network"
                // },
                {
                    "name": "Artificial Neural Network",
                    "y": 0,
                    "drilldown": "ANN"
                }
            ]
        }
    ],
    "drilldown": {
        "series": [
            {
                "name": "K Nearest Neighbor",
                "id": "KNN",
                "data": [["Circle", 0], ["Triangle", 4.76190476], ["Square", 0], ["Pentagon", 9.52380952], ["Rhombus", 8.], 
                          ["Star", 4.76190476], ["Trefoil", 9.52380952],["Heart", 6.25]],
            },
            {
                "name": "Gaussian Generative Model",
                "id": "GGM",
                "data": [["Circle", 0], ["Triangle", 0],  ["Square", 0],  ["Pentagon", 4.76190476], ["Rhombus", 0], 
                        ["Star", 0], ["Trefoil", 0], ["Heart", 0]],
            },
            {
                "name": "Multi-class Perceptron",
                "id": "MP",
                "data": [["Circle", 5.88235294], ["Triangle", 9.52380952], ["Square", 5.55555556], ["Pentagon", 14.28571429], ["Rhombus", 28], 
                         ["Star", 9.52380952], ["Trefoil", 4.76190476], ["Heart", 12.5]],
            },
            {
                "name": "Support Vector Machine (Linear)",
                "id": "SVM-lin",
                "data": [["Circle", 0], ["Triangle", 9.52380952],["Square", 5.55555556],  ["Pentagon", 14.28571429], ["Rhombus", 4.], 
                         ["Star", 14.28571429], ["Trefoil", 4.76190476], ["Heart", 12.5]],
            },
            {
                "name": "Support Vector Machine (Quadratic)",
                "id": "SVM-quad",
                "data": [["Circle", 5.88235294], ["Triangle", 4.76190476],["Square", 0],  ["Pentagon", 14.28571429 ], ["Rhombus", 8.], 
                         ["Star", 14.28571429], ["Trefoil", 0. ], ["Heart", 12.5]],
            },
            {
                "name": "Artificial Neural Network",
                "id": "ANN",
                "data": [["Circle", 0], ["Triangle", 0],["Square", 0], ["Pentagon", 0], ["Rhombus", 0], 
                          ["Star", 0], ["Trefoil", 0], ["Heart", 0]],
            },
            // {
            //     "name": "K Means (Unsupervised)",  //total error rate = 27.34375
            //     "id": "K-means",
            //     "data": [["Circle", 28.749999999999996],["Heart", 5.0], ["Pentagon", 90.0 ], ["Rhombus", 12.5], 
            //              ["Square", 51.24999999999999], ["Star", 8.75], ["Trefoil", 2.5 ], ["Triangle", 20.0]],
            // },
        ]
    }
});