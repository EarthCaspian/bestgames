$(document).ready(function() {
    updateGameCount();
    console.log('update running');
});

var url = "game/count";

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