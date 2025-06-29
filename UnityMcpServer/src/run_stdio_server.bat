@echo off
REM Stdio Server runner for Unity MCP Server on Windows
REM This script runs the Unity MCP Server in stdio mode for legacy compatibility

echo Starting Unity MCP Server in stdio mode...
echo This mode is for direct client integration (MCP client launches the server)
echo.
echo Press Ctrl+C to stop the server
echo.

set UNITY_MCP_TRANSPORT=stdio

python server.py %*