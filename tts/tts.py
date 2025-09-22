import asyncio
import edge_tts
import sys

script = sys.argv[1]

with open(script, "r") as file:
    TEXT = file.read()


VOICE = "en-US-GuyNeural"
OUT = script[:-4] + ".mp3"

async def amain():
    communicate = edge_tts.Communicate(TEXT, VOICE, rate="+0%", pitch="+0Hz")
    await communicate.save(OUT)
    print(f"[OK] Saved -> {OUT}")

asyncio.run(amain())