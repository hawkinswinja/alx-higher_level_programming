$(document).ready(() => {
  const lang = $('INPUT#language_code').val();
  $('INPUT#btn_translate').click(() => {
    $.ajax({
      type: 'POST',
      url: 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + lang,
      success: (results) => {
        $('DIV#hello').text(results.hello);
      }
    });
  });
});
