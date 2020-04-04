temp = location.href.split("?");
data = temp[1].split("=");
search_result = data[1];
console.log(search_result);
alert("받아오기 성공");

$("#test").text(search_result);

alert("입력 성공");
