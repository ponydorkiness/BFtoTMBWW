import re
import sys
from collections import defaultdict

HEADER_RE = re.compile(r'^(\d+)\s+cond\s+(left|right)\b')

def parse_blocks(lines):
    blocks = []
    i, n = 0, len(lines)
    while i < n:
        m = HEADER_RE.match(lines[i].strip())
        if not m:
            i += 1
            continue
        bid, btype = m.groups()
        start = i
        cs = i+1
        ce = cs
        while ce < n and not HEADER_RE.match(lines[ce].strip()):
            ce += 1
        blocks.append({
            'id': bid, 'type': btype,
            'header_line': start,
            'content_start': cs,
            'content_end': ce
        })
        i = ce
    return blocks

def pair_blocks(blocks):
    pairs = []
    by_id = defaultdict(list)
    for b in blocks:
        by_id[b['id']].append(b)
    for bid, blist in by_id.items():
        stack = []
        for b in sorted(blist, key=lambda x: x['header_line']):
            if b['type']=='left':
                stack.append(b)
            else:
                if stack:
                    L = stack.pop()
                    pairs.append((L,b))
                else:
                    print(f"Warning: unmatched RIGHT {bid} at {b['header_line']+1}", file=sys.stderr)
        for L in stack:
            print(f"Warning: unmatched LEFT {L['id']} at {L['header_line']+1}", file=sys.stderr)
    return pairs

def extract_labels(lines, block, kind):
    pat = rf'\b({kind}\w+)\b'
    out = []
    for i in range(block['content_start'], block['content_end']):
        for m in re.finditer(pat, lines[i]):
            out.append((i, m.group(1)))
    return out

def swap_labels_in_file(infile, outfile):
    try:
        orig = open(infile).read().splitlines(keepends=True)
    except FileNotFoundError:
        print(f"Error: '{infile}' not found", file=sys.stderr)
        return

    blocks = parse_blocks(orig)
    pairs  = pair_blocks(blocks)
    # innermost first
    pairs.sort(key=lambda p: p[1]['header_line'] - p[0]['header_line'])

    out = orig.copy()

    for left, right in pairs:
        # get first continue & first jump from each, based on the ORIGINAL text
        lc = extract_labels(orig, left,  'countine')
        lj = extract_labels(orig, left,  'jump')
        rc = extract_labels(orig, right, 'countine')
        rj = extract_labels(orig, right, 'jump')
        if not (lc and lj and rc and rj):
            print(f"Warning: missing labels in ID {left['id']} – skipping", file=sys.stderr)
            continue
        left_c, left_j = lc[0][1], lj[0][1]
        right_c, right_j = rc[0][1], rj[0][1]

        # 1) cross‑swap jump/continue
        for i in range(left['content_start'], left['content_end']):
            out[i] = re.sub(rf'\b{re.escape(left_j)}\b', right_c, out[i])
        for i in range(right['content_start'], right['content_end']):
            out[i] = re.sub(rf'\b{re.escape(right_j)}\b', left_c, out[i])

        # 2) **in the right block only**: swap exactly two distinct countine… labels
        block_text = ''.join(out[right['content_start']:right['content_end']])
        found = re.findall(r'\b(countine\w+)\b', block_text)
        unique = list(dict.fromkeys(found))
        if len(unique) == 2:
            A, B = unique
            swap_count = 0
            for i in range(right['content_start'], right['content_end']):
                # only swap on the first two lines that actually contain A or B
                if swap_count < 2 and re.search(rf'\b({re.escape(A)}|{re.escape(B)})\b', out[i]):
                    # A -> TMP
                    out[i] = re.sub(rf'\b{re.escape(A)}\b', '__TMP_SWAP__', out[i])
                    # B -> A
                    out[i] = re.sub(rf'\b{re.escape(B)}\b', A, out[i])
                    # TMP -> B
                    out[i] = out[i].replace('__TMP_SWAP__', B)
                    swap_count += 1


    try:
        with open(outfile, 'w') as f:
            f.writelines(out)
        print(f"Done: wrote '{outfile}'")
    except IOError as e:
        print(f"Error writing '{outfile}': {e}", file=sys.stderr)

if __name__=='__main__':
    if len(sys.argv)!=3:
        print("Usage: python script.py <input> <output>", file=sys.stderr)
    else:
        swap_labels_in_file(sys.argv[1], sys.argv[2])
