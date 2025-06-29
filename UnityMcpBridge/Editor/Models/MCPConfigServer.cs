using System;
using Newtonsoft.Json;

namespace UnityMcpBridge.Editor.Models
{
    [Serializable]
    public class McpConfigServer
    {
        [JsonProperty("command")]
        public string command;

        [JsonProperty("args")]
        public string[] args;
        
        [JsonProperty("url")]
        public string url;
        
        [JsonProperty("transport")]
        public string transport;
    }
}
