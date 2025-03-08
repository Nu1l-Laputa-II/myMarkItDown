# MyMarkItDown 使用说明

## 简介
MyMarkItDown 是一个命令行工具，用于将各种文档格式转换为 Markdown 格式。

## 安装方法
1. 克隆代码仓库
2. 安装所需依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 使用方法
使用以下命令运行程序：
```bash
python myMarkItDown.py <input-file>
```

### 参数说明
- `input-file`: 需要转换的文件路径（支持PDF、HTML或Word文档）

### 使用示例
```bash
python myMarkItDown.py test.pdf
```

## 支持的文件类型
- PDF文件 (.pdf)
- HTML文件 (.html, .htm)
- Word文件 (.doc, .docx)
- 后续会更新其他主流文件

## 错误处理
程序会针对以下情况显示相应的错误提示：
- 缺少输入文件
- 文件格式无效
- 转换过程中的错误
