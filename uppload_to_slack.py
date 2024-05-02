import os
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Slack APIトークンを環境変数から取得する
slack_token = os.environ.get("SLACK_TOKEN")
client = WebClient(token=slack_token)

# チャンネルID
channel_id = "C04ENEVP62V"

# PDFファイルをバイナリモードで読み込む
with open("issue.pdf", "rb") as file:
    pdf_data = file.read()

# ロガーの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    # ファイルをアップロード
    response = client.files_upload(
        channels=channel_id,
        file=pdf_data,
        filename="issue.pdf",
        title="Test upload",
        initial_comment="Here is the latest version of the file!",
    )
    logger.info(response)

except SlackApiError as e:
    logger.error(f"Error posting message: {e}")
