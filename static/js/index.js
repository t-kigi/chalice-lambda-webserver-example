var f = function() {
  var count = 0;
  var btn = document.getElementById('button');
  btn.addEventListener('click', function() {
    count += 1;
    document.getElementById('counter').innerHTML = count;
  }, false);
};

f();

