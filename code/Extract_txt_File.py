import re
import json

with open('zh_test.txt', 'r', encoding='utf-8') as file:
    data = file.read()


pattern = re.compile(r'([a-d])\s+([^\n]+(?:\n[^\n]+)*?)\n\s*\n', re.DOTALL)


output_data = []


matches = pattern.findall(data)

for match in matches:
    answer = match[0]
    question = match[1].strip()


    json_obj = {
        "instruction":f"请一步步思考，输出推理过程。输出格式为：答案：（仅回答ABCD选项中的一个即可）。推理原因：（这里跟着你的推理分析）。具体问题如下：{question}",
        "input": "",
        "output": f"{answer}"
    }
    output_data.append(json_obj)

with open('LogicQA-test-1.json', 'w', encoding='utf-8') as json_file:
    json.dump(output_data, json_file, ensure_ascii=False, indent=4)

print("数据已成功保存到output.json文件。")
