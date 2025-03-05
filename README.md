# MinCalc
The data and code for the paper: Small data sets, big breakthroughs: AI can also win the primary school Math Olympiad gold medal

It contains:

* **datasets**: Primary School Math Olympiad Dataset, Split into Training, Testing, and Validation Sets.
* **Code**:
   * **`Call_GPT-4_API.py`**: Testing the GPT-4 Model via API Calls.
   * **`Convert_Data_Format.py`**: Convert the Dataset into JSON Format.
   * **`Extract_txt_File.py`**: Extract Text from TXT and Convert to JSON Format. This Code Facilitates the Conversion of the LogicQA Dataset.
   * **`Split_Data.py`**: Split the data.
   * **`LLM Fine tune`**: The training and inference of LLM are based on the LLaMA Factory [5] framework ([link](https://github.com/hiyouga/LLaMA-Factory/tree/main)). We publish details of our training here: We employed LoRA for parameter-effcient tuning. We set the batch size to 8, thenumber of epochs to 5, the learning rate to 1e-5.maximum text length of 1500 tokens, and testedthe model that performed best on the validation set.


### Requirement

| Mandatory  | Recommend  |
|------|------|
| python  | 3.10  |
| torch  | 2.4.0  |
| transformers  | 4.49.0  |
| datasets  | 3.2.0  |
| accelerate  | 1.2.1  |
| peft  | 0.12.0 |
| trl  | 0.9.6  |
| tqdm | 4.66.4  |
| pandas |  2.0.3 |
| scikit-learn | 1.3.2  |

