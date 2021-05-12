// jQuery script that updates the text color of the <header> element on clic
/* global $ */
$('DIV#red_header').click(function () {
  $('header').css({
    color: '#FF0000'
  });
});
