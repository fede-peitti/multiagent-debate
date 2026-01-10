from models.loader import load_model
import torch

MODEL_KEY = "bloomz_1b7_multi"

tokenizer, model = load_model(MODEL_KEY)

prompt = "What is 7 + 5?"

inputs = tokenizer(prompt, return_tensors="pt")

device = next(model.parameters()).device
inputs = {k: v.to(device) for k, v in inputs.items()}

outputs = model.generate(**inputs, max_new_tokens=20, do_sample=False)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
