# 本文件中包含了各种参数, 可以进行调整
# 其中以"#"开头的注释为说明该参数的使用方法

# 生成图片的热键, 用于 keyboard 库
# 【格式】
#    1. 单键：直接写键名，如：
#         "enter"、"space"、"esc"、"tab"、"f5"、"backspace"
#    2. 组合键：多个键用加号连接（不区分大小写），如：
#         "ctrl+s"、"ctrl+shift+g"、"alt+enter"
#    3. 连续热键（序列触发）：使用逗号分隔表示按键顺序，如：
#         "ctrl+s, ctrl+shift+s"   → 表示先按 Ctrl+S，再按 Ctrl+Shift+S
#    4. 不区分大小写：'Ctrl+S' 与 'ctrl+s' 等价。
#    5. 修饰键在前，主键在后：'ctrl+alt+p'、'shift+enter'，可同时包含多个修饰符。
#
# 【常见键名示例】
#    - 字母数字键：'a' ~ 'z'、'0' ~ '9'
#    - 功能键：'f1' ~ 'f12'
#    - 修饰键：'ctrl'、'alt'、'shift'、'windows'
#    - 控制键：'enter'、'space'、'tab'、'backspace'、'delete'、'esc'
#    - 方向键：'up'、'down'、'left'、'right'
HOTKEY= "f1"

# 全选快捷键, 此按键并不会监听, 而是会作为模拟输入
# 此值为字符串, 代表热键的键名, 格式同 HOTKEY
SELECT_ALL_HOTKEY= "ctrl+a"

# 剪切快捷键, 此按键并不会监听, 而是会作为模拟输入
# 此值为字符串, 代表热键的键名, 格式同 HOTKEY
CUT_HOTKEY= "ctrl+x"

# 黏贴快捷键, 此按键并不会监听, 而是会作为模拟输入
# 此值为字符串, 代表热键的键名, 格式同 HOTKEY
PASTE_HOTKEY= "ctrl+v"

# 发送消息快捷键, 此按键并不会监听, 而是会作为模拟输入
# 此值为字符串, 代表热键的键名, 格式同 HOTKEY
SEND_HOTKEY= "enter"

# 是否阻塞按键, 如果热键设置为阻塞模式, 则按下热键时不会将该按键传递给前台应用
# 如果生成热键和发送热键相同, 则强制阻塞, 防止误触发发送消息
# 此值为布尔值, True 或 False
BLOCK_HOTKEY= False

# 操作的间隔, 如果失效可以适当增大此数值
# 此值为数字, 单位为秒
DELAY= 0.1

# 新加入参数如下
# 字符串编辑引号内内容即可
# 布尔型则使用 True/False

# 自动粘贴文本 
AUTO_PASTE_TEXT = True
# 自动发送文本
AUTO_SEND_TEXT = True
# 梦语是否启用
USE_DREAM_NAIL = True
# 分隔符,可自定义使用其他分隔符
SEPARATOR = '！'