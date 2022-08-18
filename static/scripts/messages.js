const messages_list = document.getElementById("messages_list");
const empty_message = document.getElementById("message_empty");
async function viewMessages(){
    messages_list.innerHTML = "";
    await fetch("/messages/").then(response => response.json()).then(data => {
        data.forEach(element => {
            // Создание сообщения
            let time = getTime(element.date);
            let user = element.username;
            let text = element.text;
            var message = empty_message.cloneNode(true);
            message.id = `message-${element.id}`;
            message.removeAttribute('style');
            if (User == element.user){
                message.classList.add("current");
            }
            $(message).find("h5").html(user);
            $(message).find("p").html(text);
            $(message).find(".time").html(time);
            messages_list.appendChild(message);
        });
    });
    $(".messages-wrap").animate({
        scrollTop: messages_list.scrollHeight
    }, 0);
}

// Функция установления времени
function getTime(value){
    const date = new Date(value);
    var hour = date.getHours();
    var minute = date.getMinutes();   
    // Добавление 0 если число не двузначное
    if (hour < 10){hour = '0' + hour;}
    if (minute < 10){minute = '0' + minute;}
    return `${hour}:${minute}`
}