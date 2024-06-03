<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
  $(document).ready(function() {
    // Add a click event listener to the DIV#add_item tag
    $("DIV#add_item").click(function() {
      // Create a new <li> element
      var newItem = $("<li>Item</li>");
      // Add the new <li> element to UL.my_list
      $("UL.my_list").append(newItem);
    });

    // Add a click event listener to the DIV#remove_item tag
    $("DIV#remove_item").click(function() {
      // Remove the last <li> element from UL.my_list
      $("UL.my_list li:last-child").remove();
    });

    // Add a click event listener to the DIV#clear_list tag
    $("DIV#clear_list").click(function() {
      // Remove all <li> elements from UL.my_list
      $("UL.my_list").empty();
    });
  });
</script>
