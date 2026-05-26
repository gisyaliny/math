import os
import json
import re
import pathlib

EXCLUDE_DIRS = {'_build', '.git', '.ipynb_checkpoints', 'build'}
HEADING_PATTERN = re.compile(r'^(#{1,6})\s*(.*)$')
NUMBERING_PATTERN = re.compile(r'^\d+(?:\.\d+)*\.?\s*')


def normalize_markdown_lines(lines, first_heading_seen=False, previous_level=0):
    """Normalize markdown headings in a list of lines.

    - 保证文件中仅有一个 H1。第一个标题统一为 H1，后续的 H1 改为 H2。
    - 删除标题前的数字编号。
    - 防止标题级别跳跃过大，保持层次递增。
    """
    new_lines = []
    in_fence = False
    fence_char = None

    for line in lines:
        stripped = line.rstrip('\n')

        # 检查代码块 fence，避免修改代码块中的内容
        fence_match = re.match(r'^(```|~~~)', stripped)
        if fence_match:
            fence_token = fence_match.group(1)
            if not in_fence:
                in_fence = True
                fence_char = fence_token
            elif fence_token == fence_char:
                in_fence = False
                fence_char = None
            new_lines.append(line)
            continue

        if in_fence:
            new_lines.append(line)
            continue

        m = HEADING_PATTERN.match(stripped)
        if not m:
            new_lines.append(line)
            continue

        hashes, title = m.groups()
        level = len(hashes)

        # 删除标题前的数字编号
        title = NUMBERING_PATTERN.sub('', title).strip()

        if not first_heading_seen:
            # 第一个 heading 统一为 H1
            level = 1
            first_heading_seen = True
        else:
            if level == 1:
                level = 2
            if previous_level == 0:
                previous_level = 1
            if level > previous_level + 1:
                level = previous_level + 1

        previous_level = level
        new_line = '#' * level + ' ' + title + ('\n' if line.endswith('\n') else '')
        new_lines.append(new_line)

    return new_lines, first_heading_seen, previous_level


def process_file(path):
    suffix = path.suffix.lower()
    if suffix == '.md':
        content = path.read_text(encoding='utf-8').splitlines(keepends=True)
        new_content, _, _ = normalize_markdown_lines(content)
        if new_content != content:
            path.write_text(''.join(new_content), encoding='utf-8')
            return True
        return False

    if suffix == '.ipynb':
        nb_data = json.loads(path.read_text(encoding='utf-8'))
        changed = False
        first_heading_seen = False
        previous_level = 0
        for cell in nb_data.get('cells', []):
            if cell.get('cell_type') != 'markdown':
                continue
            source = cell.get('source', [])
            if isinstance(source, list):
                new_source, first_heading_seen, previous_level = normalize_markdown_lines(
                    source, first_heading_seen, previous_level
                )
            else:
                lines = source.splitlines(keepends=True)
                new_lines, first_heading_seen, previous_level = normalize_markdown_lines(
                    lines, first_heading_seen, previous_level
                )
                new_source = ''.join(new_lines)
            if new_source != source:
                cell['source'] = new_source
                changed = True
        if changed:
            path.write_text(json.dumps(nb_data, ensure_ascii=False, indent=1), encoding='utf-8')
        return changed

    return False


def should_skip(path):
    for part in path.parts:
        if part in EXCLUDE_DIRS:
            return True
    return False


def process_directory(root_dir):
    root = pathlib.Path(root_dir).resolve()
    for dirpath, dirnames, filenames in os.walk(root):
        # 排除特定目录
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for filename in filenames:
            if not filename.lower().endswith(('.md', '.ipynb')):
                continue
            file_path = pathlib.Path(dirpath) / filename
            rel_path = file_path.relative_to(root)
            if should_skip(file_path):
                continue
            print(f'正在处理: {rel_path}')
            try:
                changed = process_file(file_path)
                print('  已修改' if changed else '  无需修改')
            except Exception as exc:
                print(f'  处理失败: {exc}')


if __name__ == '__main__':
    target_directory = '.'
    if os.path.exists(target_directory):
        process_directory(target_directory)
    else:
        print(f'目录 {target_directory} 不存在，请检查路径。')