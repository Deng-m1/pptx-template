#!/usr/bin/env python3
from pathlib import Path

BASE = Path('/home/ubuntu/pptx-template/02高端品牌PPT参考')
SLIDES = BASE / 'slides'
HTML = BASE / 'html'

TARGET_DIRS = [
    'sc_01_white_gold_project_proposal',
    'sc_02_gold_elegant_branding_kit',
    'sc_03_hotel_sales_strategy_mix',
    'sc_04_elegant_royal_background',
    'sc_05_elegant_black_gold',
    'sc_07_elegant_fancy_pitch_deck',
    'sc_09_elegant_simple_slides',
    'sc_10_aesthetic_elegant_professional',
]

SHARED_CSS = """* { box-sizing: border-box; margin: 0; padding: 0; }
html, body {
  width: 1280px;
  height: 720px;
  overflow: hidden;
  background: #ffffff;
  font-family: Arial, Helvetica, sans-serif;
}
body { position: relative; }
.slide {
  position: relative;
  width: 1280px;
  height: 720px;
  overflow: hidden;
  background-position: center center;
  background-repeat: no-repeat;
  background-size: cover;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang=\"zh-CN\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=1280, initial-scale=1.0\" />
  <title>{title}</title>
  <style>
{css}
  </style>
</head>
<body>
  <main class=\"slide\" style=\"background-image:url('{image_rel}');\">
    <h1 class=\"sr-only\">{title}</h1>
  </main>
</body>
</html>
"""


def main() -> None:
    generated = []
    missing = []

    for dirname in TARGET_DIRS:
        slide_dir = SLIDES / dirname
        html_dir = HTML / dirname
        if not slide_dir.exists():
            missing.append(dirname)
            continue
        html_dir.mkdir(parents=True, exist_ok=True)
        for image_path in sorted(slide_dir.glob('slide_*.jpg')):
            slide_name = image_path.stem
            title = f'{dirname} {slide_name}'
            image_rel = f'../../slides/{dirname}/{image_path.name}'
            html = HTML_TEMPLATE.format(title=title, css=SHARED_CSS, image_rel=image_rel)
            (html_dir / f'{slide_name}.html').write_text(html, encoding='utf-8')
            generated.append(str(html_dir / f'{slide_name}.html'))

    report_lines = [
        '# SlidesCarnival HTML 基线生成报告',
        '',
        f'- 已生成 HTML 文件数：{len(generated)}',
        f'- 缺失源目录：{", ".join(missing) if missing else "无"}',
        '',
        '## 已处理目录',
        '',
    ]
    for dirname in TARGET_DIRS:
        slide_dir = SLIDES / dirname
        count = len(list(slide_dir.glob('slide_*.jpg'))) if slide_dir.exists() else 0
        report_lines.append(f'- {dirname}: {count} 张')

    report_dir = BASE.parent / 'records'
    report_dir.mkdir(parents=True, exist_ok=True)
    (report_dir / 'sc_baseline_generation.md').write_text('\n'.join(report_lines) + '\n', encoding='utf-8')
    print(f'Generated {len(generated)} HTML files.')
    if missing:
        print('Missing:', ', '.join(missing))


if __name__ == '__main__':
    main()
