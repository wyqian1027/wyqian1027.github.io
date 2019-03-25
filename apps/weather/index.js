// var lon = document.getElementById("lon");
// var lat = document.getElementById("lat");
// var weather = document.getElementById("weather");
var API_KEY = "c44ef930e10a6f991caa29281f314605";
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



//API CALL with getJSON
function getWeather(lon, lat){
  $.getJSON(
    getWeatherURL(lon, lat),
    function(data) {

      cityID = data.id;
      
      $("#obs-loc").html(data.name);
      $("#cur-weather").html(data.weather[0].main+', '+data.weather[0].description);
      $("#cur-hum").html(data.main.humidity+' %');
      $('#cur-windspd').html(data.wind.speed + ' m/s');
      $('#cur-windir').html(Angle2Dir(data.wind.deg));
      $('#cur-time').html(getDateAndTime(data.dt));
      
      $("#cur-temp").html(K2C(data.main.temp,0)+' &#176;C');
      $("#high-temp").html(K2C(data.main.temp_max)+' &#176;C');
      $("#low-temp").html(K2C(data.main.temp_min)+' &#176;C');
      
      $("#sun-rise").html(getTime(data.sys.sunrise));
      $("#sun-set").html(getTime(data.sys.sunset));
      
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
    this.rainvol = (item.rain["3h"] == undefined ? 0 : item.rain["3h"]); //mm
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
  };

  Highcharts.chart('forecasts', {
      // colors : ['#8d4654', "rgb(184, 184, 242)", "rgb(242, 184, 184)", "rgb(184, 242, 184)"],
      chart: {
          zoomType: 'xy',
          style: {
            fontSize: '30px'
          }
      },
      title: {
          text: 'Prediction on Next 5-Day Weathers',
          style: {
            color: 'black',
            fontSize: '30px',
            // fontWeight: 'bold',
          }
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
              fontSize: '15px',
              // fontWeight: 'bold',
            }
          },
          
      }],
      yAxis: [{ // Primary yAxis
          labels: {
              format: "{value} C",
              style: {
                  color: Highcharts.getOptions().colors[1],
                  fontSize: '25px'
              }
          },
          title: {
              text: 'Temperature',
              style: {
                  color: Highcharts.getOptions().colors[1]
              }
          }
      }, { // Secondary yAxis
          title: {
              text: 'Rainfall',
              style: {
                  color: Highcharts.getOptions().colors[0]
              }
          },
          labels: {
              format: '{value} mm',
              style: {
                  color: Highcharts.getOptions().colors[0],
                  fontSize: '20px'
              }
          },
          opposite: true
      }],
      tooltip: {
          shared: true,
          style: {
            fontSize: '20px'
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
          x: 120,
          verticalAlign: 'top',
          y: 100,
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
          }
  
      }, {
          name: 'Temperature',
          type: 'spline',
          data: weatherIcons,
          tooltip: {
              valueSuffix: 'C'
          }
      }]
  });
}


function init(){
  getLocation();
}

init();