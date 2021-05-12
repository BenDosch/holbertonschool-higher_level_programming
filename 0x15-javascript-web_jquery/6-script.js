/* jQuery script to that updates the text of the <header> element
to New Header!!! when the user clicks on DIV#update_header */
/* global $ */
$('DIV#update_header').click(function () {
  $('header').text('New HEADER!!!');
});
