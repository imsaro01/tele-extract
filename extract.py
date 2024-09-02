import os
import logging
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError, FloodWaitError
import asyncio
import configparser
from collections import defaultdict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

api_id = config['Telegram']['API_ID']
api_hash = config['Telegram']['API_HASH']
phone_number = config['Telegram']['PHONE_NUMBER']
channel_username = config['Telegram']['CHANNEL_USERNAME']
session_name = 'session_name'

# Initialize the Telegram client
client = TelegramClient(session_name, api_id, api_hash)

# Define allowed file extensions
allowed_extensions = {'.zip', '.7z', '.txt', '.rar'}

# Rate limiting parameters
MAX_REQUESTS_PER_SECOND = 20
semaphore = asyncio.Semaphore(MAX_REQUESTS_PER_SECOND)

# Initialize counters for file types
file_counters = defaultdict(int)

async def download_file(message):
    async with semaphore:
        file_name = message.file.name or 'file'
        file_extension = os.path.splitext(file_name)[1].lower()

        if file_extension in allowed_extensions:
            file_path = os.path.join('downloads', file_name)
            
            try:
                # Download the file
                logger.info(f"Downloading file: {file_name}")
                await message.download_media(file=file_path)
                file_counters[file_extension] += 1
                logger.info(f"Successfully downloaded: {file_path}")
            except FloodWaitError as e:
                # Handle rate limiting by Telegram
                logger.warning(f"Rate limit hit. Sleeping for {e.seconds} seconds.")
                await asyncio.sleep(e.seconds)
            except Exception as e:
                logger.error(f"Failed to download file {file_name}: {e}")
        else:
            logger.info(f"Skipped file with extension: {file_extension}")

async def download_files():
    await client.start(phone_number)
    
    # Ensure the channel entity
    try:
        channel = await client.get_entity(channel_username)
    except Exception as e:
        logger.error(f"Failed to get channel entity: {e}")
        return

    # Create a directory to store downloaded files
    os.makedirs('downloads', exist_ok=True)
    
    async for message in client.iter_messages(channel):
        if message.file:
            # Download files with rate limiting
            await download_file(message)

async def main():
    try:
        await download_files()
    except SessionPasswordNeededError:
        # Handle 2FA
        logger.error("Two-factor authentication is required. Please provide the code.")
        code = input("Enter the 2FA code: ")
        await client.start(phone_number, code)
        await download_files()
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
    finally:
        await client.disconnect()
        # Log the file counts by type
        logger.info("Download summary:")
        for ext, count in file_counters.items():
            logger.info(f"Type {ext}: {count} files")

# Run the script
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
