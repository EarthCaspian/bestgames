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