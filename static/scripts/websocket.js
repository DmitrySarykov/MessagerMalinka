const User = document.getElementById("current_user").innerText;
var ws;
// WebSocket
(function() {
  function init() {
    if (ws) {
      ws.onerror = ws.onopen = ws.onclose = null;
      ws.close();
    }
    const port = ':8080'
    var wsUri = (window.location.protocol=='https:'&&'wss://'||'ws://')+window.location.hostname+port;
    ws = new WebSocket(wsUri); //открываем соединение
    ws.onopen = function() {
      console.log('Соединен');
      viewMessages();
    };

    ws.onmessage = ({ data }) => {
      data = JSON.parse(data) // Преобразуем данные из Json
      console.log("Сообщение", data);
      viewMessages();
    }

    ws.onclose = function() {
      console.log('Разорвано');
      ws = null;
    };
  }
  init();
  // Поддержка постоянного соединения
  const interval = setInterval(function () {
    if (!ws) { init(); }
  }, 1000);  
})();


// Мария FJmBaJPDjq9XUq5
// Иван DAMJcuLEbQN5ddd
// Елена H7WiBHw9C2msucy