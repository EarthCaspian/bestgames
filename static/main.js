$(document).ready(function() {
    updateGameCount();
    updateUserGameCount();
    console.log('update running');

    // slick init
    $('.your-class').slick({
        dots: true,
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 3,
              infinite: true,
              dots: true
            }
          },
          {
            breakpoint: 600,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 2
            }
          },
          {
            breakpoint: 480,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
          // You can unslick at a given breakpoint now by adding:
          // settings: "unslick"
          // instead of a settings object
        ]
      }
    );
});

var url = "game/count";
var url2 = "game/count/user"

function updateGameCount() {
    $.ajax({
        url: url,
        method: 'GET',
        dataType: "json",
        success: function(response) {
            $('#count-placeholder').text(response.count);
        },
        error: function(xhr, status, error) {
            console.error('Error fetching game count:', error);
        }
    });
}

function updateUserGameCount() {
    $.ajax({
        url: url2,
        method: 'GET',
        dataType: "json",
        success: function(response) {
            $('#user-count-placeholder').text(response.count);
        },
        error: function(xhr, status, error) {
            console.error('Error fetching user game count:', error);
        }
    });
}

//* Scrolling to search area function

document.querySelector('form').addEventListener('submit', function(event) {
  event.preventDefault();
  const form = event.target;
  const formData = new FormData(form);
  const url = form.getAttribute('action');
  const method = form.getAttribute('method');
  
  // Serialize the form data into a URL-encoded string
  const encodedFormData = new URLSearchParams(formData).toString();
  
  // Append the serialized form data as a query parameter to the current URL
  const updatedURL = window.location.pathname + '?' + encodedFormData;

  // Redirect to the updated URL with the fragment identifier to scroll to the results
  window.location.href = updatedURL + '#search-results';
});


//* Upvote function

document.addEventListener('DOMContentLoaded', () => {
  const upvoteButtons = document.querySelectorAll('.upvote-button');

  upvoteButtons.forEach(button => {
    button.addEventListener('click', () => {
      const gameId = button.dataset.gameId;
      console.log("upvote button works");
      // Send AJAX request to upvote view
      fetch(`/upvote/${gameId}/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken'),
        },
      })
      .then(response => response.json())
      .then(data => {
        // Update total upvote count on the page
        const upvoteCountElement = document.querySelector(`#upvote-count-${gameId}`);
        upvoteCountElement.textContent = `Total Upvotes: ${data.total_upvotes}`;
      });
    });
  });
});
