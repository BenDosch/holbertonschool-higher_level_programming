/* jQuery script that fetches and prints how to
say “Hello” depending on the language */
/* global $ */
$('document').ready(function () {
  $('INPUT#btn_translate').click(function () {
    $.get('https://fourtonfish.com/hellosalut/?lang=' +
    $('INPUT#language_code').val(),
    function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
