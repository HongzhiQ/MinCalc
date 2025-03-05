import pandas as pd
import json


data = pd.read_excel('all_data.xlsx')

result = []


for index, row in data.iterrows():
    item = {
        "instruction": f"请你解答下述数学题：{row['题目']}。输出格式为：答案为：后跟答案。解答过程为：后跟你的推理过程。",
        "input": "",
        "output": f"答案为：{row['答案']}。解答过程为：{row['答题过程']}"
    }
    result.append(item)


output_file = 'all_data.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

print(f"The file is saved as {output_file}")
