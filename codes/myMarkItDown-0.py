"""
MyMarkItDown - 文件转Markdown转换器

本脚本用于将各种格式的文件（PDF、HTML、Word）转换为Markdown格式。
使用方法: python myMarkItDown.py <input_file>
"""

import sys
import os
from markitdown import MarkItDown

def main():
    """
    主函数：处理文件转换流程
    包括：参数验证、文件处理和错误处理
    """
    # 验证命令行参数
    if len(sys.argv) != 2:
        print("Usage: python myMarkItDown.py <input_file>")
        sys.exit(1)

    # 检查输入文件是否存在
    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        sys.exit(1)

    try:
        # 初始化转换器并处理文件
        converter = MarkItDown()
        result = converter.convert(input_file)
        
        # 生成输出文件名并保存
        output_file = os.path.splitext(input_file)[0] + ".md"
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(result.text_content)
        print(f"Successfully converted '{input_file}' to '{output_file}'")
    
    except ValueError as error:
        print(f"Error: {str(error)}")
        sys.exit(1)
    except Exception as error:
        print(f"Unexpected error: {str(error)}")
        sys.exit(1)

if __name__ == "__main__":
    main()