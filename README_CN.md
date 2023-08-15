## 中文版本:

### Telegram 频道媒体下载器

此Python脚本允许用户从指定的Telegram频道下载特定格式的媒体文件。

#### 使用前提:

1. 您的计算机上必须已安装**Python**。
2. **Telethon 库**:
    - 打开终端或命令提示符。
    - 运行命令：`pip install telethon`
3. **Telegram API 凭证**：请从 [Telegram官方的API开发工具](https://my.telegram.org/auth) 获取您的API ID和API Hash。

#### 使用方法:

1. **克隆或下载此仓库**:
    - 将此仓库克隆或下载到您的计算机。

2. **导航至脚本目录**:
    - 打开终端或命令提示符。
    - 使用`cd`命令导航至脚本所在的目录。

3. **运行脚本**:
    - 使用命令运行脚本：`python telegram_media_downloader.py`

4. **输入所需信息**:
    - 根据提示输入API ID、API Hash及电话号码。
    - 输入所需的Telegram频道链接。
    - 指定您想下载的媒体文件格式，用逗号分隔（例如：jpg, png, mp4）。输入“all”以下载所有格式的媒体文件。
    > **注意**: 如果直接按Enter键而不输入，将默认使用上一次的值。

5. **下载**:
    - 脚本将开始下载过程。下载完成后，媒体文件将存储在名为`telegram_downloads`的目录中。

---
