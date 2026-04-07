#!/usr/bin/env python3
"""生成 slide_3, slide_4, slide_5 的高保真 HTML（内嵌真实建筑图片）"""
import base64, os

BASE = '/home/ubuntu/pptx-template/01高级商务蓝配色'

with open(f'{BASE}/html/assets/bg_buildings.jpg', 'rb') as f:
    img_bld = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode()

with open(f'{BASE}/html/assets/bg_circle.jpg', 'rb') as f:
    img_cir = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode()

# ─────────────────────────────────────────────
# slide_3：全幅建筑背景，右上白色LOGO区，中间蓝色面板覆盖右侧，右下白色日期区
# ─────────────────────────────────────────────
slide3 = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1280">
<title>slide_3</title>
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html,body {{ width:1280px; height:720px; overflow:hidden;
    font-family:'Microsoft YaHei','PingFang SC','Noto Sans SC',sans-serif; }}
  .slide {{ width:1280px; height:720px; position:relative; overflow:hidden; }}

  .bg-photo {{
    position:absolute; inset:0;
    background:url("{img_bld}") center/cover no-repeat;
    background-position:25% 45%;
    z-index:0;
  }}
  /* 右上白色区（LOGO 所在，约 130px 高，从 left=440px 到右边） */
  .top-right {{
    position:absolute; right:0; top:0;
    width:840px; height:130px;
    background:#ffffff; z-index:2;
  }}
  /* 右下白色区（日期所在，约 130px 高） */
  .bottom-right {{
    position:absolute; right:0; bottom:0;
    width:840px; height:130px;
    background:#ffffff; z-index:2;
  }}
  /* LOGO */
  .logo {{
    position:absolute; right:60px; top:38px;
    font-size:24px; font-weight:700;
    color:#1c3d7a; letter-spacing:3px; z-index:5;
  }}
  /* 蓝色面板：left=440px, top=130px, right=0, height=460px */
  .blue-panel {{
    position:absolute;
    left:440px; top:130px;
    right:0; height:460px;
    background:#1c3d7a; z-index:3;
    padding:50px 60px 40px 64px;
    display:flex; flex-direction:column; justify-content:flex-start;
  }}
  /* 面板标题：原图"工作汇报"(粗)+"通用总结模版"(略细)，约 52px，白色 */
  .panel-title {{
    font-size:52px; font-weight:900;
    color:#ffffff; letter-spacing:4px; line-height:1.15;
  }}
  .panel-title .thin {{ font-weight:700; }}
  /* 汇报人：右对齐，约 18px，浅蓝 */
  .panel-reporter {{
    margin-top:14px;
    font-size:18px; color:#a8c8e8;
    letter-spacing:1px; text-align:right;
  }}
  /* 描述：居中，约 13px，浅色 */
  .panel-desc {{
    margin-top:34px;
    font-size:13px; color:#c8ddf0;
    line-height:1.85; text-align:center;
  }}
  /* 日期 */
  .date {{
    position:absolute; right:60px; bottom:38px;
    font-size:17px; color:#1c3d7a;
    letter-spacing:1px; z-index:5;
  }}
  .date strong {{ font-weight:900; color:#1c3d7a; }}
</style>
</head>
<body>
<div class="slide">
  <div class="bg-photo"></div>
  <div class="top-right"></div>
  <div class="bottom-right"></div>
  <div class="logo">LOGO</div>
  <div class="blue-panel">
    <div class="panel-title"><span>工作汇报</span><span class="thin">通用总结模版</span></div>
    <div class="panel-reporter">汇报人：小序</div>
    <div class="panel-desc">Here you can describe the main work report content. Here you can describe the main work report content. Here you can describe the main work report content.</div>
  </div>
  <div class="date">汇报时间：<strong>8888年88月88日</strong></div>
</div>
</body>
</html>"""

# ─────────────────────────────────────────────
# slide_4：白底，左侧文字，右侧矩形建筑图（从 left≈636px，top≈40px）
# ─────────────────────────────────────────────
slide4 = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1280">
<title>slide_4</title>
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html,body {{ width:1280px; height:720px; overflow:hidden;
    font-family:'Microsoft YaHei','PingFang SC','Noto Sans SC',sans-serif;
    background:#ffffff; }}
  .slide {{ width:1280px; height:720px; position:relative; background:#fff; }}

  /* 右侧建筑图（矩形，无圆角） */
  .img-right {{
    position:absolute;
    left:636px; top:40px;
    width:604px; height:638px;
    background:url("{img_bld}") center/cover no-repeat;
    background-position:35% 25%;
    z-index:1;
  }}
  .logo {{
    position:absolute; left:76px; top:38px;
    font-size:22px; font-weight:700;
    color:#1c3d7a; letter-spacing:3px; z-index:3;
  }}
  /* 主标题：约 64px，字重900，深蓝，top≈150px */
  .title-h1 {{
    position:absolute; left:76px; top:150px;
    font-size:64px; font-weight:900;
    color:#1c3d7a; letter-spacing:5px; z-index:3;
  }}
  /* 副标题：约 48px，字重700，深蓝，top≈234px */
  .title-h2 {{
    position:absolute; left:76px; top:234px;
    font-size:48px; font-weight:700;
    color:#1c3d7a; letter-spacing:4px; z-index:3;
  }}
  .reporter {{
    position:absolute; left:76px; top:356px;
    font-size:17px; color:#3a6aaa;
    letter-spacing:1px; z-index:3;
  }}
  .desc {{
    position:absolute; left:76px; top:406px;
    width:460px;
    font-size:13px; color:#555;
    line-height:1.85; z-index:3;
  }}
  .date {{
    position:absolute; left:76px; bottom:36px;
    font-size:16px; color:#3a6aaa;
    letter-spacing:1px; z-index:3;
  }}
  .date strong {{ font-weight:900; color:#1c3d7a; }}
</style>
</head>
<body>
<div class="slide">
  <div class="img-right"></div>
  <div class="logo">LOGO</div>
  <div class="title-h1">工作汇报</div>
  <div class="title-h2">通用总结模版</div>
  <div class="reporter">汇报人：小序</div>
  <div class="desc">Here you can describe the main work report content. Here you can describe the main work report content. Here you can describe the main work report content.</div>
  <div class="date">汇报时间：<strong>8888年88月88日</strong></div>
</div>
</body>
</html>"""

# ─────────────────────────────────────────────
# slide_5：左侧建筑背景（约 668px），右侧白底，右对齐文字
# ─────────────────────────────────────────────
slide5 = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1280">
<title>slide_5</title>
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html,body {{ width:1280px; height:720px; overflow:hidden;
    font-family:'Microsoft YaHei','PingFang SC','Noto Sans SC',sans-serif; }}
  .slide {{ width:1280px; height:720px; position:relative; overflow:hidden; }}

  /* 左侧建筑背景 */
  .bg-left {{
    position:absolute; left:0; top:0;
    width:668px; height:720px;
    background:url("{img_bld}") center/cover no-repeat;
    background-position:15% 40%;
    z-index:0;
  }}
  /* 右侧白色 */
  .bg-right {{
    position:absolute; left:668px; top:0;
    width:612px; height:720px;
    background:#ffffff; z-index:1;
  }}
  .logo {{
    position:absolute; right:60px; top:36px;
    font-size:22px; font-weight:700;
    color:#1c3d7a; letter-spacing:3px; z-index:5;
  }}
  .title-h1 {{
    position:absolute; right:60px; top:148px;
    font-size:68px; font-weight:900;
    color:#1c3d7a; letter-spacing:4px;
    text-align:right; z-index:5;
  }}
  .title-h2 {{
    position:absolute; right:60px; top:240px;
    font-size:52px; font-weight:700;
    color:#1c3d7a; letter-spacing:3px;
    text-align:right; z-index:5;
  }}
  .reporter {{
    position:absolute; right:60px; top:368px;
    font-size:17px; color:#3a6aaa;
    letter-spacing:1px; text-align:right; z-index:5;
  }}
  .desc {{
    position:absolute; right:60px; top:418px;
    width:520px;
    font-size:13px; color:#555;
    line-height:1.85; text-align:right; z-index:5;
  }}
  .date {{
    position:absolute; right:60px; bottom:36px;
    font-size:17px; color:#3a6aaa;
    letter-spacing:1px; text-align:right; z-index:5;
  }}
  .date strong {{ font-weight:900; color:#1c3d7a; }}
</style>
</head>
<body>
<div class="slide">
  <div class="bg-left"></div>
  <div class="bg-right"></div>
  <div class="logo">LOGO</div>
  <div class="title-h1">工作汇报</div>
  <div class="title-h2">通用总结模版</div>
  <div class="reporter">汇报人：小序</div>
  <div class="desc">Here you can describe the main work report content. Here you can describe the main work report content. Here you can describe the main work report content.</div>
  <div class="date">汇报时间：<strong>8888年88月88日</strong></div>
</div>
</body>
</html>"""

out_dir = f'{BASE}/html'
for name, content in [('slide_3.html', slide3), ('slide_4.html', slide4), ('slide_5.html', slide5)]:
    path = os.path.join(out_dir, name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"{name} written ({len(content):,} bytes)")
