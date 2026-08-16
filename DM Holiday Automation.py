import asyncio
import os
import checker
from sinricpro import SinricPro, SinricProMotionSensor, SinricProConfig
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger(__name__)

# Device ID from SinricPro portal
DEVICE_ID = os.getenv("DMSWITCH_DEVICE_ID")  # Replace with your device ID

# Credentials from SinricPro portal
APP_KEY = os.getenv("SINRICPRO_APP_KEY")
APP_SECRET = os.getenv("SINRICPRO_APP_SECRET")

async def check_and_send(sensor: SinricProMotionSensor) -> None:
    """Check the Facebook page and send the corresponding motion event."""
    holiday_found = await checker.checker(logger)

    if holiday_found:
        logger.info("Holiday announcement detected.")
        lo = await sensor.send_motion_event(True)
        print(lo)
    else:
        logger.info("No holiday announcement detected.")
        await sensor.send_motion_event(False)


async def main() -> None:
    """Main function."""
    # Create SinricPro instance
    sinric_pro = SinricPro.get_instance()

    # Create motion sensor device
    motion_sensor = SinricProMotionSensor(DEVICE_ID)

    # Add device to SinricPro
    sinric_pro.add(motion_sensor)

    # Configure and connect
    config = SinricProConfig(app_key=APP_KEY, app_secret=APP_SECRET)

    try:
        await sinric_pro.begin(config)

        # Start motion simulation
        await check_and_send(motion_sensor)
        await asyncio.sleep(2)
    except KeyboardInterrupt:
        logger.info("Shutting down...")
    except Exception:
        logger.exception("Unhandled exception")
    finally:
        await sinric_pro.stop()


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
