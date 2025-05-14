# Task 3

Some ASCII Pet companies are doing better than others so Mergers and Acquisitions are now taking place.

Pair your team with the team next to you.

Wishing to prove to your investors that the cost of the merger was worthwhile you need to add your new next feature.


When the pet reaches the right hand side of your screen,  it then needs to appear on the left hand side of the next screen in your group.


## Server

To help with this,  there is a public server available called https://app-pets.azurewebsites.net

This supports the following http requests:
 
PUT https://app-pets.azurewebsites.net/values/999  with a body of { "Value": "ABC" } will set the value of 999 on the server to be ABC

GET https://app-pets.azurewebsites.net/values/999 will return the value of 999 (ABC from the above example)


### Web Sockets (Advanced)

You can also be notified when these values change,  by connecting to a websocket on the server.

wss://app-pets.azurewebsites.net/ws/{yourId}

Where {yourId} is any string unique to yourself.  Please use the same value each time you run your program!

Whenever a value changes on the server,  it will be sent down your websocket as a json document containing two properties, key and value

In c# your code could look like this....

```csharp
var webSocket = new ClientWebSocket();
await webSocket.ConnectAsync(new Uri($"{SocketUrl}/ws/{ourId}"), CancellationToken.None);
var receiveBuffer = new byte[1024 * 4];
while (true)
{
    var receiveResult = await webSocket.ReceiveAsync(new ArraySegment<byte>(receiveBuffer), cancellationToken);
    var messageString = Encoding.UTF8.GetString(receiveBuffer, 0, receiveResult.Count);
    var message = JsonSerializer.Deserialize<SocketPayload>(messageString);
    ...
```

### SignalR (Very Advanced)

In addition to supporting websockets,  you can also be notified of changes via SignalR.

```csharp
var connection = new HubConnectionBuilder()
    .WithUrl("https://app-pets.azurewebsites.net/valueHub")
    .WithAutomaticReconnect()
    .Build();

await connection.StartAsync();
connection.On<int,string>("ValueUpdated", async (key, value) =>
{
     ...
```