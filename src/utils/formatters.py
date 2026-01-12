"""Formatting Utilities"""
from datetime import datetime


def format_markdown(text: str) -> str:
    """
    Format text as GitHub-flavored Markdown.
    
    Args:
        text: Raw text to format
        
    Returns:
        Formatted markdown text
    """
    if not text:
        return ""
    
    # Basic markdown formatting
    # This is a simple implementation - extend as needed
    text = text.strip()
    return text


def format_timestamp(dt: datetime, format_type: str = "iso") -> str:
    """
    Format a datetime object to a string.
    
    Args:
        dt: Datetime object to format
        format_type: Format type - 'iso', 'human', 'github'
        
    Returns:
        Formatted timestamp string
    """
    if format_type == "iso":
        return dt.isoformat()
    elif format_type == "human":
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    elif format_type == "github":
        # GitHub API format
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    else:
        return dt.isoformat()


def format_file_size(bytes: int) -> str:
    """
    Format file size in bytes to human-readable format.
    
    Args:
        bytes: File size in bytes
        
    Returns:
        Human-readable file size (e.g., "1.5 MB")
    """
    if bytes < 1024:
        return f"{bytes} B"
    elif bytes < 1024 * 1024:
        return f"{bytes / 1024:.1f} KB"
    elif bytes < 1024 * 1024 * 1024:
        return f"{bytes / (1024 * 1024):.1f} MB"
    else:
        return f"{bytes / (1024 * 1024 * 1024):.2f} GB"


def format_duration(seconds: float) -> str:
    """
    Format duration in seconds to human-readable format.
    
    Args:
        seconds: Duration in seconds
        
    Returns:
        Human-readable duration (e.g., "2h 30m")
    """
    if seconds < 60:
        return f"{seconds:.0f}s"
    elif seconds < 3600:
        minutes = seconds / 60
        return f"{minutes:.0f}m"
    elif seconds < 86400:
        hours = seconds / 3600
        minutes = (seconds % 3600) / 60
        return f"{hours:.0f}h {minutes:.0f}m"
    else:
        days = seconds / 86400
        hours = (seconds % 86400) / 3600
        return f"{days:.0f}d {hours:.0f}h"


def format_number(number: int, compact: bool = False) -> str:
    """
    Format large numbers for display.
    
    Args:
        number: Number to format
        compact: Use compact format (e.g., 1.5K instead of 1,500)
        
    Returns:
        Formatted number string
    """
    if not compact:
        return f"{number:,}"
    
    if number < 1000:
        return str(number)
    elif number < 1_000_000:
        return f"{number / 1000:.1f}K"
    elif number < 1_000_000_000:
        return f"{number / 1_000_000:.1f}M"
    else:
        return f"{number / 1_000_000_000:.1f}B"


def format_percentage(value: float, total: float, decimal_places: int = 1) -> str:
    """
    Calculate and format percentage.
    
    Args:
        value: Numerator value
        total: Denominator value
        decimal_places: Number of decimal places
        
    Returns:
        Formatted percentage string (e.g., "85.5%")
    """
    if total == 0:
        return "0.0%"
    
    percentage = (value / total) * 100
    return f"{percentage:.{decimal_places}f}%"
