/*********TODO************
clean up code, remove old broken dumb stuff.
add more songs, add dropdown menu to select songs.
       isolate playbackRate and play()/pause()/load() functions
       allow to pick countdown songs. (upload maybe? good exercise)
    allow for end of countdown sound options (buzzer, etc)
    KE$HA TIK TOK IS 120BPM!!!!!!!
    M Jackson, don't stop til you get enough
    I believe I can fly is 60BPM (spacejam theme at 0:00:00)

    check timer setting, use song closest to that length. 
    	get a wide range
add loop function.
add pre-set time functions
*/

var hr = 0;
var min = 0;
var sec = 0;
var timeArr = [];
var endTime = 0;
var timeLeft = 0;
var disHour = "";
var disMin = "";
var disSec = "";
var timeLeft = 0;
var halt = false;
var spacejam = false;



document.addEventListener("DOMContentLoaded", function(evt) {

	var frm = document.getElementById("customTime");
	


	frm.submit.onclick = function(evt) {
		if (evt.target.name == "submit") {
			disTimeLeft(convertTime(getTime()));
			timeLeft = convertTime(getTime());
		}
	}

	frm.start.onclick = function(evt) {
		if (evt.target.name == "start") {
			document.getElementById("display").classList.add("wide");
			console.log("STARTED");
			console.log(timeLeft);
			halt = false;
			if (timeLeft === 199600) {
				document.getElementById("fly").playbackRate=1.6;
				document.getElementById("fly").play();
				spacejam = true;
				document.getElementById("display").classList.add("jam");
			}
				else {
				var rateMath = timeLeft/1000;
				console.log(rateMath + " is rateMath");
				var rate = (270/rateMath).toFixed(4);
				console.log(rate + " is playbackRate")
				if (rate > 0.5 && rate < 4) {
					document.getElementById("marvin").playbackRate = rate;
					document.getElementById("marvin").play();
					}
				else if (rate > 4){
					document.getElementById("marvin").playbackRate = 4;
					document.getElementById("marvin").play();
				}	
			}	
			disTimeLeft(timeLeft);
			countdown(timeLeft)
		}
	}

	frm.stop.onclick = function(evt) {
		if (evt.target.name == "stop") {
			halt = true;
			document.getElementById("marvin").pause();
			document.getElementById("marvin").load();
			document.getElementById("fly").pause();
			document.getElementById("spacejam").pause();
			document.getElementById("fly").load();
			document.getElementById("spacejam").load();
			console.log("after halt = true");
			window.setTimeout( function() {
			showTime([0,0,0]);
			console.log("end of stop");
		},999);
			spacejam = false;
			document.getElementById("display").classList.remove("wide", "jam", "red");
		}
	}

	frm.clear.onclick = function(evt) {
		if (evt.target.name == "clear") {
			halt = true;
			console.log("after halt = true");
			window.setTimeout( function() {
			showTime([0,0,0]);
			console.log("end of stop");
			},999);
			document.getElementById("marvin").pause();
			document.getElementById("marvin").load();
			document.getElementById("fly").pause();
			document.getElementById("spacejam").pause();
			document.getElementById("fly").load();
			document.getElementById("spacejam").load();
		document.getElementById("customTime").reset();
		spacejam = false;
		document.getElementById("display").classList.remove("wide", "red", "jam");
		}
	}

});

function getTime() {
	hr = document.getElementById("userHour").value;
	console.log(hr);
	min = document.getElementById("userMin").value;
	console.log(min);
	sec = document.getElementById("userSec").value;
	console.log(sec);
	timeArr = [hr, min, sec];
	return timeArr
}

//function writes times to page
function showTime(timeArr) {
	document.getElementById("disHour").innerHTML = twoDigits(timeArr[0]);
	document.getElementById("disMin").innerHTML= twoDigits(timeArr[1]);
	document.getElementById("disSec").innerHTML = twoDigits(timeArr[2]);	
	console.log(timeArr[2]);
	console.log(document.getElementById("disSec").innerHTML);
}

//function makes two digit numbers out of potentially single digits
function twoDigits(number) {
	var ddnum = "";
	ddnum = ("00" + number).slice(-2);
	console.log(ddnum);
	return ddnum
}

//converts time to milliseconds
function convertTime(timeArr) {
	var hrms = timeArr[0]*3600000;
	console.log(hrms);
	var minms = timeArr[1]*60000;
	console.log(minms);
	var secms = timeArr[2]*1000;
	console.log(secms);
	var time = hrms + minms + secms;
	console.log(time);
	return time
}

//converts timeLeft back in to [hours, minutes, seconds]
function disTimeLeft(timeleft) {
	hr = Math.floor(timeleft/3600000);
	console.log("hours" + hr);
	min = Math.floor((timeleft%3600000)/60000);
	console.log("minutes" + min);
	sec = Math.floor((timeleft%60000)/1000);
	console.log("seconds" + sec);
	disTimeLeftArr = [hr, min, sec]
	console.log(disTimeLeftArr);
	showTime(disTimeLeftArr); 
}


//countdown v 2.0 
function countdown(timeLeft) {
	console.log(timeLeft + " pre-loop")
	if (halt === false) {
	window.setTimeout(function() {
		if (timeLeft > 0) {
			timeLeft = timeLeft - 1000;
			disTimeLeft(timeLeft);
			console.log(timeLeft + " end of if");
			countdown(timeLeft)	
			}
		if (timeLeft > 536000 && timeLeft < 537100) {
			console.log("in marvin if" + timeLeft)
			document.getElementById("marvin").playbackRate=0.5;
			document.getElementById("marvin").play();
		}
		if (timeLeft <= 0) {
			if (spacejam === true) {
				document.getElementById("fly").load();
				document.getElementById("spacejam").play();
			}
		else {
			document.getElementById("display").classList.add("red");
			document.getElementById("marvin").playbackRate=1;
		}
			
		}
		}, 1000);
	}
	else if (halt === true)
		halt = false;
		return
}
