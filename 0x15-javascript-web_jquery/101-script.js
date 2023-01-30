$(document).ready(() => {
  const mylist = $('UL.my_list');
  $('DIV#add_item').click(() => {
    mylist.append('<li>Item</li>');
  });

  $('DIV#remove_item').click(() => {
    const last = $('UL.my_list LI').last();
    last.remove();
  });

  $('DIV#clear_list').click(() => {
    mylist.empty();
  });
});
