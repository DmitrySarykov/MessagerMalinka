$('#send').click(createMessage);
  
$('#text').keyup(function(e) {
    if (e.keyCode === 13) {
      $('#send').click();
      return false;
    }
});
  
async function createMessage(e){
    e.preventDefault();
    var text = $('#text').val();
    const options = {
      method: 'POST',
      body: JSON.stringify({
        user: User,
        text: text,
      }),
      headers: {
          "X-CSRFToken": getCookie('csrftoken'),
          "Content-type": "application/json; charset=UTF-8"
      }
    }
    await fetch("/message/add",options).then(response => response.json()).then(data => {
      ws.send(JSON.stringify(data)); // Посылаем данные получателю
      viewMessages();
    }).catch(error => console.log(error));
    $('#text').val('').focus();
}


function getCookie(name) {
    var matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}