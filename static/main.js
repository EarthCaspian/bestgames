$(document).ready(function() {
    updateGameCount();
    updateUserGameCount();
    console.log('update running');
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

function scrollToSearch(elementId) {
    const element = document.getElementById(elementId);
    window.scrollTo(0, element.offsetTop);
}

document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();
    scrollToSearch('results');
});