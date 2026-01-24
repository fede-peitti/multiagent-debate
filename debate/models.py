import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def load_model(model_name, quantize=False):
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    if quantize:
        model = AutoModelForCausalLM.from_pretrained(
            model_name, load_in_8bit=True, device_map="auto"
        )
    else:
        model = AutoModelForCausalLM.from_pretrained(
            model_name, torch_dtype=torch.float16, device_map="auto"
        )

    model.eval()
    return tokenizer, model
