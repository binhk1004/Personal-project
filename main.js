temp = location.href.split("?");
data = temp[1].split("=");
search_result = data[1];
let result = decodeURIComponent(search_result);
console.log(result);

$(document).ready(function () {
  $("#test").append(result);
});
