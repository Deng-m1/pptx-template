import json
import re
import statistics
from collections import Counter
from pathlib import Path

p = Path('/home/ubuntu/pptx-template/records/compare_100_160.jsonl')
text = p.read_text(encoding='utf-8')


def extract_json_objects(s: str):
    objs = []
    depth = 0
    start = None
    for i, ch in enumerate(s):
        if ch == '{':
            if depth == 0:
                start = i
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0 and start is not None:
                objs.append(s[start:i+1])
                start = None
    return objs


objs = [json.loads(x) for x in extract_json_objects(text)]
objs = [o for o in objs if o.get('status') == 'success']
for o in objs:
    o['slide'] = int(re.search(r'(\d+)', o['original']).group(1))
objs.sort(key=lambda x: x['slide'])

print(f'count {len(objs)}')
print(f'avg_score {statistics.mean(o["similarity_score"] for o in objs):.2f}')
print(f'median_score {statistics.median(o["similarity_score"] for o in objs):.2f}')
print(f'min_score {min(o["similarity_score"] for o in objs):.2f}')
print(f'max_score {max(o["similarity_score"] for o in objs):.2f}')
print('\nworst_20')
for o in sorted(objs, key=lambda x: x['similarity_score'])[:20]:
    print(f"slide_{o['slide']}\t{o['similarity_score']:.2f}\tssim={o['ssim']:.4f}\tdiff={o['pixel_diff_rate']:.4f}\t{o['grade']}")
print('\nbest_10')
for o in sorted(objs, key=lambda x: x['similarity_score'], reverse=True)[:10]:
    print(f"slide_{o['slide']}\t{o['similarity_score']:.2f}\tssim={o['ssim']:.4f}\tdiff={o['pixel_diff_rate']:.4f}\t{o['grade']}")
print('\nby_grade')
for k, v in Counter(o['grade'] for o in objs).items():
    print(f'{k}\t{v}')
