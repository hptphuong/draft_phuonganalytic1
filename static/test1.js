(function() {
  var img = new Image,
      // url = encodeURIComponent(document.location.href),
      url = encodeURIComponent("https://phuonganalytic.herokuapp.com"),
      title = encodeURIComponent(document.title),
      ref = encodeURIComponent(document.referrer);
      img.src = 'phuonganalytic.herokuapp.com/a.gif?url=' + url + '&t=' + title + '&ref=' + ref;
})();