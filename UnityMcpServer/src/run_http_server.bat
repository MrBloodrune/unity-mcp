@echo off
REM HTTP Server runner for Unity MCP Server on Windows
REM This script runs the Unity MCP Server in HTTP/SSE mode for remote access

echo Starting Unity MCP Server in HTTP/SSE mode...
echo.
echo Server will listen on: http://0.0.0.0:6501
echo Unity connection: localhost:6400
echo.
echo Remote clients can connect to:
echo   http://^<your-windows-ip^>:6501/sse
echo.
echo Press Ctrl+C to stop the server
echo.

set UNITY_MCP_TRANSPORT=http
set UNITY_MCP_HTTP_HOST=0.0.0.0
set UNITY_MCP_HTTP_PORT=6501

python server.py %*