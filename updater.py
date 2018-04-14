# Copyright 2018 (c) Clarity
# This Source is covered by Apache 2.0 License.
# Please see LICENSE for details

import six
import json
import aiohttp
import asyncio
import async_timeout
        
async def request(url, json=query):
    async with async_timeout.timeout(20):
      async with aiohttp.ClientSession() as session:
         try:
          json.loads(query)
         except ValueError:
          print('query parameter not valid JSON')
         else:
          async with session.post(url, query)

def main():
    #TODO: finish all query funcs and complete this.
    print('nya')