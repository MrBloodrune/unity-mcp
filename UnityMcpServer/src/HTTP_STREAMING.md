# Unity MCP HTTP Streaming Setup

This guide explains how to use the HTTP/SSE transport mode to connect to Unity MCP Server from remote clients.

## Overview

The Unity MCP Server uses HTTP Server-Sent Events (SSE) transport by default, allowing both local and remote MCP clients to connect to the server over HTTP. This makes it possible to run Unity and the MCP Server on a Windows PC while connecting from any MCP client, whether local or remote. The server also supports stdio transport for legacy compatibility.

## Configuration

### Environment Variables

You can configure the HTTP server using environment variables:

- `UNITY_MCP_TRANSPORT`: Set to `"stdio"` for legacy stdio mode (default: `"http"`)
- `UNITY_MCP_HTTP_HOST`: HTTP server host (default: `"0.0.0.0"`)
- `UNITY_MCP_HTTP_PORT`: HTTP server port (default: `6501`)
- `UNITY_MCP_UNITY_HOST`: Unity Editor host (default: `"localhost"`)
- `UNITY_MCP_UNITY_PORT`: Unity Editor port (default: `6400`)

### Running in HTTP Mode

#### Option 1: Using the Helper Script

```bash
cd UnityMcpServer/src
python run_http_server.py
```

Optional arguments:
```bash
python run_http_server.py --host 0.0.0.0 --port 6501 --unity-host localhost --unity-port 6400
```

#### Option 2: Using Environment Variables

```bash
export UNITY_MCP_TRANSPORT=http
export UNITY_MCP_HTTP_HOST=0.0.0.0
export UNITY_MCP_HTTP_PORT=6501
python server.py
```

#### Option 3: Using uv with Environment Variables

```bash
UNITY_MCP_TRANSPORT=http UNITY_MCP_HTTP_HOST=0.0.0.0 uv run server.py
```

## Remote Connection Setup

### Server Side (Windows with Unity)

1. Ensure Unity Editor is running with the Unity MCP Bridge
2. Ensure Windows firewall allows incoming connections on port 6501
3. Run the Unity MCP Server in HTTP mode:
   ```bash
   cd UnityMcpServer\src
   python run_http_server.py --host 0.0.0.0
   ```
   
   Or using PowerShell:
   ```powershell
   $env:UNITY_MCP_TRANSPORT="http"
   $env:UNITY_MCP_HTTP_HOST="0.0.0.0"
   python server.py
   ```

### Client Side (Remote MCP Client)

1. Configure your MCP client to connect to the HTTP endpoint:
   ```
   http://<windows-pc-ip>:6501/sse
   ```

2. Example configuration for remote MCP client:
   ```json
   {
     "mcpServers": {
       "UnityMCP": {
         "url": "http://192.168.1.100:6501/sse",
         "transport": "sse"
       }
     }
   }
   ```

## Security Considerations

- The HTTP server listens on all interfaces (0.0.0.0) by default for remote access
- Consider using a firewall to restrict access to trusted IP addresses
- For production use, consider adding authentication or running behind a reverse proxy with HTTPS

## Troubleshooting

1. **Connection refused**: Check firewall settings and ensure the server is running
2. **Unity not responding**: Verify Unity Editor is running with the MCP Bridge on the same machine as the HTTP server
3. **Port already in use**: Change the port using `--port` argument or environment variable

## Switching to stdio Mode

If you prefer the legacy stdio transport (where the MCP client launches the server):

1. Set the environment variable:
   ```bash
   set UNITY_MCP_TRANSPORT=stdio
   ```

2. Update your MCP client configuration to use command/args instead of URL:
   ```json
   {
     "mcpServers": {
       "unityMCP": {
         "command": "uv",
         "args": ["--directory", "C:\\path\\to\\UnityMcpServer\\src", "run", "server.py"]
       }
     }
   }
   ```

## Architecture

```
[Windows PC]
  Unity Editor <-- TCP (6400) --> Unity MCP Bridge
       |
  Unity MCP Server
       |
  HTTP/SSE endpoint (0.0.0.0:6501)
       |
       v
[Remote Linux/Mac/Windows]
  MCP Client (Claude, Cursor, etc.)
```

The Unity MCP Server runs on the same Windows machine as Unity and exposes an HTTP endpoint for remote MCP clients to connect.