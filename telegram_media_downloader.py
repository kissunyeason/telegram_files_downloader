from telethon import TelegramClient, utils
import os

FILENAME = 'last_input.txt'
download_folder = 'telegram_downloads'

def get_input_with_default(prompt, default=None):
    if default:
        user_input = input(f"{prompt} (默认：{default}): ")
    else:
        user_input = input(prompt + ": ")
    return user_input or default

# 尝试读取上次的输入值
try:
    with open(FILENAME, 'r') as f:
        last_api_id, last_api_hash, last_phone_number, last_channel_link, last_formats = f.read().splitlines()
except:
    last_api_id, last_api_hash, last_phone_number, last_channel_link, last_formats = (None, None, None, None, 'all')

api_id = get_input_with_default("请输入你的API ID", last_api_id)
api_hash = get_input_with_default("请输入你的API Hash", last_api_hash)
phone_number = get_input_with_default("请输入你的电话号码 (例如：'+1234567890')", last_phone_number)
channel_link = get_input_with_default("请输入Telegram频道链接", last_channel_link)
desired_formats_input = get_input_with_default("请输入你想下载的文件格式，用逗号隔开 (例如: jpg, png, mp4, 或 'all' 代表全部)", last_formats)

# 存储这次的输入值供下次使用
with open(FILENAME, 'w') as f:
    f.write(f"{api_id}\n{api_hash}\n{phone_number}\n{channel_link}\n{desired_formats_input}")

if desired_formats_input.lower() == "all":
    desired_formats = None
else:
    desired_formats = [fmt.strip().lower() for fmt in desired_formats_input.split(',')]

async def main():
    # 确保下载目录存在
    if not os.path.exists(download_folder):
        os.mkdir(download_folder)

    # 获取你要下载图片的频道
    channel = await client.get_entity(channel_link)
    
    if channel:
        print(f"Connected to channel: {channel.title}")
    else:
        print("Failed to connect to the channel.")
        return

    message_count = 0
    media_count = 0

    async for message in client.iter_messages(channel):
        if message.media:
            media_filename = utils.get_display_name(message.media)
            file_extension = os.path.splitext(media_filename)[1].strip('.').lower()

            # 如果desired_formats为None或文件扩展名在列表中，则下载文件
            if not desired_formats or file_extension in desired_formats:
                media_count += 1
                print(f"Found {file_extension} media in message {message_count}.")
                file_path = os.path.join(download_folder, media_filename)
                await client.download_media(message=message, file=file_path)

        message_count += 1

    print(f"Total messages processed: {message_count}")
    print(f"Total media files downloaded: {media_count}")

if __name__ == '__main__':
    with TelegramClient(phone_number, int(api_id), api_hash) as client:
        client.loop.run_until_complete(main())
