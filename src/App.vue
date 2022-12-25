<template>
  <div id="app">
    <main>
<!--      <div class="search-box">-->
<!--        <input type="text"-->
<!--               class="search-bar"-->
<!--               placeholder="Search..."-->
<!--               v-model="query"-->
<!--               @keypress="fetchWeather"-->
<!--        />-->
<!--      </div>-->
      <div class="weather-warp">
          <div class="location-box">
            <div class="location">{{ this.city, this.region}}</div>
            <div class="date">{{this.date}}</div>
          </div>
      </div>

        <div class="weather-box">
          <div class="temp">{{ Math.floor(this.city_temperature)}} °C</div>
          <div class="weather">{{this.weather}}</div>
        </div>


        <div class="myhome">
          <div style="display: flex" class="room">
            <div class="label">
              <div class="temp">房间内</div>
            </div>
            <div class="temp-room1">
              <div class="temp">{{ Math.floor(this.room1_temperature) }} °C</div>
            </div>
          </div>
          <div style="display: flex" class="outside">
            <div class="label">
              <div class="temp">房间外</div>
            </div>
            <div class="temp-outdoor">
              <div class="temp">{{ Math.floor(this.outside_temperature) }} °C</div>
            </div>
          </div>
        </div>


    </main>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
// import TheWelcome from './components/TheWelcome.vue'
// import Vue from 'vue'
import axios from 'axios'
// import VueAxios from 'vue-axios'

// Vue.use(VueAxios, axios);
export default {
  name:'app',
  data(){
    return{
      api_key:'5a2464c37a93b560995106345eeaaa99',
      url_base:'https://restapi.amap.com/v3/weather/weatherInfo',
      url_ip_locate:'https://restapi.amap.com/v3/ip',
      query:'',
      province:'',
      region:'',
      city:'',
      city_temperature:0,
      weather:{},
      date:'',
      room1_temperature:'',
      outside_temperature:'',
      timer1:'',/*高德地图的api免费的次数每天好像只要5000,一次是请求两下,这个慢一点*/
      timer2:''/*自己的接口,随便轰炸*/
    }
  },
  methods:{
    // (){},
    fetchWeather(e){
        axios.get(`${this.url_ip_locate}?key=${this.api_key}`).then((res)=>{
          // console.log(res);
          this.city=res.data.city;
          axios.get(`${this.url_base}?city=${res.data.adcode}&key=${this.api_key}`).then((response) => {
            var r=response.data.lives[0];
            // console.log(response);
            this.setResults(r);
          })
        })
      // }
    },
    setResults(results){
      if(results){
            this.city_temperature=results.temperature;
            this.weather=results.weather;
            this.date=results.reporttime;
            this.province=results.province;
            if(this.city!=results.city)
              this.region=results.city;/*有时候city返回回来的是区的名字*/
      }
    },
    pullIndoorWeather(){
      axios.get("http://42.192.227.238/DianDongChe_query/one_sensor_last_data?sensor_name=dht_athome&data_name=temperature")
          .then((res)=>{
        this.room1_temperature=res.data.value;
      });
      axios.get("http://42.192.227.238/DianDongChe_query/one_sensor_last_data?sensor_name=dht_atoutside&data_name=temperature")
          .then((res)=>{
            this.outside_temperature=res.data.value;
          });

    }
  },
  mounted() {
    this.fetchWeather();
    this.pullIndoorWeather();
    this.timer1=setInterval(this.fetchWeather,1000000);
    this.timer2=setInterval(this.pullIndoorWeather,10000);

  },
  beforeDestroy() {
    clearInterval(this.timer1);
    clearInterval(this.timer2);
  }
}
</script>



<style scoped>
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
/*body{*/
/*  !*font-family: 'monserrat',sans-serif;*!*/
/*}*/
#app{
  background-image: url("./assets/cold-bg.jpg");
  background-size: cover;
  background-position: bottom;
  transition: 0.4s;
}
main{
  min-height: 80vh;
  min-width: 80vh;
  padding:25px;
  background-image: linear-gradient(to bottom,rgba(0,0,0,0.25),rgba(0,0,0,0.75));
}

.location-box .location {
  color: #FFF;
  font-size: 32px;
  font-weight: 500;
  text-align: center;
  text-shadow: 1px 3px rgba(0, 0, 0, 0.25);
}
.location-box .date {
  color: #FFF;
  font-size: 20px;
  font-weight: 300;
  font-style: italic;
  text-align: center;
}
.weather-box {
  text-align: center;
}

.weather-box .temp {
  display: inline-block;
  padding: 10px 25px;
  color: #FFF;
  font-size: 102px;
  font-weight: 900;
  text-shadow: 3px 6px rgba(0, 0, 0, 0.25);
  background-color:rgba(255, 255, 255, 0.25);
  border-radius: 16px;
  margin: 30px 0px;
  box-shadow: 3px 6px rgba(0, 0, 0, 0.25);
}
.weather-box .weather {
  color: #FFF;
  font-size: 48px;
  font-weight: 700;
  font-style: italic;
  text-shadow: 3px 6px rgba(0, 0, 0, 0.25);
}
.myhome {
  text-align: center;
}
.myhome .room .temp-room1 .temp {
  display: inline-block;
  padding: 10px 25px;
  color: #FFF;
  font-size: 102px;
  font-weight: 900;
  text-shadow: 3px 6px rgba(0, 0, 0, 0.25);
  background-color:rgba(255, 255, 255, 0.25);
  border-radius: 16px;
  margin: 30px 0px;
  box-shadow: 3px 6px rgba(0, 0, 0, 0.25);
}
.myhome .room .label {
  /*display: inline-block;*/
  /*padding: 10px 25px;*/
  color: #FFF;
  font-size:50px;
  font-weight: 900;
  /*text-shadow: 3px 6px rgba(0, 0, 0, 0.25);*/
  /*background-color:rgba(255, 255, 255, 0.25);*/
  /*border-radius: 16px;*/
  margin: 80px 0px;
  /*margin-right: 80px;*/
  border: 10px;

  /*box-shadow: 3px 6px rgba(0, 0, 0, 0.25);*/
}
.myhome .outside .label {
  /*display: inline-block;*/
  /*padding: 10px 25px;*/
  color: #FFF;
  font-size:50px;
  font-weight: 900;
  /*text-shadow: 3px 6px rgba(0, 0, 0, 0.25);*/
  /*background-color:rgba(255, 255, 255, 0.25);*/
  /*border-radius: 16px;*/
  margin: 80px 0px;
  /*margin-right: 80px;*/
  border: 10px;
  /*box-shadow: 3px 6px rgba(0, 0, 0, 0.25);*/
}
.myhome .outside .temp-outdoor .temp {
  display: inline-block;
  padding: 10px 25px;
  color: #FFF;
  font-size: 102px;
  font-weight: 900;
  text-shadow: 3px 6px rgba(0, 0, 0, 0.25);
  background-color:rgba(255, 255, 255, 0.25);
  border-radius: 16px;
  margin: 30px 0px;
  box-shadow: 3px 6px rgba(0, 0, 0, 0.25);
}

</style>
