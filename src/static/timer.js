const COUNTER_KEY = 'my-counter';

function countDown(i, callback) {
    //callback = callback || function(){};
    timer = setInterval(function() {
      seconds = parseInt(i % 16, 10); // here we give 16 as the parameter, so the timer will start from 15
      seconds = seconds < 10 ? "0" + seconds : seconds;

      document.getElementById("timer").innerHTML = "Time: " + seconds;

      if ((i--) > 0) {
        window.sessionStorage.setItem(COUNTER_KEY, i);
      } else {
        window.sessionStorage.removeItem(COUNTER_KEY);
        document.location.href = "/tr-timeout";
        clearInterval(timer);
        callback();
      }
    }, 1000);
}

window.onload = function() {
    var countDownTime = window.sessionStorage.getItem(COUNTER_KEY) || 15;
    countDown(countDownTime, function() {
      $('#myModal').modal('show');
    });
};
