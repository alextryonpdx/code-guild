/*********TODO************
clean up code, remove old broken dumb stuff.
add more songs, add dropdown menu to select songs.
       isolate playbackRate and play()/pause()/load() functions
       allow to pick countdown songs.
    allow for end of countdown sound options (buzzer, etc)
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

//var counterWorker = undefined;


document.addEventListener("DOMContentLoaded", function(evt) {

	var frm = document.getElementById("customTime");
	


	frm.submit.onclick = function(evt) {
		if (evt.target.name == "submit") {
			disTimeLeft(convertTime(getTime()));
			//showTime(getTime());
			//convertTime(getTime());
			timeLeft = convertTime(getTime());
		}
	}

	frm.start.onclick = function(evt) {
		if (evt.target.name == "start") {
			document.getElementById("display").classList.add("wide");
			console.log("STARTED");
			console.log(timeLeft);
			halt = false;
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
			disTimeLeft(timeLeft);
			countdown(timeLeft)
		}
	}

	frm.stop.onclick = function(evt) {
		if (evt.target.name == "stop") {
			halt = true;
			document.getElementById("marvin").pause();
			document.getElementById("marvin").load();
			console.log("after halt = true");
			window.setTimeout( function() {
			showTime([0,0,0]);
			console.log("end of stop");
		},999);
			document.getElementById("display").classList.remove("wide", "red");
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
		document.getElementById("customTime").reset();
		document.getElementById("display").classList.remove("wide", "red");
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
// WHY WONT IT DESPLAY AS TIME COUNTS DOWN?
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
	/*
	document.getElementById("disHour").innerHTML = twoDigits(hr);
	document.getElementById("disMin").innerHTML= twoDigits(min);		
	document.getElementById("disSec").innerHTML = seconds;
	*/
	};
	//timeArr = [hr, min, sec];
	//console.log(timeArr);
	//showTime(timeArr);


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
		if (timeLeft > 536000 && timeLeft < 537100 ) {
			console.log("in marvin if" + timeLeft)
			document.getElementById("marvin").playbackRate=0.5;
			document.getElementById("marvin").play();
		}
		if (timeLeft <= 0) {
			document.getElementById("display").classList.add("red");
			document.getElementById("marvin").playbackRate=1;
		}
		}, 1000);
	}
	else if (halt === true)
		halt = false;
		return
}


/*
//countdown v 1.0 with some prooooooblems//
function countdown(endtime) {
			//setInterval(function(){twoDigits(disTimeLeft()); }, 1000);
			while (Date.parse(new Date) < endTime) {
				//console.log("waiting");
				timeLeft = endTime - (Date.parse(new Date));
				console.log(timeLeft);
				disTimeLeft(timeLeft);
				//if (halt = true) {
				//	break

				}
				/*if (timeLeft === 1000){
					alert("One Second")
				}
			
			
			alert(" Time's up!");

			};
			//setInterval(function(){ alert("Hello"); }, 3000);
/*
function findEndTime(time) {
var endTime = Date.parse(new Date()) + time;
return endTime
}

function findTimeLeft(endtime) {
	timeLeft = endtime - Date.parse(new Date());
	//console.log(timeLeft);
	return timeLeft
}
*/


/*
function startWorker() {
	console.log(counterWorker);
    if(typeof(Worker) !== "undefined") {
        if(typeof(counterWorker) == "undefined") {
            counterWorker = new Worker("worker.js");
            console.log(typeof(counterWorker))
        }
        //counterWorker.onmessage = function(event) {
        //    console.log("worker")};
        
    } else {
        console.log("Sorry, your browser does not support Web Workers...");
    }
    

function stopWorker() { 
    counterWorker.terminate();
    counterWorker = undefined;
}

counterWorker.onmessage = function(timeLeft) {
		disTimeLeft(timeLeft);
		console.log(timeLeft);
		console.log(typeof(timeLeft));
		console.log(timeLeft.attributes)
	}

}
*/