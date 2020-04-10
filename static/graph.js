temp = location.href.split("?");
data = temp[1].split("=");
search_result = data[1];
let juso = decodeURIComponent(search_result);
console.log(juso);

$(document).ready(function () {
  $("#test").append(juso);
});

$(document).ready(function () {
  show_result();
});

let numbers = response["local_number"];

function show_result() {
  $.ajax({
    type: "GET",
    url: "/main.html",
    data: {},
    success: function (response) {
//      let numbers = response["local_number"];
      for (let i = 0; i < numbers.length; i++) {
        let number = numbers[i];
        let name = number["법정동명"];
        let id = number["법정동코드"];
        let temp_html =
          "<tr>" + "<th>" + name + "</th>" + "<th>" + id + "</th>" + "</tr>";
        $(".mid").append(temp_html);

      }
    },
  });
}
