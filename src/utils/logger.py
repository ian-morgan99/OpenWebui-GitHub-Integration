"""Structured Logging Configuration"""
import logging
import sys
from typing import Any, Dict

import structlog


def sanitize_log_data(logger: Any, method_name: str, event_dict: Dict[str, Any]) -> Dict[str, Any]:
    """
    Sanitize sensitive data from logs.
    
    Args:
        logger: Logger instance
        method_name: Method name
        event_dict: Event dictionary
        
    Returns:
        Sanitized event dictionary
    """
    sensitive_keys = ['token', 'password', 'secret', 'api_key', 'authorization']
    
    for key in sensitive_keys:
        if key in event_dict:
            event_dict[key] = '***REDACTED***'
    
    return event_dict


def setup_logging(log_level: str = "INFO") -> None:
    """
    Setup structured logging with structlog.
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    # Configure structlog
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            sanitize_log_data,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.stdlib.BoundLogger,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )
    
    # Configure standard library logging
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, log_level.upper()),
    )


def get_logger(name: str) -> structlog.BoundLogger:
    """
    Get a structured logger instance.
    
    Args:
        name: Logger name (typically __name__)
        
    Returns:
        Structured logger instance
    """
    return structlog.get_logger(name)
