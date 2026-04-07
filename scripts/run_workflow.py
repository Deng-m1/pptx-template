#!/usr/bin/env python3
"""
run_workflow.py
主工作流脚本：批量处理幻灯片图片 → 生成 HTML → Playwright 截图 → 相似度对比 → 更新记录表
"""

import os
import sys
import json
import csv
import argparse
import time
from pathlib import Path
from datetime import datetime

# 脚本目录
SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent

# 默认路径配置
DEFAULT_TEMPLATE = "01高级商务蓝配色"
DEFAULT_SLIDES_DIR = PROJECT_DIR / DEFAULT_TEMPLATE
DEFAULT_HTML_DIR = PROJECT_DIR / DEFAULT_TEMPLATE / "html"
DEFAULT_SCREENSHOTS_DIR = PROJECT_DIR / DEFAULT_TEMPLATE / "screenshots"
DEFAULT_RECORDS_DIR = PROJECT_DIR / "records"
DEFAULT_RECORD_FILE = DEFAULT_RECORDS_DIR / "progress.csv"
DEFAULT_ISSUES_FILE = DEFAULT_RECORDS_DIR / "issues.md"

# CSV 记录表字段
CSV_FIELDS = [
    "slide_id",
    "image_file",
    "html_file",
    "screenshot_file",
    "ssim",
    "pixel_diff_rate",
    "similarity_score",
    "grade",
    "html_status",
    "screenshot_status",
    "compare_status",
    "error_notes",
    "processed_at",
]


