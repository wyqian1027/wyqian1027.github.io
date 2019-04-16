// var lon = document.getElementById("lon");
// var lat = document.getElementById("lat");
// var weather = document.getElementById("weather");
var API_KEY = "c44ef930e10a6f991caa29281f314605";
var currentInfo = document.querySelector("#current-info");
var cityID;
$.ajaxSetup({
  async: false
});

function getWeatherURL(lon, lat){
  return `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}`;
}

function getForecastURL(lon, lat){
  return `https://api.openweathermap.org/data/2.5/forecast?lat=${lat}&lon=${lon}&appid=${API_KEY}`;
}

function K2C(k, dec=2){
  return (k-273.15).toFixed(dec);
}

function showPosition(position) {
  $("#lon").html(position.coords.latitude.toFixed(2));
  $("#lat").html(position.coords.longitude.toFixed(2));
  console.log(position.coords.latitude);
  console.log(position.coords.longitude);
  getWeather(position.coords.longitude, position.coords.latitude);
  getForecast(position.coords.longitude, position.coords.latitude);
  makeForecast();
}

function getTime(unixFormat){
  var d = new Date(1000*unixFormat);
  var hour = d.getHours()+"";
  var min = d.getMinutes()+"";
  if (hour.length == 1) hour = "0"+hour;
  if (min.length == 1) min = "0"+min;
  return hour+":"+min;
}

function getWeatherIconFromID(id){
  return `url(http://openweathermap.org/img/w/${id}.png)`;
}

function getDateAndTime(unixFormat){
  var d = new Date(1000*unixFormat);
  return d.toLocaleTimeString() + ", " + d.toDateString();
}

function getDateTimeShort(unixFormat){
  var d = new Date(1000*unixFormat);
  var dstr = d.toDateString();
  return dstr.slice(0,4)+d.getHours()+":00 "+(dstr.slice(4,8))+d.getDate();
}

function getDay(unixFormat){
  return (new Date(1000*unixFormat)).toDateString().slice(0,4);
}

function getHour(unixFormat){
  return (new Date(1000*unixFormat)).getHours()+":00";
}

function getMonthDate(unixFormat){
  var d = new Date(1000*unixFormat);
  return d.toDateString().slice(4,8)+d.getDate();
}

function Angle2Dir(angle){
  //simply 8 possible directions, N, NE, E, SE, S, SW, W, NW
  var x = parseInt(angle);
  var dirs = ["North", "Northeast", "East", "Southeast", "South", "Southwest", "West", "Northwest"];
  if (x >= 360-22.5) return "North";
  return dirs[parseInt((x+22.5) / 45)];
}

function getWindChill(temp, windspd, digit){
  //temp in celius, windsp in m/s
  var res = 13.12+0.6215*(temp)-11.37*(windspd*3.6)**(0.16)+0.3965*(temp)*(windspd*3.6)**0.16;
  if (digit == 0) {
    return Math.floor(res);
  } else {
    return res.toFixed(digit);
  }
}


//API CALL with getJSON
function getWeather(lon, lat){
  $.getJSON(
    getWeatherURL(lon, lat),
    function(data) {

      cityID = data.id;
      var windspd = data.wind.speed;
      var curTemp = K2C(data.main.temp,0);
      
      // $("#obs-loc").html(data.name);
      // $("#cur-weather").html(data.weather[0].main+' ( '+data.weather[0].description + ' )');
      // $('#cur-time').html(getDateAndTime(data.dt));
      // $("#cur-hum").html(data.main.humidity+' %');
      // $('#cur-windspd').html(windspd + ' m/s');
      // $('#cur-windir').html(Angle2Dir(data.wind.deg));
      // $("#cur-temp").html(curTemp+' &#176;C');
      // $("#cur-wc-temp").html(getWindChill(curTemp, windspd, 0)+' &#176;C');
      // $("#high-temp").html(K2C(data.main.temp_max)+' &#176;C');
      // $("#low-temp").html(K2C(data.main.temp_min)+' &#176;C');
      // $("#sun-rise").html(getTime(data.sys.sunrise));
      // $("#sun-set").html(getTime(data.sys.sunset));
      console.log(data.weather[0].main)
      currentInfo.innerHTML = `
      <div class='info'><span id='cur-weather'>${data.weather[0].main} ( ${data.weather[0].description} )</span> &nbsp; &nbsp; - &nbsp; &nbsp; <span id='obs-loc'>${data.name}</span>  &nbsp; &nbsp; - &nbsp; &nbsp; <span id='cur-time'>${getDateAndTime(data.dt)}</span></div>
      <br><div class='info'><i class="fas fa-thermometer-half" style="font-size: 0.7em"></i>&nbsp;&nbsp;<span id='cur-temp'>${curTemp} &#176;C</span> &nbsp; (<span id='cur-wc-temp'>${getWindChill(curTemp, windspd, 0)} &#176;C</span>)&nbsp; &nbsp; &nbsp; &nbsp;
      <i class="fas fa-wind" style="font-size: 0.7em"></i> &nbsp;  <span id='cur-windspd'>${windspd} m/s</span>&nbsp; &nbsp; &nbsp;  &nbsp;
      <i class="fas fa-tint" style="font-size: 0.7em"></i> &nbsp;  <span id='cur-hum'>${data.main.humidity+' %'}</span></div>
      <br>
      `;
    }
  );
}

