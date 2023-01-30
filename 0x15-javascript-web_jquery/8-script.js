const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.ajax({
  type: 'GET',
  url: url,
  success: (movies) => {
    $.each(movies.results, (i, movie) => {
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    });
  }
});
