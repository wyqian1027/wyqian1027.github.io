//This js contains usage of Highcharts for three plots used in the html.

// Create the chart
Highcharts.chart('sc2-earnings', {
    // colors: ['#f45b5b', '#8085e9', '#8d4654', '#7798BF', '#aaeeee',
    //     '#ff0066', '#eeaaee', '#55BF3B', '#DF5353', '#7798BF', '#aaeeee'],
        
    colors : ['#8d4654', "rgb(184, 184, 242)", "rgb(242, 184, 184)", "rgb(184, 242, 184)"],
        
    
    chart: {
        // height: (9 / 16 * 100) + '%', // 16:9 ratio,
        type: 'column',
        borderColor: 'black',
        borderWidth: 1,

    },
    title: {
        text: 'Professional Starcraft 2 Player Earning Distributions',
        style: {
            color: 'black',
            fontSize: '20px',
            // fontWeight: 'bold',
        }
    },
    subtitle: {
        text: 'Click the legends to toggle between Starcraft races.',
        style: {
            color: 'black',
            fontSize: '15px'
        }
    },
    xAxis: {
        title: {
            text: 'Earnings (US Dollars)',
            style: {
                fontSize: '20px',
                color: 'black'
            }
        },
        type: 'category',
        labels: {
            style: {
                color: 'black',
                fontSize: '15px'
            }
        },
        categories: [
            '100K',
            '200K',
            '300K',
            '400K',
            '500K',
            '600K',
            '700K',

        ],
        crosshair: true

    },
    yAxis: {
        title: {
            text: '# Counts',
            style: {
                fontSize: '20px',
                color: 'black'
            }
        },
        labels: {
            style: {
                color: 'black',
                fontSize: '12px'
            }
        },
        // max: 15,
        min: 0
    },
    legend: {
        layout: 'horizontal',
        align: 'center',
        verticalAlign: 'top',
        // x: -50,
        y: 50,
        floating: true,
        itemStyle: {
            // color: '#000000',
            fontSize: '16px'
        }

    },
    

    plotOptions: {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        },
        // series: {
        //     borderWidth: 0,
        //     dataLabels: {
        //         // enabled: true,
        //         format: '{point.y:.1f}%',
        //         style: {
        //             fontSize: '15px'
        //         }
        //     }
        // }
    },

    tooltip: {
        headerFormat: '<span style="font-size:15px"># Players with ${point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y:.f}</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    },

    series: [{
        name: 'Total',
        data: [83, 30, 16, 5, 9, 5, 2]

    }, {
        name: 'Terran',
        data: [27, 7, 3, 0, 4, 2, 1 ]

    }, {
        name: 'Zerg',
        data: [24, 12, 9, 3, 2, 1, 1]

    }, {
        name: 'Protoss',
        data: [32, 11, 4, 2, 3, 2, 0]

    }]
    
});




// Create the chart
Highcharts.chart('sc2-country', {
    // colors: ['#f45b5b', '#8085e9', '#8d4654', '#7798BF', '#aaeeee',
    //     '#ff0066', '#eeaaee', '#55BF3B', '#DF5353', '#7798BF', '#aaeeee'],
    
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie',
        // borderColor: 'black',
        // borderWidth: 1,

    },
    title: {
        text: 'Professional Starcraft 2 Player Country Distributions',
        style: {
            color: 'black',
            fontSize: '20px',
            // fontWeight: 'bold',
        }
    },
    // subtitle: {
    //     text: 'Click the legends to toggle between Starcraft races.',
    //     style: {
    //         color: 'black',
    //         fontSize: '15px'
    //     }
    // },
    
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                style: {
                    color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                }
            }
        }
    },
    tooltip: {
        headerFormat: '<span style="font-size:20px; font-weight: bold;">{point.key}</span><table>',
        pointFormat: '<table><tr><td>Count <b>{point.y:.f}</b></td>' +
        '<td>   Percentage <b>{point.percentage:.1f} %</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    },
    // tooltip: {
    //     headerFormat: '<span style="font-size:15px"># Players with ${point.key}</span><table>',
    //     pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
    //         '<td style="padding:0"><b>{point.y:.f}</b></td></tr>',
    //     footerFormat: '</table>',
    //     shared: true,
    //     useHTML: true
    // },

    series: [{
        name: 'Countries',
        colorByPoint: true,
        data: [{
            name: 'South Korea',
            y: 96,
            sliced: true,
            selected: true
        }, {name: 'France', y: 6 }, {name: 'Sweden', y: 5 }, {name: 'Germany', y: 5 }, {name: 'Poland', y: 4 }, {name: 'Ukraine', y: 4 }, {name: 'Netherlands', y: 4 }, {name: 'Finland', y: 3 }, {name: 'Taiwan', y: 3 }, {name: 'Canada', y: 3 }, {name: 'China', y: 3 }, {name: 'United States', y: 2 }, {name: 'Russia', y: 2 }, {name: 'Spain', y: 1 }, {name: 'United Kingdom', y: 1 }, {name: 'Norway', y: 1 }, {name: 'Italy', y: 1 }, {name: 'Canada United States', y: 1 }, {name: 'Peru', y: 1 }, {name: 'Australia', y: 1 }, {name: 'USA', y: 1 }, {name: 'Belgium', y: 1 }, {name: 'France Tunisia', y: 1 }]
    }]
});


