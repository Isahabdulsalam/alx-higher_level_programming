$(document).ready(function() {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function(data) {
      data.results.forEach(function(movie) {
        let listItem = $('<li>').text(movie.title);
        $("UL#list_movies").append(listItem);
      });
    },
    error: function() {
      $("UL#list_movies").append('<li>Error fetching movies</li>');
    }
  });
});
