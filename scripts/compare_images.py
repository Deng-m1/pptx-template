#!/usr/bin/env python3
"""
compare_images.py
对比原始幻灯片图片与 HTML 截图的视觉相似度（SSIM + 像素差异率）。
用法: python3 compare_images.py <original_png> <screenshot_png>
"""

import os
import sys
import json
import argparse
import numpy as np
from PIL import Image

TARGET_SIZE = (1280, 720)


def compute_ssim_channel(a: np.ndarray, b: np.ndarray) -> float:
    C1 = (0.01 * 255) ** 2
    C2 = (0.03 * 255) ** 2
    a, b = a.astype(np.float64), b.astype(np.float64)
    mu1, mu2 = a.mean(), b.mean()
    s1, s2 = a.var(), b.var()
    s12 = ((a - mu1) * (b - mu2)).mean()
    return float(((2 * mu1 * mu2 + C1) * (2 * s12 + C2)) / ((mu1**2 + mu2**2 + C1) * (s1 + s2 + C2)))


def compare_images(original_path: str, screenshot_path: str) -> dict:
    result = {
        "original": os.path.basename(original_path),
        "screenshot": os.path.basename(screenshot_path),
        "ssim": None, "pixel_diff_rate": None,
        "similarity_score": None, "grade": None,
        "status": "pending", "error": None,
    }
    try:
        img1 = Image.open(original_path).convert("RGB").resize(TARGET_SIZE, Image.LANCZOS)
        img2 = Image.open(screenshot_path).convert("RGB").resize(TARGET_SIZE, Image.LANCZOS)
        a1, a2 = np.array(img1), np.array(img2)
        diff = np.abs(a1.astype(np.float64) - a2.astype(np.float64))
        pixel_diff_rate = float(diff.mean() / 255.0)
        ssim = float(np.mean([compute_ssim_channel(a1[:,:,c], a2[:,:,c]) for c in range(3)]))
        score = round((ssim * 0.7 + (1 - pixel_diff_rate) * 0.3) * 100, 2)
        grade = "A（优秀）" if score >= 85 else "B（良好）" if score >= 70 else "C（一般）" if score >= 55 else "D（需改进）"
        result.update({"ssim": round(ssim, 4), "pixel_diff_rate": round(pixel_diff_rate, 4),
                        "similarity_score": score, "grade": grade, "status": "success"})
    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("original")
    parser.add_argument("screenshot")
    args = parser.parse_args()
    result = compare_images(args.original, args.screenshot)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result["status"] == "success" else 1)


if __name__ == "__main__":
    main()