Highcharts.chart('sc2-age', {
    colors : ["rgb(184, 184, 242)", "rgb(242, 184, 184)", "rgb(184, 242, 184)"],

    chart: {
        type: 'scatter',
        zoomType: 'xy',
        borderColor: 'black',
        borderWidth: 1,
    },
    title: {
        text: 'Professional Starcraft 2 Tournament Earning Versus Player Age',
        style: {
            color: 'black',
            fontSize: '20px',
            // fontWeight: 'bold',
        }
    },
    subtitle: {
        text: 'Click the legends to view each race.',
        style: {
            color: 'black',
            fontSize: '14px'
        }

    },
    xAxis: {
        title: {
            enabled: true,
            text: 'Player Age (Years)',
            style: {
                fontSize: '20px',
                color: 'black'
            }
        },
        startOnTick: true,
        endOnTick: true,
        showLastLabel: true,
        labels: {
            style: {
                color: 'black',
                fontSize: '14px'
            }
        },
    },
    yAxis: {
        title: {
            text: 'Earnings (US Dollars)',
            style: {
                fontSize: '20px',
                color: 'black'
            }
        },
        labels: {
            style: {
                color: 'black',
                fontSize: '14px'
            }
        },
        // max: 15,
        min: 0
    },
    legend: {
        layout: 'horizontal',
        align: 'center',
        verticalAlign: 'top',
        // x: -50,
        y: 50,
        floating: true,
        backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF',
        // borderWidth: 1,
        itemStyle: {
            // color: '#000000',
            fontSize: '16px'
        }
    },
    plotOptions: {
        scatter: {
            marker: {
                radius: 5,
                states: {
                    hover: {
                        enabled: true,
                        lineColor: 'rgb(100,100,100)'
                    }
                }
            },
            states: {
                hover: {
                    marker: {
                        enabled: true
                    }
                }
            },
            tooltip: {
                headerFormat: '<span style="font-size:18px; font-weight: bold; color:{series.color}">{series.name} Player</span><table><br>',
                // pointFormat: '{point.x:.1f} Years, {point.y:.f} US Dollars'
                pointFormat: '<table style="font-size:16px;"><tr><td >Age: {point.x:.1f} Years</td> <br>' +
                '<td style="font-size:16px;">Earnings:  ${point.y:.f} </td></tr>',
                footerFormat: '</table>',
                shared: true,
                useHTML: true
            },
            // tooltip: {
            //     headerFormat: '<span style="font-size:20px; font-weight: bold;">{point.key}</span><table>',
            //     pointFormat: '<table><tr><td>Count <b>{point.y:.f}</b></td>' +
            //     '<td>   Percentage <b>{point.percentage:.1f} %</b></td></tr>',
            //     footerFormat: '</table>',
            //     shared: true,
            //     useHTML: true
            // },
        }
    },
    // '#f45b5b', '#8085e9', '#8d4654'
    series: [{
        name: 'Terran',
        color: "rgb(184, 184, 242)", //'rgba(244, 91, 91, 0.5)',
        data: [[21.613698630136987, 692700.0],
 [24.473972602739725, 543280.0],
 [26.5972602739726, 196551.0],
 [25.624657534246577, 514148.0],
 [22.364383561643837, 66597.0],
 [25.838356164383562, 403469.0],
 [25.663013698630138, 212426.0],
 [26.67945205479452, 91339.0],
 [26.208219178082192, 85196.0],
 [24.186301369863013, 291935.0],
 [29.07123287671233, 146773.0],
 [30.364383561643837, 406444.0],
 [28.073972602739726, 402867.0],
 [31.15068493150685, 256207.0],
 [30.69041095890411, 455455.0],
 [26.312328767123287, 197168.0],
 [28.28767123287671, 43933.0],
 [23.328767123287673, 119362.0],
 [31.197260273972603, 34943.0],
 [26.205479452054796, 17319.0],
 [27.632876712328766, 143886.0],
 [25.208219178082192, 11768.0],
 [28.315068493150687, 66808.0],
 [25.06027397260274, 135177.0],
 [28.08219178082192, 102927.0],
 [23.77260273972603, 64060.0],
 [24.28767123287671, 70097.0],
 [26.405479452054795, 24276.0],
 [28.816438356164383, 58452.0],
 [26.767123287671232, 33399.0],
 [28.07945205479452, 33683.0],
 [35.09041095890411, 42803.0],
 [30.386301369863013, 39812.0],
 [31.216438356164385, 5932.0],
 [32.18630136986302, 37743.0],
 [32.917808219178085, 12247.0],
 [29.413698630136988, 28060.0],
 [32.21643835616438, 40446.0],
 [24.435616438356163, 80207.0],
 [31.471232876712328, 21152.0],
 [30.29041095890411, 72148.0],
 [29.126027397260273, 34246.0],
 [24.065753424657533, 30729.0]]
    },
    {
        name: 'Zerg',
        color: "rgb(242, 184, 184)" ,//'rgba(128, 133, 233, .5)',
        data: [[23.424657534246574, 455443.0],
 [25.153424657534245, 623797.0],
 [22.156164383561645, 475744.0],
 [27.24931506849315, 154691.0],
 [29.167123287671235, 224593.0],
 [26.589041095890412, 114583.0],
 [20.964383561643835, 590785.0],
 [22.832876712328765, 279232.0],
 [26.457534246575342, 382305.0],
 [27.76986301369863, 260073.0],
 [28.953424657534246, 80601.0],
 [31.153424657534245, 249874.0],
 [23.504109589041096, 77512.0],
 [25.235616438356164, 299981.0],
 [23.93972602739726, 279866.0],
 [27.057534246575344, 32157.0],
 [28.61917808219178, 376720.0],
 [32.153424657534245, 158561.0],
 [16.684931506849313, 42590.0],
 [26.912328767123288, 113163.0],
 [26.583561643835615, 368349.0],
 [27.515068493150686, 146568.0],
 [36.24931506849315, 285672.0],
 [33.62465753424657, 100005.0],
 [24.904109589041095, 22908.0],
 [26.9013698630137, 178248.0],
 [27.186301369863013, 98537.0],
 [28.13972602739726, 76610.0],
 [27.106849315068494, 64895.0],
 [33.35342465753425, 75333.0],
 [24.64109589041096, 39993.0],
 [32.23013698630137, 49672.0],
 [28.660273972602738, 100471.0],
 [24.12876712328767, 69335.0],
 [25.994520547945207, 293263.0],
 [32.24109589041096, 28023.0],
 [28.87123287671233, 52896.0],
 [32.772602739726025, 72021.0],
 [27.27123287671233, 26189.0],
 [28.263013698630136, 185247.0],
 [32.156164383561645, 137930.0],
 [21.24109589041096, 207050.0],
 [25.627397260273973, 73562.0],
 [28.526027397260275, 23267.0],
 [30.13150684931507, 112458.0],
 [26.586301369863012, 7572.0],
 [27.45205479452055, 10695.0],
 [25.495890410958904, 105804.0],
 [32.66027397260274, 37147.0],
 [29.553424657534247, 65625.0],
 [25.983561643835618, 20846.0],
 [27.945205479452056, 29644.0]]

    }, {
        name: 'Protoss',
        color: "rgb(184, 242, 184)", //'rgba(141, 70, 84,0.5)',
        data: [[26.81917808219178, 437546.0],
 [26.663013698630138, 418510.0],
 [27.284931506849315, 382541.0],
 [24.791780821917808, 178625.0],
 [26.56986301369863, 241605.0],
 [26.55890410958904, 281328.0],
 [24.96164383561644, 143798.0],
 [24.542465753424658, 360914.0],
 [25.397260273972602, 598373.0],
 [23.041095890410958, 128937.0],
 [21.054794520547944, 405853.0],
 [27.731506849315068, 508202.0],
 [26.745205479452054, 91724.0],
 [28.991780821917807, 177412.0],
 [22.03835616438356, 128198.0],
 [25.065753424657533, 21793.0],
 [28.76164383561644, 265498.0],
 [28.78904109589041, 112293.0],
 [28.824657534246576, 111745.0],
 [23.413698630136988, 131647.0],
 [33.465753424657535, 27354.0],
 [21.764383561643836, 121429.0],
 [25.235616438356164, 192905.0],
 [25.041095890410958, 224528.0],
 [28.156164383561645, 80941.0],
 [31.610958904109587, 94026.0],
 [32.83561643835616, 60248.0],
 [27.60821917808219, 94975.0],
 [29.882191780821916, 72428.0],
 [24.115068493150684, 59192.0],
 [29.835616438356166, 150475.0],
 [26.235616438356164, 42687.0],
 [26.676712328767124, 92726.0],
 [25.736986301369864, 13366.0],
 [24.616438356164384, 93375.0],
 [29.92876712328767, 11835.0],
 [25.778082191780822, 7063.0],
 [32.104109589041094, 71224.0],
 [23.7013698630137, 91173.0],
 [27.10958904109589, 41084.0],
 [38.323287671232876, 55304.0],
 [23.33150684931507, 88843.0],
 [27.632876712328766, 32648.0],
 [31.96164383561644, 28736.0],
 [26.578082191780823, 47364.0],
 [30.791780821917808, 86024.0],
 [30.397260273972602, 31226.0],
 [27.40821917808219, 36949.0],
 [26.435616438356163, 21033.0],
 [28.378082191780823, 44400.0],
 [29.34794520547945, 28930.0],
 [31.561643835616437, 17917.0]]

    }]
});

