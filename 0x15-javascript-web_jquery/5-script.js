$(document).ready(function() {
  $("DIV#add_item").click(function() {
    let newItem = $("<li>Item</li>");
    $("UL.my_list").append(newItem);
  });
});
