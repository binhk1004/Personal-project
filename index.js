function mainpage() {
  if (event.keyCode == 13) {
    location.href = "main.html";
    var a = $(".search").val();
  }
  console.log(a);
}
