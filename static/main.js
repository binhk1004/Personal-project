$(document).ready(function () {
  let juso = getJuso();
  drawMap(juso);
  find_result(juso);
});

function getJuso() {
  let temp = location.href.split("?");
  let data = temp[1].split("=");
  let search_result = data[1];
  return decodeURIComponent(search_result).replace(/\+/g, " ");
}

function drawMap(juso) {
  let mapContainer = document.getElementById("map"), // 지도를 표시할 div
    mapOption = {
      center: new kakao.maps.LatLng(33.450701, 126.570667), // 지도의 중심좌표
      level: 4, // 지도의 확대 레벨
    };

  // 지도를 생성합니다
  let map = new kakao.maps.Map(mapContainer, mapOption);

  // 주소-좌표 변환 객체를 생성합니다
  let geocoder = new kakao.maps.services.Geocoder();

  // 주소로 좌표를 검색합니다
  geocoder.addressSearch(juso, function (result, status) {
    // 정상적으로 검색이 완료됐으면
    if (status === kakao.maps.services.Status.OK) {
      let coords = new kakao.maps.LatLng(result[0].y, result[0].x);

      // 결과값으로 받은 위치를 마커로 표시합니다
      let marker = new kakao.maps.Marker({
        map: map,
        position: coords,
      });

      // 인포윈도우로 장소에 대한 설명을 표시합니다
      let infowindow = new kakao.maps.InfoWindow({
        // content:
        //   '<div style="width:150px;text-align:center;padding:6px 0;">우리회사</div>',
      });
      infowindow.open(map);

      // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
      map.setCenter(coords);
    }
  });
}

function find_result(keyword) {
  $.ajax({
    type: "POST",
    url: "/main",
    data: { local_NB: keyword },
    success: function (response) {
      if (response["result"] == "success") {
        // alert(response["msg"]);
        // alert(response["data"]);
        // console.log(response["data"]);
        for_news = response["data"];

        for (let i = 0; i < for_news.length; i++) {
          href = for_news[i]["href"];
          title = for_news[i]["title"];
          image = for_news[i]["image"];
          show_news(title, href, image);
        }
        for_data = response["msg"];
        var ctx = document.getElementById("myChart");
        var myChart = new Chart(ctx, {
          type: "line",
          data: {
            labels: ["2015", "2016", "2017", "2018", "2019"],
            fill: false,
            datasets: [
              {
                label: "# of Votes",
                data: for_data,
                backgroundColor: [
                  "rgba(255, 99, 132, 0.2)",
                  "rgba(54, 162, 235, 0.2)",
                  "rgba(255, 206, 86, 0.2)",
                  "rgba(75, 192, 192, 0.2)",
                  "rgba(153, 102, 255, 0.2)",
                  "rgba(255, 159, 64, 0.2)",
                ],
                borderColor: [
                  "rgba(255,99,132,1)",
                  "rgba(54, 162, 235, 1)",
                  "rgba(255, 206, 86, 1)",
                  "rgba(75, 192, 192, 1)",
                  "rgba(153, 102, 255, 1)",
                  "rgba(255, 159, 64, 1)",
                ],
                borderWidth: 1,
              },
            ],
          },
          options: {
            maintainAspectRatio: true,
            fill: false,
            scales: {
              yAxes: [
                {
                  ticks: {
                    beginAtZero: false,
                  },
                },
              ],
            },
          },
        });
      }
    },
  });
}

function show_news(title, href, image) {
  $.ajax({
    type: "GET",
    url: "/main",
    data: { title, href, image },
    success: function (response) {
      if (response["result"] == "success") {
        // alert(response["msg"]);
        // alert(response["data"]);
        // console.log(response["data"]);
        for_news = response["data"];

        for (let i = 0; i < for_news.length; i++) {
          href = for_news[i]["href"];
          title = for_news[i]["title"];
          image = for_news[i]["image"];
          make_news(title, href, image);
        }
        function make_news(title, href, image) {
          card_deck =
            "<div class='card-deck'>" +
            "<div class='card'>" +
            "<img src=" +
            image +
            ">" +
            "<div class='card-body'>" +
            "<h5 class='card-title'>" +
            title +
            "</h5>" +
            "<p class='card-text'>" +
            "</p>" +
            "<p class=" +
            href +
            ">" +
            "<small class='text-muted'>" +
            "</small>" +
            "</p>" +
            "</div>" +
            "</div>" +
            "</div>";
          $(".bottom").append(card_deck);
        }
      }
    },
  });
}

// let card_deck = "";

// if (image == null) {
//   card_deck =
//     "<div class='card-deck'>" +
//     "<div class='card'>" +
//     "<img src=" +
//     "class='card-img-top' alt='...'>" +
//     "<div class='card-body'>" +
//     "<h5 class='card-title'>" +
//     title +
//     "</h5>" +
//     "<p class='card-text'>" +
//     "</p>";
//   "<p class=" +
//     href +
//     ">" +
//     "<small class='text-muted'>" +
//     "</small>" +
//     "</p>" +
//     "</div>";
// } else {
//   card_deck =
//     "<div class='card-deck'>" +
//     "<div class='card'>" +
//     "<img src=" +
//     image +
//     "class='card-img-top' alt='...'>" +
//     "<div class='card-body'>" +
//     "<h5 class='card-title'>" +
//     title +
//     "</h5>" +
//     "<p class='card-text'>" +
//     "</p>";
//   "<p class=" +
//     href +
//     ">" +
//     "<small class='text-muted'>" +
//     "</small>" +
//     "</p>" +
//     "</div>";
// }

// card_deck =
//   "<div class='card-deck'>" +
//   "<div class='card'>" +
//   "<img src=" +
//   image +
//   "class='card-img-top' alt='...'>" +
//   "<div class='card-body'>" +
//   "<h5 class='card-title'>" +
//   title +
//   "</h5>" +
//   "<p class='card-text'>" +
//   "</p>";
// "<p class=" +
//   href +
//   ">" +
//   "<small class='text-muted'>" +
//   "</small>" +
//   "</p>" +
//   "</div>";

// let temp_html = "";

// if (image == null) {
//   temp_html =
//     "<div class='news'> " +
//     "<a href='" +
//     href +
//     "' target='_blank' >" +
//     title +
//     "</a></div>";
// } else {
//   temp_html =
//     "<div class='news'> " +
//     "<img class ='image' src=" +
//     image +
//     " />" +
//     "<a class = 'link' href='" +
//     href +
//     "' target='_blank' >" +
//     title +
//     "</a></div>";
// }

// if (image == null) {
//   card_deck =
//     "<div class='card-deck'>" +
//     "<div class='card'>" +
//     "<img src=" +
//     "class='card-img-top' alt='...'>" +
//     "<div class='card-body'>" +
//     "<h5 class='card-title'>" +
//     title +
//     "</h5>" +
//     "<p class='card-text'>" +
//     "</p>";
//   "<p class=" +
//     href +
//     ">" +
//     "<small class='text-muted'>" +
//     "</small>" +
//     "</p>" +
//     "</div>";
// } else {
//   card_deck =
//     "<div class='card-deck'>" +
//     "<div class='card'>" +
//     "<img src=" +
//     image +
//     "class='card-img-top' alt='...'>" +
//     "<div class='card-body'>" +
//     "<h5 class='card-title'>" +
//     title +
//     "</h5>" +
//     "<p class='card-text'>" +
//     "</p>";
//   "<p class=" +
//     href +
//     ">" +
//     "<small class='text-muted'>" +
//     "</small>" +
//     "</p>" +
//     "</div>";
// }
