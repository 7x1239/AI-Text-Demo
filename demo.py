import sys
import io
# 加上这两行，强制解决刚才那个 Unicode 编码报错的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from zhipuai import ZhipuAI

# 1. 把下面这行引号里的内容，替换成你微信里存的那个真正的 cad 开头的密钥！
client = ZhipuAI(api_key="我的真实密钥已隐藏") 

# 2. 发送请求
response = client.chat.completions.create(
    model="glm-4-flash",
    messages=[
        {"role": "user", "content": "你好，我是广东培正学院人工智能专业的大一学生，我正在准备职业规划大赛，请给我一句鼓励的话。"}
    ]
)

# 3. 打印结果
print("----- AI回复如下 -----")
print(response.choices[0].message.content)