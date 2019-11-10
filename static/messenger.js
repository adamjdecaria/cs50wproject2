/* Messenger.js - use websockets to broadcast messages across channels */

document.addEventListener('DOMContentLoaded', () => {
    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    socket.on('connect', () => {
        // when connected, configure sendMessage button
        document.querySelectorAll('button').forEach(button => {
            button.onclick = () => {
                const message = document.getElementById("chatMessage").value;
                socket.emit('new message', { 'message': message });
            };
        });
    });

    socket.on('announce message', message => {
        console.log(message);
        const li = document.createElement('li');
        li.innerHTML = `${message.message}`;
        document.querySelector("#messageList").append(li);
    });
});