/* jQuery script that adds, removes and clears LI elements
from a list when the user clicks */
/* global $ */
$('document').ready(function () {
  $('DIV#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    $('ul.my_list > li').first().remove();
  });
  $('DIV#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
