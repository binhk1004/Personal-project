$(document).ready(function () {
  find_result();
});

function find_result() {
  temp = location.href.split("?");
  data = temp[1].split("=");
  search_result = data[1];
  let number = decodeURIComponent(search_result);

  $.ajax({
    type: "POST",
    url: "/main.html",
    data: { local_NB: number },
    success: function (response) {
      if (response["result"] == "success") {
        alert("DB접속 성공");
      } else {
        alert(number);
      }
    },
  });
}

// $(document).ready(function () {
//   show_result();
// });

// function show_result(){
//   $.ajax({
//     type: "GET",
//     url: "/main.html",
//     data: {},
//     success: function (response) {
//       // 3. 서버가 돌려준 star_list를 star라는 변수에 저장합니다.
//       let DB = response["show_list"];
//       // 4. for 문을 활용하여 star 배열의 요소를 차례대로 조회합니다.
//       for (let i = 0; i < DB.length; i++) {
//         let data = DB[i];
//         // 5. star[i] 요소의 name, url, img_url, recent, like 키 값을 활용하여 값을 조회합니다.
//         make_list(
//           let localcode = data["법정동코드"],
//           let localname = data["법정동명"]
//         );
//       }
//     }
//   })
// }

//   function make_list(){
//     let temp_html =
//     "<tr>" +
//     "<th>" + localcode +
//     "</th>" +
//     "<th>" + localname +
//     "</th>" +
//     "</tr>" ;
//     $(".mid").append(temp_html);
//   }
