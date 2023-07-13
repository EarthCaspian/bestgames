$(document).ready(function() {
    updateGameCount();
    console.log('update running');
});

function updateGameCount() {
    $.ajax({
        url: '/game/count/',
        method: 'GET',
        success: function(response) {
            $('#count-placeholder').text(response.count);
        },
        error: function(xhr, status, error) {
            console.error('Error fetching game count:', error);
        }
    });
}