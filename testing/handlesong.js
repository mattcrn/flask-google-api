$( document ).ready(function() {
  $('#js-handle-suggestion').on('click', function() {

    var artist = $('#artist').val()
    var song = $('#song').val()
    console.log(artist + ' - ' + song)
    var jqxhr = $.post( "http://flask-google.local/suggest-song", {'artist': artist, 'song': song}, function() {
    })
      .done(function() {
        console.log('succ')
      })
      .fail(function(e) {
        console.log(e)
      })
  });
});