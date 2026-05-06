import os
import json
import re

def remove_header_numbering(content):
    """
    使用正则表达式去除 H1-H3 的数字排序
    匹配模式：开始的 1-3 个 #，后跟数字、点、空格
    例如: # 1. Title -> # Title
         ## 2.1 Sub -> ## Sub
         ### 3. Topic -> ### Topic
    """
    # 正则解释:
    # ^(#{1,3})\s+      : 匹配行首 1 到 3 个 # 符号及随后的空格
    # \d+(?:\.\d+)*\.?  : 匹配数字(如 1, 1.1, 2.)
    # \s* : 匹配数字后的多余空格
    pattern = r'^(#{1,3})\s+\d+(?:\.\d+)*\.?\s*'
    
    new_content = []
    for line in content:
        # sub 函数执行替换
        new_line = re.sub(pattern, r'\1 ', line)
        new_content.append(new_line)
    return new_content

def process_notebooks(root_dir):
    # 遍历目录
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.ipynb'):
                file_path = os.path.join(root, file)
                print(f"正在处理: {file_path}")
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        nb_data = json.load(f)
                    
                    changed = False
                    # 遍历 notebook 中的每一个 cell
                    for cell in nb_data.get('cells', []):
                        if cell.get('cell_type') == 'markdown':
                            original_source = cell.get('source', [])
                            # 处理 source 是列表或字符串的情况
                            if isinstance(original_source, list):
                                new_source = remove_header_numbering(original_source)
                                if new_source != original_source:
                                    cell['source'] = new_source
                                    changed = True
                            elif isinstance(original_source, str):
                                # 如果是字符串，先拆分处理再合并
                                lines = original_source.splitlines(keepends=True)
                                new_lines = remove_header_numbering(lines)
                                new_str = "".join(new_lines)
                                if new_str != original_source:
                                    cell['source'] = new_str
                                    changed = True
                    
                    if changed:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            json.dump(nb_data, f, ensure_ascii=False, indent=1)
                        print(f"成功更新: {file_path}")
                    else:
                        print(f"无需修改: {file_path}")
                        
                except Exception as e:
                    print(f"处理文件 {file} 时出错: {e}")

if __name__ == "__main__":
    # 请确保该脚本在 docs 目录的同级目录下运行，或修改路径
    target_directory = './docs' 
    if os.path.exists(target_directory):
        process_notebooks(target_directory)
    else:
        print(f"目录 {target_directory} 不存在，请检查路径。")