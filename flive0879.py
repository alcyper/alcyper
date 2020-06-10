"""Emoji

Available Commands:

.fleave"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 17)

    input_str = event.pattern_match.group(1)

    if input_str == "fleave":

        await event.edit(input_str)

        animation_chars = [
        
            "⬛⬛⬛\n⬛⬛⬛\n⬛⬛⬛",
            "⬛⬛⬛\n⬛🔄⬛\n⬛⬛⬛",
            "⬛⬆️⬛\n⬛🔄⬛\n⬛⬛⬛",
            "⬛⬆️↗️\n⬛🔄⬛\n⬛⬛⬛",
            "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛⬛",          
            "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛↘️",
            "⬛⬆️↗️\n⬛🔄➡️\n⬛⬇️↘️",
            "⬛⬆️↗️\n⬛🔄➡️\n↙️⬇️↘️",
            "⬛⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
            "↖️⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
            "**Chat Message Exported To** `./ঔৣ͡❂✦҈͜͡➳ৡৢ͜͡➛CypeRᴢ᭄͜͡࿐_ـࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧ✰ৡৢ͡/`",
            "**Chat Message Exported To** `./ঔৣ͡❂✦҈͜͡➳ৡৢ͜͡➛CypeRᴢ᭄͜͡࿐_ـࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧ✰ৡৢ͡/chatbackup/`",
            "**Chat Message Exported To** `./ঔৣ͡❂✦҈͜͡➳ৡৢ͜͡➛CypeRᴢ᭄͜͡࿐_ـࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧ✰ৡৢ͡/chatbackup/groupchat.txt`",
            "__Legend is leaving this chat.....! kuninjirunnoobu myrole..__",
            "__Legend is leaving this chat.....! kuninjirunnoobu myrole..__"

 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 17])
