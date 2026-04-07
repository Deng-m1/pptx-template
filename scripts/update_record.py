#!/usr/bin/env python3
"""
update_record.py
更新 records/progress.csv 记录表中某一张幻灯片的处理结果。
用法: python3 update_record.py --slide 1 --html-status success --score 78.5 --grade "B（良好）" ...
"""

import csv
import argparse
import os
from datetime import datetime
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent
RECORD_FILE = PROJECT_DIR / "records" / "progress.csv"

FIELDS = [
    "slide_id", "image_file", "html_file", "screenshot_file",
    "ssim", "pixel_diff_rate", "similarity_score", "grade",
    "html_status", "screenshot_status", "compare_status",
    "error_notes", "processed_at",
]


def load_records(path: Path) -> dict:
    records = {}
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                records[row["slide_id"]] = row
    return records


def save_records(path: Path, records: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for key in sorted(records.keys(), key=lambda x: int(x)):
            writer.writerow(records[key])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--slide", required=True, help="幻灯片编号")
    parser.add_argument("--html-status", default="")
    parser.add_argument("--screenshot-status", default="")
    parser.add_argument("--compare-status", default="")
    parser.add_argument("--ssim", default="")
    parser.add_argument("--pixel-diff-rate", default="")
    parser.add_argument("--score", default="")
    parser.add_argument("--grade", default="")
    parser.add_argument("--error", default="")
    args = parser.parse_args()

    records = load_records(RECORD_FILE)
    sid = args.slide
    existing = records.get(sid, {f: "" for f in FIELDS})
    existing.update({
        "slide_id": sid,
        "image_file": f"slide_{sid}.png",
        "html_file": f"slide_{sid}.html",
        "screenshot_file": f"slide_{sid}.png",
        "html_status": args.html_status or existing.get("html_status", ""),
        "screenshot_status": args.screenshot_status or existing.get("screenshot_status", ""),
        "compare_status": args.compare_status or existing.get("compare_status", ""),
        "ssim": args.ssim or existing.get("ssim", ""),
        "pixel_diff_rate": args.pixel_diff_rate or existing.get("pixel_diff_rate", ""),
        "similarity_score": args.score or existing.get("similarity_score", ""),
        "grade": args.grade or existing.get("grade", ""),
        "error_notes": args.error or existing.get("error_notes", ""),
        "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    })
    records[sid] = existing
    save_records(RECORD_FILE, records)
    print(f"记录已更新: slide_{sid}")


if __name__ == "__main__":
    main()
