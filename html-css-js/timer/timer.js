document.addEventListener("DOMContentLoaded", function(event) {
	var form = document.getElementbyId("timerForm");
	
	form.setTimer.onclick = function(event){
		if (event.target.id == "setTimer") {
	var timeleft = customTime()
}
}
});

var timeleft = 0;
var userhr = 0;
var usermin = 0;
var usersec = 0;

function customTime() {
	userhr = document.getElementbyId("hour");
	usermin = document.getElementbyId("minute");
	usersec = document.getElementbyId("minute");
	console.log(userhr, usermin, usersec);
	setZero(userhr);
	setZero(usermin);
	setZero(usersec);
	console.log(userhr, usermin, usersec);
	timeleft = (userhr* 3600000) + (usermin *60000) + (usersec * 1000);
	console.log(timeleft);
	return timeleft
};

function setZero(timeset) {
	if(isNaN(timeset)) {
		timeset = 0;
		return timeset }
	else {
		return timeset
	}
};

//var usersubmit = document.getElementbyId("setTimer");
//document.getElementById("setTimer").onclick.customTime();


//function getTimeLeft(hour, minute, second)



/*function getTime() {
	var timerTime = parseFloat(document.getElementbyId("hour").value) * 360000000 +
		parseFloat(document.getElementbyId("minute").value) * 60000 +
		parseFloat(document.getElementbyId("second").value) * 1000;
	console.log(timerTime);
	return timerTime
}



 function setTimeLeft(hms, mms, sms) {
	//document.getElementbyId("setTimer").submit();
	hms = hms*3600000;
	console.log(hms);
	mms = mms*60000;
	console.log(mms);
	sms = sms*1000;
	console.log(sms);
	var timerTime = hms + mms + sms;
	var timeleft = timerTime;
	console.log(timerTime);
	console.log(timeleft);
	return timeleft
}

/*function getTime() {
// converts user input to milliseconds.
var hms = document.getElementbyId("hour");
var mms = document.getElementbyId("min");
var sms = document.getElementbyId("sec");
consol.log(hms, mms, sms);
return hms, mms, sms
}


function count(timeleft) {
	var timeleft = timerTime //creates timeleft
	var endtime = new Date(Date.parse(new Date()) + timeleft) // sets an endtime at START
	timeleft = Date.parse(endtime) - Date.parse(new Date) // re-evaluates time left
}

function onemin(evt) {
	self.document.getElementbyId("displaymin").innerHTML = 01;
	self.console.log("ok");
}


//////////// DISPLAY ///////////////////

// each variable defined independently, no waterfall.
// finds number of hours left. rounds down (if not at least 1, will show 0)
var hrs = Math.floor(timeleft/3600000)

 // takes remainder after hours. divides by 60000 to find minutes. rounds down
var min = Math.floor((timeleft%3600000)/60000)

// takes remainder after minutes. divides by 1000 to find seconds. rounds down
var sec = Math.floor((timeleft%60000)/1000)
*/