import openai
import pandas as pd
import time
import os

openai.api_key = "your_key"



def ask_gpt4(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": question},
                {"role": "user", "content": ""}
            ],
            temperature=1.0
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error: {e}")
        return "Error: 无法获取回答"


input_file = "your_data.tsv"
data = pd.read_csv(input_file, sep="\t")


output_file = "response.tsv"


if not os.path.exists(output_file):
    with open(output_file, "w") as f:
        f.write("\t".join(data.columns.tolist() + ["GPT回答"]) + "\n")


for index, row in data.iterrows():
    question = f"{row['题目']}"
    prompt = f"你是一名数学专家，请解答下述数学题：\n{question}\n注意：请使用思维链的方式一步步思考并回答。\n回答格式如下：最终答案为：（后跟你生成的答案）。分析如下：（后跟你的推理分析）。"


    print(f"正在处理第 {index + 1} 条问题：")
    answer = ask_gpt4(prompt)


    answer = answer.replace("\n", "\\n")




    with open(output_file, "a", encoding="utf-8") as f:
        f.write("\t".join([str(row[col]) for col in data.columns] + [answer]) + "\n")


    time.sleep(5)

print(f"所有回答已保存到文件 {output_file}")

