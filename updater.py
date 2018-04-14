""" Copyright 2018 (c) Clarity
    This Source is covered by Apache 2.0 License.
    Please see LICENSE for details
"""
import six
import json
import aiohttp
import asyncio
import async_timeout

"""  Sends a request to remote API and returns a JSON response
     Intended for REST APIs for the moment. 
"""
 async def request(url: str, query: dict):
    async with async_timeout.timeout(20):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=query):
                return response.text()
 

    def main():
        # TODO: finish all query funcs and complete this.
        print('nya')
