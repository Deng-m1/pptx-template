import base64

with open('/tmp/b64_dark2.txt') as f:
    b64 = f.read().strip()

html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1280">
<title>slide_6</title>
<style>
  * { margin:0; padding:0; box-sizing:border-box; }
  html,body { width:1280px; height:720px; overflow:hidden;
    font-family:'Microsoft YaHei','PingFang SC','Noto Sans SC',sans-serif; }
  .slide { width:1280px; height:720px; position:relative; overflow:hidden; background:#fff; }

  /* 左侧深蓝竖条 */
  .left-bar {
    position:absolute; left:0; top:0; width:70px; height:720px;
    background:#1535a0; z-index:3;
  }
  /* 竖排 CONTENTS 文字 — 超大，溢出到图片区域上方半透明叠加 */
  .vert-text {
    position:absolute;
    top:50%; left:35px;
    transform:translate(-50%, -50%) rotate(180deg);
    writing-mode:vertical-rl;
    text-orientation:mixed;
    font-size:680px; font-weight:900;
    color:#ffffff;
    line-height:1;
    opacity:0.18;
    white-space:nowrap;
    letter-spacing:-20px;
    z-index:4;
    pointer-events:none;
  }

  /* 建筑图区 */
  .photo {
    position:absolute; left:70px; top:0;
    width:430px; height:720px;
    background:url("data:image/jpeg;base64,''' + b64 + '''") center/cover no-repeat;
    background-position:30% 20%;
    z-index:1;
  }
  /* 图片上叠加暗色遮罩 */
  .photo-overlay {
    position:absolute; left:70px; top:0;
    width:430px; height:720px;
    background:rgba(5,15,60,0.35);
    z-index:2;
  }

  /* 右侧白底区 */
  .right-panel {
    position:absolute; left:500px; top:0;
    right:0; height:720px;
    background:#ffffff; z-index:3;
    padding:72px 70px 40px 60px;
  }
  /* 标题 */
  .main-title {
    font-size:62px; font-weight:900;
    color:#1535a0; letter-spacing:2px;
    line-height:1.1; margin-bottom:48px;
  }
  .main-title .sep {
    font-weight:400; margin:0 10px; color:#1535a0;
  }
  /* 目录条目 */
  .item {
    display:flex; align-items:baseline;
    margin-bottom:34px;
  }
  .item-num {
    font-size:56px; font-weight:900;
    color:#1535a0; min-width:100px;
    letter-spacing:-1px; line-height:1;
  }
  .item-text {
    margin-left:16px;
  }
  .item-text .zh {
    font-size:22px; font-weight:700;
    color:#1535a0; display:block;
    letter-spacing:1px;
  }
  .item-text .en {
    font-size:15px; font-weight:400;
    color:#4a6aaa; display:block;
    margin-top:3px; letter-spacing:0.5px;
  }
</style>
</head>
<body>
<div class="slide">
  <div class="left-bar"></div>
  <div class="vert-text">CONTENTS</div>
  <div class="photo"></div>
  <div class="photo-overlay"></div>
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
</html>'''

with open('/home/ubuntu/pptx-template/01高级商务蓝配色/html/slide_6.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('slide_6 written')
