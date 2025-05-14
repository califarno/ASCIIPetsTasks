using System.Net.Http.Json;
using System.Net.WebSockets;
using System.Text;
using System.Text.Json;
using System.Text.Json.Serialization;
using Microsoft.AspNetCore.SignalR.Client;

namespace cat;

public static class Program
{
    private const string HttpUrl = "https://app-pets.azurewebsites.net";
    private const string SocketUrl = "wss://app-pets.azurewebsites.net";
    
    private const int SequenceKey = 0;
    
    public static async Task Main(string[] args)
    {
    }

    private static async Task TriggeredByHttpGet(string ourId, string nextId)
    {
        var client = new HttpClient();
        client.BaseAddress = new Uri(HttpUrl);

        while (true)
        {
            var response = await client.GetFromJsonAsync<string>($"/values/{SequenceKey}");
            await Task.Delay(100);  // Wait 1/10th of a second so that we don't flood server
        }
    }

    private static async Task TriggeredByWebSocket(string ourId, string nextId)
    {
        var cancellationToken = CancellationToken.None;
        ;
        var webSocket = new ClientWebSocket();
        await webSocket.ConnectAsync(new Uri($"{SocketUrl}/ws/{ourId}"), CancellationToken.None);
        
        var receiveBuffer = new byte[1024 * 4];
        while (true)
        {
            var receiveResult = await webSocket.ReceiveAsync(new ArraySegment<byte>(receiveBuffer), cancellationToken);
            var messageString = Encoding.UTF8.GetString(receiveBuffer, 0, receiveResult.Count);
            var message = JsonSerializer.Deserialize<SocketPayload>(messageString);
            if (message is not null)
            {
            }
        }
    }

    private record SocketPayload
    {
        [JsonPropertyName("key")]
        public required int Key { get; init; }
        
        [JsonPropertyName("value")]
        public required string Value { get; init; }
    }
    
    private static async Task TriggeredBySignalR(string ourId, string nextId)
    {
        var connection = new HubConnectionBuilder()
            .WithUrl($"{HttpUrl}/valueHub")
            .WithAutomaticReconnect()
            .Build();

        await connection.StartAsync();
        connection.On<int,string>("ValueUpdated", async (key, value) =>
        {
        });
    }

    private static async Task TriggerNextPet(string nextId)
    {
        var client = new HttpClient();
        client.BaseAddress = new Uri(HttpUrl);
        var response = await client.PutAsJsonAsync($"/values/{SequenceKey}", new ValueModel{ Value=nextId});
        response.EnsureSuccessStatusCode();
    }
    
    private record ValueModel
    {
        public string? Value { get; set; }
    }
    
    private static async Task DrawCat(string nextId)
    {
        Console.Clear();
        Console.WriteLine("meow");
    }


}