// jQuery script to add a <li> element when the user clicks on the tag DIV#add_item:
/* global $ */
$('DIV#add_item').click(function () {
  $('ul.my_list').append('<li>Item</li>');
});
