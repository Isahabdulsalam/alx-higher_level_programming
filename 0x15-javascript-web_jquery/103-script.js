<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
  // Wait for the document to be ready
  $(document).ready(function() {
    // Add a click event listener to the INPUT#btn_translate tag
    $("INPUT#btn_translate").click(fetchTranslation);

    // Add a keypress event listener to the INPUT#language_code tag
    $("INPUT#language_code").keypress(function(event) {
      if (event.which === 13) { // Check if the enter key is pressed
        fetchTranslation();
      }
    });

    // Function to fetch the translation of "Hello" based on the language code
    function fetchTranslation() {
      // Get the language code entered by the user
      var languageCode = $("INPUT#language_code").val();
      // Make an AJAX request to fetch the translation of "Hello" based on the language code
      $.ajax({
        url: 'https://www.fourtonfish.com/hellosalut/hello/',
        data: { lang: languageCode },
        method: 'GET',
        success: function(data) {
          // Display the translation in the HTML tag DIV#hello
          $("DIV#hello").text(data.hello);
        },
        error: function() {
          // Handle the error if the translation request fails
          $("DIV#hello").text("Translation not found");
        }
      });
    }
  });
</script>
