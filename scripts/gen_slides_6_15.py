#!/usr/bin/env python3
"""生成 slide_6 ~ slide_15 的高保真 HTML"""
import base64, os

BASE = '/home/ubuntu/pptx-template/01高级商务蓝配色'
ASSETS = f'{BASE}/html/assets'
OUT = f'{BASE}/html'

with open(f'{ASSETS}/bg_buildings.jpg', 'rb') as f:
    img_bld = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode()

with open(f'{ASSETS}/bg_circle.jpg', 'rb') as f:
    img_cir = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode()

# ─────────────────────────────────────────────
# slide_6：目录页 A
# 左侧深蓝竖条（约230px）+ 建筑图（约430px）+ 右侧白底目录区
# 左侧竖排"CONTENTS"大字（略深蓝，字间距极大）
# ─────────────────────────────────────────────
slide6 = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1280">
<title>slide_6</title>
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html,body {{ width:1280px; height:720px; overflow:hidden;
    font-family:'Microsoft YaHei','PingFang SC','Noto Sans SC',sans-serif; }}
  .slide {{ width:1280px; height:720px; position:relative; overflow:hidden; background:#fff; }}

  /* 左侧深蓝竖条 */
  .left-bar {{
    position:absolute; left:0; top:0; width:230px; height:720px;
    background:#1a3a9e; z-index:2;
    display:flex; align-items:center; justify-content:center;
  }}
  /* 竖排 CONTENTS 文字 */
  .left-bar .vert-text {{
    writing-mode:vertical-rl;
    text-orientation:mixed;
    transform:rotate(180deg);
    font-size:88px; font-weight:900;
    color:#0f2a8a; letter-spacing:18px;
    line-height:1; user-select:none;
    opacity:0.55;
  }}
  /* 建筑图区（紧贴左侧竖条右边） */
  .photo {{
    position:absolute; left:230px; top:0;
    width:430px; height:720px;
    background:url("{img_bld}") center/cover no-repeat;
    background-position:30% 20%;
    z-index:1;
  }}
  /* 右侧白底区 */
  .right-panel {{
    position:absolute; left:660px; top:0;
    right:0; height:720px;
    background:#ffffff; z-index:3;
    padding:72px 70px 40px 60px;
  }}
  /* 标题 */
  .main-title {{
    font-size:56px; font-weight:900;
    color:#1a3a9e; letter-spacing:2px;
    line-height:1.1; margin-bottom:52px;
  }}
  .main-title .sep {{
    font-weight:400; margin:0 10px; color:#1a3a9e;
  }}
  .main-title .en {{
    font-weight:700;
  }}
  /* 目录条目 */
  .item {{
    display:flex; align-items:baseline;
    margin-bottom:36px;
  }}
  .item-num {{
    font-size:52px; font-weight:900;
    color:#1a3a9e; min-width:90px;
    letter-spacing:-1px; line-height:1;
  }}
  .item-text {{
    margin-left:14px;
  }}
  .item-text .zh {{
    font-size:22px; font-weight:700;
    color:#1a3a9e; display:block;
    letter-spacing:1px;
  }}
  .item-text .en {{
    font-size:15px; font-weight:400;
    color:#3a6aaa; display:block;
    margin-top:3px; letter-spacing:0.5px;
  }}
</style>
</head>
<body>
<div class="slide">
  <div class="left-bar">
    <span class="vert-text">CONTENTS</span>
  </div>
  <div class="photo"></div>
  <div class="right-panel">
    <div class="main-title">目录<span class="sep">|</span><span class="en">Contents</span></div>
    <div class="item">
      <div class="item-num">01-</div>
      <div class="item-text">
        <span class="zh">工作完成情况</span>
        <span class="en">work completion</span>
      </div>
    </div>
    <div class="item">
      <div class="item-num">02-</div>
      <div class="item-text">
        <span class="zh">工作不足之处</span>
        <span class="en">inadequacies of work</span>
      </div>
    </div>
    <div class="item">
      <div class="item-num">03-</div>
      <div class="item-text">
        <span class="zh">业绩成果展示</span>
        <span class="en">performance display</span>
      </div>
    </div>
    <div class="item">
      <div class="item-num">04-</div>
      <div class="item-text">
        <span class="zh">明年的工作计划</span>
        <span class="en">next year's work plan</span>
      </div>
    </div>
  </div>
</div>
</body>
</html>"""

# ─────────────────────────────────────────────
# slide_7：目录页 B
# 全幅建筑背景 + 半透明深蓝矩形面板（含左侧标题+竖线+右侧目录）
# ─────────────────────────────────────────────
slide7 = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1280">
<title>slide_7</title>
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html,body {{ width:1280px; height:720px; overflow:hidden;
    font-family:'Microsoft YaHei','PingFang SC','Noto Sans SC',sans-serif; }}
  .slide {{ width:1280px; height:720px; position:relative; overflow:hidden; }}

  .bg {{
    position:absolute; inset:0;
    background:url("{img_bld}") center/cover no-repeat;
    background-position:30% 25%;
    z-index:0;
  }}
  /* 半透明深蓝面板 */
  .panel {{
    position:absolute;
    left:120px; top:120px; right:0; bottom:120px;
    background:rgba(20,50,150,0.88);
    z-index:2;
    display:flex; align-items:stretch;
  }}
  /* 面板左侧：标题区 */
  .panel-left {{
    width:380px; padding:50px 40px 50px 60px;
    display:flex; align-items:center;
    flex-shrink:0;
  }}
  .panel-left .title {{
    font-size:52px; font-weight:900;
    color:#ffffff; letter-spacing:2px; line-height:1.2;
  }}
  .panel-left .title .sep {{
    font-weight:300; margin:0 8px;
  }}
  /* 竖线分隔 */
  .divider {{
    width:2px; background:rgba(255,255,255,0.35);
    margin:30px 0; flex-shrink:0;
  }}
  /* 面板右侧：目录区 */
  .panel-right {{
    flex:1; padding:40px 60px 40px 50px;
    display:flex; flex-direction:column; justify-content:space-around;
  }}
  .item {{
    display:flex; align-items:baseline;
  }}
  .item-num {{
    font-size:48px; font-weight:900;
    color:#ffffff; min-width:86px;
    letter-spacing:-1px; line-height:1;
  }}
  .item-text {{ margin-left:12px; }}
  .item-text .zh {{
    font-size:20px; font-weight:700;
    color:#ffffff; display:block; letter-spacing:1px;
  }}
  .item-text .en {{
    font-size:14px; font-weight:400;
    color:rgba(255,255,255,0.7); display:block;
    margin-top:3px; letter-spacing:0.5px;
  }}
</style>
</head>
<body>
<div class="slide">
  <div class="bg"></div>
  <div class="panel">
    <div class="panel-left">
      <div class="title">目录<span class="sep">|</span>Contents</div>
    </div>
    <div class="divider"></div>
    <div class="panel-right">
      <div class="item">
        <div class="item-num">01-</div>
        <div class="item-text">
          <span class="zh">工作完成情况</span>
          <span class="en">work completion</span>
        </div>
      </div>
      <div class="item">
        <div class="item-num">02-</div>
        <div class="item-text">
          <span class="zh">工作不足之处</span>
          <span class="en">inadequacies of work</span>
        </div>
      </div>
      <div class="item">
        <div class="item-num">03-</div>
        <div class="item-text">
          <span class="zh">业绩成果展示</span>
          <span class="en">performance display</span>
        </div>
      </div>
      <div class="item">
        <div class="item-num">04-</div>
        <div class="item-text">
          <span class="zh">明年的工作计划</span>
          <span class="en">next year's work plan</span>
        </div>
      </div>
    </div>
  </div>
</div>
</body>
</html>"""

# ─────────────────────────────────────────────
# slide_8：目录页 C（圆形数字 3x2 网格）
# 左侧蓝色矩形（建筑图+蓝色蒙层）+ 右侧白底 6 圆形网格
# ─────────────────────────────────────────────
slide8 = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1280">
<title>slide_8</title>
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html,body {{ width:1280px; height:720px; overflow:hidden;
    font-family:'Microsoft YaHei','PingFang SC','Noto Sans SC',sans-serif;
    background:#fff; }}
  .slide {{ width:1280px; height:720px; position:relative; background:#fff; }}

  /* 左侧蓝色矩形（建筑图+蓝色蒙层） */
  .left-panel {{
    position:absolute; left:0; top:0;
    width:430px; height:720px;
    background:url("{img_bld}") center/cover no-repeat;
    background-position:20% 30%;
    z-index:1;
  }}
  .left-panel::after {{
    content:''; position:absolute; inset:0;
    background:rgba(20,50,160,0.72);
  }}
  .left-content {{
    position:absolute; left:0; top:0;
    width:430px; height:720px;
    z-index:3;
    padding:60px 44px 40px 44px;
    display:flex; flex-direction:column; justify-content:flex-start;
  }}
  .left-title-zh {{
    font-size:56px; font-weight:900;
    color:#ffffff; letter-spacing:3px;
  }}
  .left-title-en {{
    font-size:26px; font-weight:900;
    color:#ffffff; letter-spacing:4px;
    margin-top:6px;
  }}
  .left-desc {{
    margin-top:40px;
    font-size:13px; color:rgba(255,255,255,0.75);
    line-height:1.85; text-align:justify;
  }}

  /* 右侧白底区 */
  .right-panel {{
    position:absolute; left:430px; top:0;
    right:0; height:720px;
    background:#fff; z-index:2;
    padding:40px 60px 40px 60px;
    display:flex; align-items:center;
  }}
  /* 3x2 网格 */
  .grid {{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    grid-template-rows:repeat(2,1fr);
    gap:20px 30px;
    width:100%;
  }}
  .grid-item {{
    display:flex; flex-direction:column; align-items:center;
  }}
  .circle {{
    width:158px; height:158px;
    border-radius:50%;
    background:#1a3a9e;
    display:flex; align-items:center; justify-content:center;
    flex-shrink:0;
  }}
  .circle span {{
    font-size:66px; font-weight:900;
    color:#ffffff; letter-spacing:-2px;
    line-height:1;
  }}
  .grid-item .zh {{
    margin-top:14px;
    font-size:20px; font-weight:700;
    color:#1a3a9e; text-align:center;
    letter-spacing:1px;
  }}
  .grid-item .en {{
    margin-top:4px;
    font-size:13px; font-weight:400;
    color:#3a6aaa; text-align:center;
    letter-spacing:0.5px;
  }}
</style>
</head>
<body>
<div class="slide">
  <div class="left-panel"></div>
  <div class="left-content">
    <div class="left-title-zh">目录</div>
    <div class="left-title-en">CONTENTS</div>
    <div class="left-desc">Here you can describe the main work report content. Here you can describe the main work report content. Here you can describe the main work report content.</div>
  </div>
  <div class="right-panel">
    <div class="grid">
      <div class="grid-item">
        <div class="circle"><span>01</span></div>
        <div class="zh">工作完成情况</div>
        <div class="en">work completion</div>
      </div>
      <div class="grid-item">
        <div class="circle"><span>02</span></div>
        <div class="zh">工作完成情况</div>
        <div class="en">work completion</div>
      </div>
      <div class="grid-item">
        <div class="circle"><span>03</span></div>
        <div class="zh">工作完成情况</div>
        <div class="en">work completion</div>
      </div>
      <div class="grid-item">
        <div class="circle"><span>04</span></div>
        <div class="zh">工作完成情况</div>
        <div class="en">work completion</div>
      </div>
      <div class="grid-item">
        <div class="circle"><span>05</span></div>
        <div class="zh">工作完成情况</div>
        <div class="en">work completion</div>
      </div>
      <div class="grid-item">
        <div class="circle"><span>06</span></div>
        <div class="zh">工作完成情况</div>
        <div class="en">work completion</div>
      </div>
    </div>
  </div>
</div>
</body>
</html>"""

# ─────────────────────────────────────────────
# slide_9：目录页 D
# 全幅建筑背景 + 左侧竖排"CONTENTS"水印 + 右侧深蓝实色面板（约right 52%）
# ─────────────────────────────────────────────
slide9 = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1280">
<title>slide_9</title>
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html,body {{ width:1280px; height:720px; overflow:hidden;
    font-family:'Microsoft YaHei','PingFang SC','Noto Sans SC',sans-serif; }}
  .slide {{ width:1280px; height:720px; position:relative; overflow:hidden; }}

  .bg {{
    position:absolute; inset:0;
    background:url("{img_bld}") center/cover no-repeat;
    background-position:20% 30%;
    z-index:0;
  }}
  /* 左侧竖排水印文字 */
  .watermark {{
    position:absolute; left:-30px; top:0;
    height:720px; width:260px;
    display:flex; align-items:center; justify-content:center;
    z-index:2;
  }}
  .watermark span {{
    writing-mode:vertical-rl;
    text-orientation:mixed;
    transform:rotate(180deg);
    font-size:120px; font-weight:900;
    color:rgba(255,255,255,0.18);
    letter-spacing:20px; line-height:1;
    user-select:none;
  }}
  /* 右侧深蓝实色面板 */
  .right-panel {{
    position:absolute; left:620px; top:0;
    right:0; height:720px;
    background:#1a3a9e;
    z-index:3;
    padding:60px 70px 50px 64px;
    display:flex; flex-direction:column; justify-content:flex-start;
  }}
  .main-title {{
    font-size:52px; font-weight:900;
    color:#ffffff; letter-spacing:2px;
    line-height:1.1; margin-bottom:48px;
  }}
  .main-title .sep {{ font-weight:300; margin:0 8px; }}
  .item {{
    display:flex; align-items:baseline;
    margin-bottom:34px;
  }}
  .item-num {{
    font-size:48px; font-weight:900;
    color:#ffffff; min-width:84px;
    letter-spacing:-1px; line-height:1;
  }}
  .item-text {{ margin-left:10px; }}
  .item-text .zh {{
    font-size:20px; font-weight:700;
    color:#ffffff; display:block; letter-spacing:1px;
  }}
  .item-text .en {{
    font-size:14px; font-weight:400;
    color:rgba(255,255,255,0.65); display:block;
    margin-top:3px; letter-spacing:0.5px;
  }}
</style>
</head>
<body>
<div class="slide">
  <div class="bg"></div>
  <div class="watermark"><span>CONTENTS</span></div>
  <div class="right-panel">
    <div class="main-title">目录<span class="sep">|</span>Contents</div>
    <div class="item">
      <div class="item-num">01-</div>
      <div class="item-text">
        <span class="zh">工作完成情况</span>
        <span class="en">work completion</span>
      </div>
    </div>
    <div class="item">
      <div class="item-num">02-</div>
      <div class="item-text">
        <span class="zh">工作不足之处</span>
        <span class="en">inadequacies of work</span>
      </div>
    </div>
    <div class="item">
      <div class="item-num">03-</div>
      <div class="item-text">
        <span class="zh">业绩成果展示</span>
        <span class="en">performance display</span>
      </div>
    </div>
    <div class="item">
      <div class="item-num">04-</div>
      <div class="item-text">
        <span class="zh">明年的工作计划</span>
        <span class="en">next year's work plan</span>
      </div>
    </div>
  </div>
</div>
</body>
</html>"""

# ─────────────────────────────────────────────
# slide_10：目录页 E
# 顶部深蓝横条（约280px）+ 左下建筑图 + 右下白底 2x2 目录
# ─────────────────────────────────────────────
slide10 = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1280">
<title>slide_10</title>
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html,body {{ width:1280px; height:720px; overflow:hidden;
    font-family:'Microsoft YaHei','PingFang SC','Noto Sans SC',sans-serif;
    background:#fff; }}
  .slide {{ width:1280px; height:720px; position:relative; background:#fff; }}

  /* 顶部深蓝横条 */
  .top-bar {{
    position:absolute; left:0; top:0;
    width:1280px; height:280px;
    background:#1a3a9e; z-index:2;
  }}
  /* 顶部横条内的建筑图（左侧，约490px宽，覆盖整个高度） */
  .top-photo {{
    position:absolute; left:0; top:0;
    width:490px; height:280px;
    background:url("{img_bld}") center/cover no-repeat;
    background-position:25% 20%;
    z-index:3;
  }}
  /* 顶部标题（在横条右侧） */
  .top-title {{
    position:absolute; left:530px; top:0;
    right:0; height:280px;
    z-index:4;
    display:flex; align-items:center;
    padding-left:40px;
  }}
  .top-title span {{
    font-size:62px; font-weight:900;
    color:#ffffff; letter-spacing:2px;
  }}
  .top-title .sep {{ font-weight:300; margin:0 10px; }}

  /* 左下建筑图 */
  .bottom-photo {{
    position:absolute; left:0; top:280px;
    width:490px; height:440px;
    background:url("{img_bld}") center/cover no-repeat;
    background-position:25% 60%;
    z-index:1;
  }}
  /* 右下白底目录区 */
  .bottom-right {{
    position:absolute; left:490px; top:280px;
    right:0; height:440px;
    background:#fff; z-index:2;
    padding:50px 70px 40px 60px;
    display:grid;
    grid-template-columns:1fr 1fr;
    grid-template-rows:1fr 1fr;
    gap:20px 30px;
    align-items:center;
  }}
  .item {{
    display:flex; align-items:baseline;
  }}
  .item-num {{
    font-size:48px; font-weight:900;
    color:#1a3a9e; min-width:80px;
    letter-spacing:-1px; line-height:1;
  }}
  .item-text {{ margin-left:10px; }}
  .item-text .zh {{
    font-size:20px; font-weight:700;
    color:#1a3a9e; display:block; letter-spacing:1px;
  }}
  .item-text .en {{
    font-size:13px; font-weight:400;
    color:#3a6aaa; display:block;
    margin-top:3px; letter-spacing:0.5px;
  }}
</style>
</head>
<body>
<div class="slide">
  <div class="top-bar"></div>
  <div class="top-photo"></div>
  <div class="top-title">
    <span>目录<span class="sep">|</span>Contents</span>
  </div>
  <div class="bottom-photo"></div>
  <div class="bottom-right">
    <div class="item">
      <div class="item-num">01-</div>
      <div class="item-text">
        <span class="zh">工作完成情况</span>
        <span class="en">work completion</span>
      </div>
    </div>
    <div class="item">
      <div class="item-num">03-</div>
      <div class="item-text">
        <span class="zh">业绩成果展示</span>
        <span class="en">performance display</span>
      </div>
    </div>
    <div class="item">
      <div class="item-num">02-</div>
      <div class="item-text">
        <span class="zh">工作不足之处</span>
        <span class="en">inadequacies of work</span>
      </div>
    </div>
    <div class="item">
      <div class="item-num">04-</div>
      <div class="item-text">
        <span class="zh">明年的工作计划</span>
        <span class="en">next year's work plan</span>
      </div>
    </div>
  </div>
</div>
</body>
</html>"""

# ─────────────────────────────────────────────
# slide_11~15：章节过渡页（数字 1~5）
# 全幅深蓝背景 + 左侧超大白色数字 + 右侧标题+胶囊按钮+描述+底部线
# ─────────────────────────────────────────────
def make_chapter_slide(num):
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1280">
<title>slide_{10+num}</title>
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html,body {{ width:1280px; height:720px; overflow:hidden;
    font-family:'Microsoft YaHei','PingFang SC','Noto Sans SC',sans-serif;
    background:#1a3a9e; }}
  .slide {{ width:1280px; height:720px; position:relative; background:#1a3a9e; overflow:hidden; }}

  /* 超大数字装饰（从左边缘溢出） */
  .big-num {{
    position:absolute;
    left:-30px; top:50%;
    transform:translateY(-52%);
    font-size:560px; font-weight:900;
    color:#ffffff; line-height:1;
    letter-spacing:-20px;
    user-select:none;
    z-index:1;
  }}
  /* 右侧内容区 */
  .content {{
    position:absolute;
    left:500px; top:0; right:0; height:720px;
    z-index:2;
    padding:130px 70px 60px 0;
    display:flex; flex-direction:column; justify-content:flex-start;
  }}
  .title-zh {{
    font-size:76px; font-weight:900;
    color:#ffffff; letter-spacing:3px; line-height:1.1;
    margin-bottom:16px;
  }}
  .title-en {{
    font-size:28px; font-weight:400;
    color:rgba(255,255,255,0.75);
    letter-spacing:3px; margin-bottom:36px;
  }}
  /* 胶囊按钮行 */
  .btn-row {{
    display:flex; gap:24px; margin-bottom:36px;
  }}
  .btn {{
    display:flex; align-items:center;
    padding:14px 32px;
    background:rgba(255,255,255,0.18);
    border:1.5px solid rgba(255,255,255,0.35);
    border-radius:30px;
    font-size:18px; font-weight:700;
    color:#1a3a9e;
    background:rgba(230,235,255,0.92);
    letter-spacing:1px;
    cursor:default;
  }}
  .btn .arrow {{
    margin-right:10px; font-size:16px;
    color:#1a3a9e;
  }}
  /* 描述文字 */
  .desc {{
    font-size:15px; color:rgba(255,255,255,0.8);
    line-height:1.85; max-width:560px;
    margin-bottom:40px;
  }}
  /* 底部横线 */
  .bottom-line {{
    width:500px; height:1.5px;
    background:rgba(255,255,255,0.4);
    margin-top:auto;
  }}
</style>
</head>
<body>
<div class="slide">
  <div class="big-num">{num}</div>
  <div class="content">
    <div class="title-zh">工作汇报总结</div>
    <div class="title-en">summary of work report</div>
    <div class="btn-row">
      <div class="btn"><span class="arrow">▶</span>项目1工作进度</div>
      <div class="btn"><span class="arrow">▶</span>项目2工作进度</div>
    </div>
    <div class="desc">Here you can describe the main work report content. Here you can describe the main work report content. Here you can describe the main work report content.</div>
    <div class="bottom-line"></div>
  </div>
</div>
</body>
</html>"""

# 写出所有文件
slides = {
    'slide_6.html': slide6,
    'slide_7.html': slide7,
    'slide_8.html': slide8,
    'slide_9.html': slide9,
    'slide_10.html': slide10,
}
for i in range(1, 6):
    slides[f'slide_{10+i}.html'] = make_chapter_slide(i)

for name, content in slides.items():
    path = os.path.join(OUT, name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"{name} written ({len(content):,} bytes)")
