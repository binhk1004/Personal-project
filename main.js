$(document).ready(function() {
  $.ajax({
    type: "GET", //전송방식을 지정한다 (POST,GET)
    url: "file:///Users/binhk1004/Documents/GitHub/Personal-project/index.html", //호출 URL을 설정한다. GET방식일경우 뒤에 파라티터를 붙여서 사용해도된다.
    dataType: "text", //호출한 페이지의 형식이다. xml,json,html,text등의 여러 방식을 사용할 수 있다.
    success: function(Parse_data) {
      var a = $(".search").val(); //div에 받아온 값을 넣는다.
      $(".mid").append(a);
    }
  });
});