var forecasts = [];
class WeatherItem { //built base on API returned items in "list"
  constructor(item, index){
    this.index = index;
    this.time = item.dt;
    this.temp = K2C(item.main.temp);
    this.temp_min = K2C(item.main.temp_min);
    this.temp_max = K2C(item.main.temp_max);
    this.pressure = item.main.pressure;
    this.humidity = item.main.humidity;
    this.weather = item.weather[0].main;
    this.weatherDesc = item.weather[0].description;
    this.windspd = item.wind.speed;
    this.windeg = item.wind.deg;
    this.windir = Angle2Dir(item.wind.deg);
    this.rainvol = ((item.rain == undefined || item.rain["3h"] == undefined) ? 0 : item.rain["3h"]); //mm
    this.iconID = item.weather[0].icon;
  }
}
//API CALL with getJSON
function getForecast(lon, lat){
  $.getJSON(
    getForecastURL(lon, lat),
    function(data) {
      data.list.forEach(function(el, ind){
        forecasts.push(new WeatherItem(el, ind));
      });
    }
  );
}


function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else { 
    alert("Geolocation is not supported by this browser.");
  }
}


function makeForecast(){
  
  var temps = [];
  var categories = [];
  var rainfalls = [];
  var weathers = [];
  var weatherIcons = [];
  var windspds = [];
  var windchilltemps = [];
  for (var i=0; i<24; i++){
    el = forecasts[i];
    temps.push(parseFloat(el.temp));
    categories.push(getDay(el.time)+" "+getHour(el.time)+"<br>"+getMonthDate(el.time));
    rainfalls.push(el.rainvol);
    weathers.push([el.weather, el.weatherDesc]);
    weatherIcons.push({
      y: parseFloat(el.temp),
      marker: {
        symbol:  getWeatherIconFromID(el.iconID)
      }
    });
    windspds.push(el.windspd);
    windchilltemps.push(parseFloat(getWindChill(temps[i], windspds[i], 2)));
    
  };
  // console.log(windchilltemps)

  var weekdayColor = {
    'Mon' : '#FF4C40',  
    'Tue' : '#0060E3',  
    'Wed' : '#347E55',  
    'Thu' : '#7853DB',  
    'Fri' : '#FF4C40',  
    'Sat' : '#0060E3',  
    'Sun' : '#347E55',  
  };
  
  Highcharts.chart('forecasts', {
      // colors : ['#8d4654', "rgb(184, 184, 242)", "rgb(242, 184, 184)", "rgb(184, 242, 184)"],
      chart: {
          zoomType: 'xy',
          style: {
            fontSize: '20px'
          },
          // backgroundColor: '#F1FFEE'
          backgroundColor: '#FFFFFF',
          // borderWidth: 1
      },
      title: {
          text: 'Next 3-Day Weathers (on 3-hour interval)<br>',
          style: {
            // color: 'brown',
            fontSize: '25px',
            // fontWeight: 'bold',
          },
          margin: 45
      },
      subtitle: {
          text: 'Source: OpenWeatherMap.com',
          style: {
            color: 'grey',
            fontSize: '15px',
            // fontWeight: 'bold',
          }
      },
      xAxis: [{
          categories: categories,
          // crosshair: true,
          labels:{
            step: 2, // this will show every second label
            style: {
              fontSize: '13px',
              fontWeight: 'bold',
            },
            formatter: function () {
                if (this.value.slice(0,3) in weekdayColor) {
                    return `<span style="fill: ${weekdayColor[this.value.slice(0,3)]};">${this.value}</span>`;
                } else {
                    return this.value;
                }
            }
          },
          
          
      }],
      yAxis: [{ // Primary yAxis
          labels: {
              format: "{value} C",
              style: {
                  color: "#FA7D7B",
                  fontSize: '20px'
              }
          },
          title: {
              text: 'Temperature',
              style: {
                  color: "#FA7D7B"
              }
          }
      }, { // Secondary yAxis
          title: {
              text: 'Rainfall',
              style: {
                  color: "#76A5E6"
              }
          },
          labels: {
              format: '{value} mm',
              style: {
                  color: "#76A5E6",
                  fontSize: '20px'
              },
              formatter: function () {
                  return `<span>${this.value.toFixed(1)} mm</span>`;
              }
          },
          opposite: true
      }],
      tooltip: {
          shared: true,
          style: {
            fontSize: '15px'
          }
      },
    //   tooltip: {
    //     headerFormat: '<span style="font-size:15px"># Players with ${point.key}</span><table>',
    //     pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
    //         '<td style="padding:0"><b>{point.y:.f}</b></td></tr>',
    //     footerFormat: '</table>',
    //     shared: true,
    //     useHTML: true
    // },
      
      
      legend: {
          layout: 'vertical',
          align: 'left',
          x: 900,
          verticalAlign: 'top',
          y: 40,
          floating: true,
          backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || 'rgba(255,255,255,0.25)',
          itemStyle: {
            // color: '#000000',
            fontSize: '16px'
          }
      },
      series: [{
          name: 'Rainfall',
          type: 'column',
          yAxis: 1,
          data: rainfalls,
          tooltip: {
              valueSuffix: ' mm'
          },
          color: "#C2DAFC",
  
      }, {
          name: 'Temperature',
          type: 'spline',
          data: weatherIcons,
          tooltip: {
              valueSuffix: 'C'
          },
          color: "#FA695C"
      }, {
        name: 'Wind Chill',
        type: 'spline',
        data: windchilltemps,
        fillColor: 'rgba(28,28,28,0.5)',
        tooltip: {
            valueSuffix: 'C'
        },
        color: "#FFC4BF" ,
        dashStyle: 'longdash'
        
      }]
  });
}


function init(){
  getLocation();
}

init();