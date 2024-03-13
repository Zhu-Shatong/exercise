import json


def ipynb_to_md(input_filename, output_filename):
    # 读取.ipynb文件
    with open(input_filename, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    # 创建一个空的Markdown字符串
    markdown_content = ""

    # 遍历所有单元格
    for cell in notebook['cells']:
        if cell['cell_type'] == 'markdown':
            # 对于Markdown单元格，直接将内容添加到Markdown字符串中
            markdown_content += "\n".join(cell['source']) + "\n\n"
        elif cell['cell_type'] == 'code':
            # 对于代码单元格，添加Python代码块标记
            markdown_content += "```python\n" + \
                "\n".join(cell['source']) + "\n```\n\n"

    # 将Markdown内容写入输出文件
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(markdown_content)


# 使用函数转换.ipynb到.md
input_filename = '2-2函数拟合.ipynb'  # 输入你的.ipynb文件路径
output_filename = 'output.md'  # 指定输出的Markdown文件名称
ipynb_to_md(input_filename, output_filename)

print(f"Converted {input_filename} to {output_filename} successfully!")