def load_existing_records(record_file: Path) -> dict:
    """加载已有记录，返回以 slide_id 为键的字典"""
    records = {}
    if record_file.exists():
        with open(record_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                records[row["slide_id"]] = row
    return records


def save_records(record_file: Path, records: dict):
    """保存记录到 CSV 文件"""
    record_file.parent.mkdir(parents=True, exist_ok=True)
    with open(record_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        # 按 slide_id 数字排序
        sorted_keys = sorted(records.keys(), key=lambda x: int(x))
        for key in sorted_keys:
            writer.writerow(records[key])


def get_slide_files(slides_dir: Path) -> list:
    """获取所有幻灯片图片，按编号排序"""
    files = sorted(
        slides_dir.glob("slide_*.png"),
        key=lambda p: int(p.stem.split("_")[1])
    )
    return files


def process_slide(
    slide_file: Path,
    html_dir: Path,
    screenshots_dir: Path,
    model: str = "gpt-4.1-mini",
    force: bool = False,
) -> dict:
    """处理单张幻灯片的完整流程"""
    from generate_html import generate_html_for_slide
    from screenshot_html import screenshot_html
    from compare_images import compare_images

    slide_id = slide_file.stem.split("_")[1]
    html_file = html_dir / f"slide_{slide_id}.html"
    screenshot_file = screenshots_dir / f"slide_{slide_id}.png"

    record = {
        "slide_id": slide_id,
        "image_file": slide_file.name,
        "html_file": html_file.name,
        "screenshot_file": screenshot_file.name,
        "ssim": "",
        "pixel_diff_rate": "",
        "similarity_score": "",
        "grade": "",
        "html_status": "pending",
        "screenshot_status": "pending",
        "compare_status": "pending",
        "error_notes": "",
        "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    errors = []

    # Step 1: 生成 HTML
    if force or not html_file.exists():
        print(f"  [1/3] 生成 HTML: slide_{slide_id}...")
        html_result = generate_html_for_slide(str(slide_file), str(html_file), model)
        record["html_status"] = html_result["status"]
        if html_result["status"] != "success":
            errors.append(f"HTML生成失败: {html_result.get('error', '')}")
    else:
        print(f"  [1/3] HTML 已存在，跳过: slide_{slide_id}")
        record["html_status"] = "skipped"

    # Step 2: Playwright 截图
    if record["html_status"] in ("success", "skipped") and html_file.exists():
        if force or not screenshot_file.exists():
            print(f"  [2/3] Playwright 截图: slide_{slide_id}...")
            shot_result = screenshot_html(str(html_file), str(screenshot_file))
            record["screenshot_status"] = shot_result["status"]
            if shot_result["status"] != "success":
                errors.append(f"截图失败: {shot_result.get('error', '')}")
        else:
            print(f"  [2/3] 截图已存在，跳过: slide_{slide_id}")
            record["screenshot_status"] = "skipped"
    else:
        record["screenshot_status"] = "skipped_no_html"

    # Step 3: 相似度对比
    if screenshot_file.exists():
        print(f"  [3/3] 相似度对比: slide_{slide_id}...")
        cmp_result = compare_images(str(slide_file), str(screenshot_file))
        record["compare_status"] = cmp_result["status"]
        if cmp_result["status"] == "success":
            record["ssim"] = cmp_result["ssim"]
            record["pixel_diff_rate"] = cmp_result["pixel_diff_rate"]
            record["similarity_score"] = cmp_result["similarity_score"]
            record["grade"] = cmp_result["grade"]
        else:
            errors.append(f"对比失败: {cmp_result.get('error', '')}")
    else:
        record["compare_status"] = "skipped_no_screenshot"

    record["error_notes"] = " | ".join(errors)
    record["processed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return record


def main():
    parser = argparse.ArgumentParser(description="幻灯片 HTML 还原主工作流")
    parser.add_argument("--template", default=DEFAULT_TEMPLATE, help="模板目录名称")
    parser.add_argument("--slides", type=int, nargs="+", help="指定处理哪些幻灯片编号（默认全部）")
    parser.add_argument("--limit", type=int, help="限制处理数量（用于测试）")
    parser.add_argument("--model", default="gpt-4.1-mini", help="LLM 模型")
    parser.add_argument("--force", action="store_true", help="强制重新生成（忽略已有文件）")
    parser.add_argument("--record-file", default=str(DEFAULT_RECORD_FILE), help="记录文件路径")
    args = parser.parse_args()

    # 路径配置
    slides_dir = PROJECT_DIR / args.template
    html_dir = slides_dir / "html"
    screenshots_dir = slides_dir / "screenshots"
    record_file = Path(args.record_file)

    html_dir.mkdir(parents=True, exist_ok=True)
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    # 将脚本目录加入 Python 路径
    sys.path.insert(0, str(SCRIPT_DIR))

    # 获取幻灯片文件列表
    all_slides = get_slide_files(slides_dir)
    if args.slides:
        all_slides = [f for f in all_slides if int(f.stem.split("_")[1]) in args.slides]
    if args.limit:
        all_slides = all_slides[:args.limit]

    print(f"共 {len(all_slides)} 张幻灯片待处理")
    print(f"模型: {args.model}")
    print(f"记录文件: {record_file}")
    print("=" * 60)

    # 加载已有记录
    records = load_existing_records(record_file)

    # 逐张处理
    for i, slide_file in enumerate(all_slides, 1):
        slide_id = slide_file.stem.split("_")[1]
        print(f"\n[{i}/{len(all_slides)}] 处理 slide_{slide_id}.png")

        try:
            record = process_slide(
                slide_file, html_dir, screenshots_dir,
                model=args.model, force=args.force
            )
            records[slide_id] = record
            score = record.get("similarity_score", "N/A")
            grade = record.get("grade", "N/A")
            print(f"  完成 → 相似度: {score} ({grade})")
        except Exception as e:
            print(f"  错误: {e}")
            records[slide_id] = {
                "slide_id": slide_id,
                "image_file": slide_file.name,
                "html_file": f"slide_{slide_id}.html",
                "screenshot_file": f"slide_{slide_id}.png",
                "ssim": "", "pixel_diff_rate": "", "similarity_score": "", "grade": "",
                "html_status": "error", "screenshot_status": "error", "compare_status": "error",
                "error_notes": str(e),
                "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }

        # 每处理完一张就保存记录（防止中途中断丢失数据）
        save_records(record_file, records)

        # 避免 API 限速
        if i < len(all_slides):
            time.sleep(1)

    print("\n" + "=" * 60)
    print(f"处理完成！记录已保存到: {record_file}")

    # 打印统计摘要
    total = len(records)
    success = sum(1 for r in records.values() if r.get("html_status") in ("success", "skipped"))
    scores = [float(r["similarity_score"]) for r in records.values() if r.get("similarity_score")]
    avg_score = round(sum(scores) / len(scores), 2) if scores else 0

    print(f"\n统计摘要:")
    print(f"  总计: {total} 张")
    print(f"  成功: {success} 张")
    print(f"  平均相似度: {avg_score}")


if __name__ == "__main__":
    main()
