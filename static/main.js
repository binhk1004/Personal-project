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
      level: 7, // 지도의 확대 레벨
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
        alert(response["msg"]);
        for_data = response["msg"];
        graph_data = [];
        max_value = Math.max.apply(null, for_data);
        for (let i = 0; i < for_data.length; i++) {
          graph_data.push(((for_data[i] / max_value) * 100).toString());
        }
        d3.select(".mid")
          .selectAll()
          .data(graph_data)
          .enter()
          .append("div")
          .attr("class", "chart")
          .style("height", function (d) {
            return d + "px";
          });
      } else {
        alert(keyword);
      }
    },
  });
}
