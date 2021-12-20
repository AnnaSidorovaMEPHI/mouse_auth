<template>
  <div class="container">
  <span id='timer-counter' style='color:red;font-size:150%;font-weight:bold;'></span>
    <h1 style="color: #000080;">Личный кабинет</h1>
    <br>
  	<img align=right src="~/static/img/photo.jpg" alt="" height="150px" width="150px" display="inline-block">
  	<br>
  	<h2 align=justify>John Smith</h2>
  	<h3 align=justify>Doctor</h3>
  <p id="log"></p>
  </div>
</template>


<script>
import axios from "axios";
export default {
  data: () => ({
  startdate: "",
  clockStart: null,
  timeOnPage: 0,
  tempTimeOnPage: 0,
  tempSecs: 0,
  time_for_measure: 10, //ВРЕМЯ ОТПРАВКИ
  formData: null
  }),
  created() {},

  methods: {

  	initStopwatch() {
  	this.thisTime = new Date();
  	return (this.thisTime.getTime() - this.clockStart)/1000;
	},
	getSecs() {
	  let tSecs = Math.round(this.initStopwatch());
	  let iSecs = tSecs % 60;
	  let iMins = Math.round((tSecs-30)/60);
	  let sSecs ="" + ((iSecs > 9) ? iSecs : "0" + iSecs);
	  let sMins ="" + ((iMins > 9) ? iMins : "0" + iMins);
	  //console.log("Time in this page:"+sMins+":"+sSecs);
	  // Считаем секунды
	  return tSecs;
	}
  },
  mounted() {
  	  var ref = this;
  	  // for data section: initial form_Data
  	  const formData = new FormData();
  	  ref.formData = formData;
	  ref.startdate = new Date();
	  ref.clockStart = ref.startdate.getTime();

	  // Измеряем раз в секунду, а потом захватим с частотой, которая нужна
	  setInterval(function(){
		  if (!document.hidden){
		  // если страница открыта
		  	ref.tempSecs = ref.getSecs();
		  	ref.timeOnPage += 1; // интервал - секунда
		  	console.log("User is here, time: " + ref.timeOnPage);

		  	} else {
			        ref.tempSecs = 0;
			        console.log("User is on other page, time: " + ref.timeOnPage);
			        let CurTime = new Date();
			        ref.clockStart = CurTime;
		        }

		console.log(ref.timeOnPage)
			
		}, 1000);

	// Движения мыши
	var totalX = 0;
	var totalY = 0;
	var moveX = 0;
	var moveY = 0;
	let time_for_mv = 10; //ВРЕМЯ ОТПРАВКИ

	document.addEventListener("mousemove", function(ev){
	    totalX += Math.abs(ev.movementX);
	    totalY += Math.abs(ev.movementY);
	    moveX += ev.movementX;
	    moveY += ev.movementY;
	}, false);

	// Клики
	let count_left = 0;
	let count_right = 0;
	let time_for_cl = 10; //ВРЕМЯ ОТПРАВКИ
	let button = document.querySelector('#button');
	let log = document.querySelector('#log');
	document.addEventListener('mouseup', logMouseButton);

	function logMouseButton(e) {
	  if (typeof e === 'object') {
	    switch (e.button) {
	      case 0:
	        //console.log('Left button clicked.');
	        count_left ++;
	        //console.log('Number of clicks on the left key: '+count_left);
	        break;
	      case 1:
	        //console.log('Middle button clicked.');
	        break;
	      case 2:
	        //console.log('Right button clicked.');
	        count_right ++;
	        //console.log('Number of clicks on the right key: '+count_right);
	        break;
	      default:
	        //console.log(`Unknown button code: ${e.button}`);
	    }
	  }
	}

	// Сбор
	setInterval(function(){

	    // console.log(`Speed of the moving X: ${totalX}px/s, Y: ${totalY}px/s`);
	    // console.log(`Movement of the mouse X: ${moveX}px/s, Y: ${moveY}px/s`);
	    // ???

	    ref.formData.append('time', ref.timeOnPage);
	    ref.formData.append('speed_of_movement_X', totalX);
	    ref.formData.append('speed_of_movement_Y', totalY);
	    ref.formData.append('movement_X', moveX);
		ref.formData.append('movement_Y', moveY);
	    moveX = moveY = totalX = totalY = 0;
	}, 1000*ref.time_for_measure);

	let myGreeting = setInterval(function logMouseButton() {
	  let speed_of_clicks_r=count_right/ref.timeOnPage;
	  let speed_of_clicks_l=count_left/ref.timeOnPage;
	  //console.log('Speed of the right clicking: '+speed_of_clicks_r);
	  //console.log('Speed of the left clicking: '+speed_of_clicks_l);
	  //formData['speed_of_clicks_r'] = speed_of_clicks_r;
	  //formData['speed_of_clicks_l'] = speed_of_clicks_l;
	  ref.formData.append('speed_of_clicks_r', speed_of_clicks_r);
	  ref.formData.append('speed_of_clicks_l', speed_of_clicks_l);


      axios({
        method: "POST",
        url: "https://192.168.137.1:5000/",
        data: ref.formData,
        headers: {
          "content-type": 'multipart/form-data;',
          'Access-Control-Allow-Origin': '*',
        }
      })
        .then(response => {if (response.data === "True") {
          alert("OK")
        } else {
          alert(ref.formData);
          console.log(response);
        }})
        .catch(error => console.log(error));
	 }, ref.time_for_measure*1000)
	
	setInterval(function(){
		}, 1000*ref.time_for_measure);
	},

	// Запись
	  layout: "main"
	};
</script>

<style></style>
