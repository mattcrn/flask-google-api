$( document ).ready(function() {
  $('#js-handle-suggestion').on('click', function() {

    var artist = $('#artist').val()
    var song = $('#song').val()
    var msg = $('#js-ajax-msg')

    if(song == '' || artist == '') {
      msg.html('Bitte Interpret und Titel angeben!')
      return
    }

    var jqxhr = $.post( "http://flask-google.local/suggest-song", {'artist': artist, 'song': song}, function() {
    })
      .done(function() {
        msg.html(artist + ' - ' + song + 'erfolgreich zur Liste hinzugefügt!')
      })
      .fail(function(e) {
        msg.html('Oje, da ist wohl etwas schief gegangen :( Bitte versuche es später erneut.')
      })
  });
});