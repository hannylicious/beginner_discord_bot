import asyncdispatch, os, strutils, times, discordnim

let bot = newShard("Bot " & $getEnv("DISCORD_BOT_TOKEN")) # Create 1 Discord bot

proc on_message(bot: Shard, mesage: MessageCreate) =
  if mesage.author.id != bot.cache.me.id: # Bot wont reply itself (infinite loop)
    case mesage.content.strip()           # case switch on message content
    of "!help":                           # message content is "!help"
      asyncCheck bot.channelMessageSend(mesage.channel_id, "Help: Some help.")
    of "!ping":                           # message content is "!ping"
      asyncCheck bot.channelMessageSend(mesage.channel_id, "pong")
    of "!time":                           # message content is "!time"
      asyncCheck bot.channelMessageSend(mesage.channel_id, $now())
    else:
      echo mesage.content                 # message content is something else

discard bot.addHandler(EventType.message_create, on_message) # Add on_message handler


if isMainModule:
  try:
    waitFor bot.startSession()            # Bot starts the session
  finally:
    waitFor bot.disconnect()              # Bot disconnects the session
