#!/usr/bin/env python3
"""
screenshot_html.py
使用 Playwright 对 HTML 文件进行截图，固定视口 1280×720。
用法: python3 screenshot_html.py <html_path> <output_png>
"""

import os
import sys
import json
import argparse


def screenshot_html(html_path: str, output_path: str, viewport_width: int = 1280, viewport_height: int = 720) -> dict:
    result = {
        "html": os.path.basename(html_path),
        "output": output_path,
        "status": "pending",
        "error": None,
    }
    try:
        from playwright.sync_api import sync_playwright
        html_abs = os.path.abspath(html_path)
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": viewport_width, "height": viewport_height})
            page.goto(f"file://{html_abs}", wait_until="networkidle", timeout=30000)
            page.wait_for_timeout(500)
            page.screenshot(path=output_path, full_page=False)
            browser.close()
        result["status"] = "success"
    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)
    return result


def main():
    parser = argparse.ArgumentParser(description="Playwright 截图工具")
    parser.add_argument("html_path", help="HTML 文件路径")
    parser.add_argument("output_path", help="输出 PNG 路径")
    parser.add_argument("--width", type=int, default=1280)
    parser.add_argument("--height", type=int, default=720)
    args = parser.parse_args()
    result = screenshot_html(args.html_path, args.output_path, args.width, args.height)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result["status"] == "success" else 1)


if __name__ == "__main__":
    main()
