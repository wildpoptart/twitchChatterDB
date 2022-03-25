// Create a new server on port 4000
var http = require('http');
var server = http.createServer(function (req, res) {
  res.end('Hello world!');
}).listen(4000);

// Maintain a hash of all connected sockets
var sockets = {}, nextSocketId = 0;
server.on('connection', function (socket) {
  // Add a newly connected socket
  var socketId = nextSocketId++;
  sockets[socketId] = socket;
  console.log('socket', socketId, 'opened');

  // Remove the socket when it closes
  socket.on('close', function () {
    console.log('socket', socketId, 'closed');
    delete sockets[socketId];
  });

  // Extend socket lifetime for demo purposes
  socket.setTimeout(4000);
});

// Count down from 10 seconds
(function countDown (counter) {
  console.log(counter);
  if (counter > 0)
    return setTimeout(countDown, 1000, counter - 1);

  // Close the server
  server.close(function () { console.log('Server closed!'); });
  // Destroy all open sockets
  for (var socketId in sockets) {
    console.log('socket', socketId, 'destroyed');
    sockets[socketId].destroy();
  }
})(10);