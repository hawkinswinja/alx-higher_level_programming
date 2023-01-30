$.ajax({
  type: 'POST',
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  success: (result) => {
    $('DIV#hello').text(result.hello);
  },
  error: () => {
    console.log('error loading data');
  }
});
