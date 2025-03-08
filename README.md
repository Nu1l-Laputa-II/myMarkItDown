# 构建思路
## 功能的大致描述
鼠标右键{pdf, html, word, ...}文件，可以有转化为md(直接在本地)的功能

# 实现记录
## 版本0-简答的实现
### 功能描述
使用下述命令将文件转换为Markdown格式：
```bash
python myMarkItDown.py <input_file>
```
程序会在同目录下生成一个与输入文件同名的.md文件。

### 使用说明
1. 确保已安装必要的依赖
2. 在命令行中运行程序
3. 程序将自动在输入文件的同目录下生成转换后的markdown文件

### 支持的文件类型
- PDF文件 (.pdf)
- HTML文件 (.html, .htm)
- Word文件 (.doc, .docx)

### 项目结构
```
myMarkItDown/
├── codes/
│   └── myMarkItDown-0.py    # 主程序文件
├── docs/
│   └── usage.md             # 详细使用文档
└── README.md                # 项目说明文档
```

### 错误处理
程序会处理以下错误情况：
- Invalid command line arguments
- Input file does not exist
- File conversion errors
