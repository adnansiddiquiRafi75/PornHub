"""Emoji

Available Commands:

.adnan"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 30)

    input_str = event.pattern_match.group(1)

    if input_str == "adnan":

        await event.edit(input_str)

        animation_chars = [

            "ÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN",
            
            "◼️ÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN",

            "◼️◼️ÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN",

            "◼️◼️◼️️ÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN",

            "◼️◼️◼️◼️ÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN",

            "‎◼️◼️◼️◼️◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN",

            "◼️◼️◼️◼️◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN",
            
            "◼️◼️◼️◼️◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN",
            
            "◼️◼️◼️◼️◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀNÀDNÀN",
   
            "◼️◼️◼️◼️◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️",

            "◼️◼️◼️◼️◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\nÀDNÀNÀDNÀNÀDNÀN◼️◼️",

            "◼️◼️◼️◼️◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\nÀDNÀNÀDNÀN◼️◼️◼️",

            "◼️◼️◼️◼️◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\nÀDNÀN◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\n◼️ÀDNÀNÀDNÀNÀDNÀN◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\nÀDNÀNÀDNÀNÀDNÀNÀDNÀN◼️\n◼️ÀDNÀNÀDNÀNÀDNÀN◼️\n◼️ÀDNÀNÀDNÀNÀDNÀN◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️ÀDNÀNÀDNÀNÀDNÀN◼️\n◼️ÀDNÀNÀDNÀNÀDNÀN◼️\n◼️ÀDNÀNÀDNÀNÀDNÀN◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️ÀDNÀNÀDNÀN◼️\n◼️ÀDNÀNÀDNÀNÀDNÀN◼️\n◼️ÀDNÀNÀDNÀNÀDNÀN◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️ÀDNÀN◼️\n◼️ÀDNÀNÀDNÀNÀDNÀN◼️\n◼️ÀDNÀNÀDNÀNÀDNÀN◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️ÀDNÀNÀDNÀNÀDNÀN◼️\n◼️ÀDNÀNÀDNÀNÀDNÀN◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️ÀDNÀNÀDNÀN◼️◼️\n◼️ÀDNÀNÀDNÀNÀDNÀN◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️ÀDNÀNÀDNÀN◼️◼️\n◼️ÀDNÀNÀDNÀN◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️ÀDNÀNÀDNÀN◼️◼️\n◼️ÀDNÀN◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️ÀDNÀNÀDNÀN◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️ÀDNÀN◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
          
            "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",
           
            "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",

            "◼️◼️\n◼️◼️",

            "◼️"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 30])
