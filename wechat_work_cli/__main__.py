import argparse
from typing import List
from wechat_work import WechatWork


def send_message(
    w: WechatWork, message_type: str, users: List[str], content_path: str
) -> None:
    if message_type == "text":
        w.send_text(content_path, users)
    elif message_type == "markdown":
        with open(content_path, "r", encoding="utf-8") as file:
            markdown_content = file.read()
        w.send_markdown(markdown_content, users)
    elif message_type == "image":
        w.send_image(content_path, users)
    elif message_type == "file":
        w.send_file(content_path, users)
    else:
        print("Invalid message type")


def main() -> None:
    parser = argparse.ArgumentParser(description="Send messages to WeChat Work users.")
    parser.add_argument("--corpid", required=True, help="企业 ID")
    parser.add_argument("--appid", required=True, help="企业应用 ID")
    parser.add_argument("--corpsecret", required=True, help="企业应用 Secret")
    parser.add_argument(
        "--users", nargs="+", required=True, help="企业微信的用户账号列表"
    )
    parser.add_argument(
        "--type",
        choices=["text", "markdown", "image", "file"],
        required=True,
        help="消息类型",
    )
    parser.add_argument("--content", required=True, help="消息内容或文件路径")
    args = parser.parse_args()

    w = WechatWork(corpid=args.corpid, appid=args.appid, corpsecret=args.corpsecret)
    send_message(w, args.type, args.users, args.content)


if __name__ == "__main__":
    main()
