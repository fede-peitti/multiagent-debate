import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from config.models import MODELS


def load_model(model_key: str):
    assert model_key in MODELS, f"Unknown model key: {model_key}"

    model_id = MODELS[model_key]["hf_id"]

    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id, dtype=torch.float32, device_map="auto"  # M1 config
    )

    model.eval()
    return tokenizer, model
