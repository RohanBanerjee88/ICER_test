// form.js - Update your jQuery code to a more testable structure

function handleClick() {
    $('#helloBtn').click(function() {
      $('#message').show();
      $(this).text('Clicked!');
    });
  }

// Assign the functions to variables for easier reference in tests
const handleClick = () => {
    $('#helloBtn').click(() => {
      $('#message').show();
      $('#helloBtn').text('Clicked!');
    });
  };
  
  module.exports = { handleClick };  