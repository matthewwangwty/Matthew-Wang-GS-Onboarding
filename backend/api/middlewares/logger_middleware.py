from collections.abc import Callable
import datetime
import logging
from typing import Any
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware


class LoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Any]
    ) -> Response:
        """
        Logs all incoming and outgoing request, response pairs. This method logs the request params,
        datetime of request, duration of execution. Logs should be printed using the custom logging module provided.
        Logs should be printed so that they are easily readable and understandable.

        :param request: Request received to this middleware from client (it is supplied by FastAPI)
        :param call_next: Endpoint or next middleware to be called (if any, this is the next middleware in the chain of middlewares, it is supplied by FastAPI)
        :return: Response from endpoint
        """
        start_time = datetime.datetime.now()
        method = request.method
        url = str(request.url)

        logging.info(f"Incoming {method} request to {url}")
        logging.info(f"Request started at: {start_time}")

        response = await call_next(request)

        end_time = datetime.datetime.now()
        duration = (end_time - start_time).total_seconds()

        logging.info(f"Request completed with status {response.status_code}")
        logging.info(f"Request duration: {duration:.3f} seconds")

        return response
