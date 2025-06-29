"""
Configuration settings for the Unity MCP Server.
This file contains all configurable parameters for the server.
"""

from dataclasses import dataclass
import os

@dataclass
class ServerConfig:
    """Main configuration class for the MCP server."""
    
    # Network settings
    unity_host: str = "localhost"
    unity_port: int = 6400
    mcp_port: int = 6500
    
    # HTTP SSE settings
    http_host: str = "0.0.0.0"  # Listen on all interfaces for remote access
    http_port: int = 6501
    
    # Transport settings
    transport: str = "stdio"  # "stdio" or "http"
    
    # Connection settings
    connection_timeout: float = 86400.0  # 24 hours timeout
    buffer_size: int = 16 * 1024 * 1024  # 16MB buffer
    
    # Logging settings
    log_level: str = "INFO"
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Server settings
    max_retries: int = 3
    retry_delay: float = 1.0
    
    def __post_init__(self):
        """Override settings from environment variables if present."""
        # Allow environment variables to override settings
        self.transport = os.getenv("UNITY_MCP_TRANSPORT", self.transport)
        self.http_host = os.getenv("UNITY_MCP_HTTP_HOST", self.http_host)
        self.http_port = int(os.getenv("UNITY_MCP_HTTP_PORT", str(self.http_port)))
        self.unity_host = os.getenv("UNITY_MCP_UNITY_HOST", self.unity_host)
        self.unity_port = int(os.getenv("UNITY_MCP_UNITY_PORT", str(self.unity_port)))

# Create a global config instance
config = ServerConfig() 