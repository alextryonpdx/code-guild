// This event called when the DOM is fully loaded and parsed 
document.addEventListener("DOMContentLoaded", function (event) {

   // Get the FORM 
   var frm = document.getElementById('calcform');

   // Attach an event handler for the click event 
   //frm.addbutton.onclick = calculate;
   frm.clearbutton.onclick = function(evt) {
      document.getElementById("operator").innerHTML = "( )";
      evt.preventDefault();   
      document.getElementById("result").innerHTML = "...";
      evt.preventDefault();
      document.getElementById("calcform").reset()

   }
   frm.addbutton.onclick = function(evt) {
      
      if(evt.target.name == 'addbutton') {
         var result = calcAddResult(frm.input_a.value, frm.input_b.value);
      }
      document.getElementById("operator").innerHTML = "+";
      evt.preventDefault();   
      document.getElementById("result").innerHTML = result;
      evt.preventDefault();
   }

   frm.subbutton.onclick = function(evt) {

      if(evt.target.name == 'subbutton') {
         var result = calcSubResult(frm.input_a.value, frm.input_b.value);
      }
      document.getElementById("operator").innerHTML = "-";
      evt.preventDefault(); 
      document.getElementById("result").innerHTML = result;
      evt.preventDefault();
   }

   frm.multbutton.onclick = function(evt) {

      if(evt.target.name == 'multbutton') {
         var result = calcMultResult(frm.input_a.value, frm.input_b.value);
      }
      document.getElementById("operator").innerHTML = "*";
      evt.preventDefault(); 
      document.getElementById("result").innerHTML = result;
      evt.preventDefault();
   }

   frm.divbutton.onclick = function(evt) {

      if(evt.target.name == 'divbutton') {
         var result = calcDivResult(frm.input_a.value, frm.input_b.value);
      }
      document.getElementById("operator").innerHTML = "/";
      evt.preventDefault(); 
      document.getElementById("result").innerHTML = result;
      evt.preventDefault();
   }
});

function inputCheck (fnum, snum) {
         if (isNaN(parseFloat(fnum)) || isNaN(parseFloat(snum))) {
            console.log("NaN!");
            document.getElementById("result").innerHTML = "!!!ERROR!!!";
            evt.preventDefault();
         }
         else {
            console.log("not NaN")
            return fnum, snum
         }
}

function calcAddResult(fnum, snum) {
         inputCheck(fnum, snum);
         var a = parseFloat(fnum);
         var b = parseFloat(snum);
         return a + b;
      }

function calcSubResult(fnum, snum) {
         inputCheck(fnum, snum);
         var a = parseFloat(fnum);
         var b = parseFloat(snum);
         return a-b;
      }

function calcMultResult(fnum, snum) {
         inputCheck(fnum, snum);
         var a = parseFloat(fnum);
         var b = parseFloat(snum);
         return a*b;
      }

function calcDivResult(fnum, snum) {
         inputCheck(fnum, snum);
         var a = parseFloat(fnum);
         var b = parseFloat(snum);
         return a/b;
      }