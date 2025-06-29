#!/usr/bin/env python3
"""
Stdio Server runner for Unity MCP Server.
This script runs the Unity MCP Server in stdio mode for legacy compatibility.
"""

import os
import sys

def main():
    # Set environment variable for stdio transport
    os.environ['UNITY_MCP_TRANSPORT'] = 'stdio'
    
    print("Starting Unity MCP Server in stdio mode...")
    print("This mode is for direct client integration (MCP client launches the server)")
    print("\nPress Ctrl+C to stop the server")
    
    # Import and run the server
    from server import mcp
    mcp.run(transport='stdio')

if __name__ == '__main__':
    main()