#!/usr/bin/env python3
"""
HTTP Server runner for Unity MCP Server.
This script runs the Unity MCP Server in HTTP/SSE mode for remote access.
"""

import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Run Unity MCP Server in HTTP/SSE mode')
    parser.add_argument('--host', default='0.0.0.0', help='HTTP server host (default: 0.0.0.0)')
    parser.add_argument('--port', type=int, default=6501, help='HTTP server port (default: 6501)')
    parser.add_argument('--unity-host', default='localhost', help='Unity host (default: localhost)')
    parser.add_argument('--unity-port', type=int, default=6400, help='Unity port (default: 6400)')
    
    args = parser.parse_args()
    
    # Set environment variables for configuration
    os.environ['UNITY_MCP_TRANSPORT'] = 'http'
    os.environ['UNITY_MCP_HTTP_HOST'] = args.host
    os.environ['UNITY_MCP_HTTP_PORT'] = str(args.port)
    os.environ['UNITY_MCP_UNITY_HOST'] = args.unity_host
    os.environ['UNITY_MCP_UNITY_PORT'] = str(args.unity_port)
    
    print(f"Starting Unity MCP Server in HTTP/SSE mode")
    print(f"HTTP Server: http://{args.host}:{args.port}")
    print(f"Unity Connection: {args.unity_host}:{args.unity_port}")
    print(f"\nTo connect from a remote client, use:")
    print(f"  HTTP endpoint: http://<server-ip>:{args.port}/sse")
    print(f"\nPress Ctrl+C to stop the server")
    
    # Import and run the server
    from server import mcp
    mcp.run(transport='sse', host=args.host, port=args.port)

if __name__ == '__main__':
    main()