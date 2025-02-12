import os
import asyncio

from core.clicker.blum import BlumClicker
from main.static import AUTOCLICKER_TEXT, DONATE_TEXT

#python -m main.main
async def main() -> None:
    os.system("cls")

    print(AUTOCLICKER_TEXT)
    print(DONATE_TEXT)

    clicker = BlumClicker()
    await clicker.run()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exiting due to keyboard interrupt.")
