EXPERIMENT_GRID = [
    # GPT-OSS-20B (English)
    {"model": "openai/gpt-oss-20b", "model_label": "EN", "agents": 1, "rounds": 1},  # 1
    {"model": "openai/gpt-oss-20b", "model_label": "EN", "agents": 1, "rounds": 2},  # 2
    {"model": "openai/gpt-oss-20b", "model_label": "EN", "agents": 1, "rounds": 5},  # 3
    {"model": "openai/gpt-oss-20b", "model_label": "EN", "agents": 2, "rounds": 1},  # 4
    {"model": "openai/gpt-oss-20b", "model_label": "EN", "agents": 2, "rounds": 2},  # 5
    {"model": "openai/gpt-oss-20b", "model_label": "EN", "agents": 2, "rounds": 5},  # 6
    {"model": "openai/gpt-oss-20b", "model_label": "EN", "agents": 5, "rounds": 1},  # 7
    {"model": "openai/gpt-oss-20b", "model_label": "EN", "agents": 5, "rounds": 2},  # 8
    {"model": "openai/gpt-oss-20b", "model_label": "EN", "agents": 5, "rounds": 5},  # 9
    # Gemma 3 (Multilingual)
    {
        "model": "google/gemma-3-27b-it",
        "model_label": "MULTI",
        "agents": 1,
        "rounds": 1,
    },
    {
        "model": "google/gemma-3-27b-it",
        "model_label": "MULTI",
        "agents": 1,
        "rounds": 2,
    },
    {
        "model": "google/gemma-3-27b-it",
        "model_label": "MULTI",
        "agents": 1,
        "rounds": 5,
    },
    {
        "model": "google/gemma-3-27b-it",
        "model_label": "MULTI",
        "agents": 2,
        "rounds": 1,
    },
    {
        "model": "google/gemma-3-27b-it",
        "model_label": "MULTI",
        "agents": 2,
        "rounds": 2,
    },
    {
        "model": "google/gemma-3-27b-it",
        "model_label": "MULTI",
        "agents": 2,
        "rounds": 5,
    },
    {
        "model": "google/gemma-3-27b-it",
        "model_label": "MULTI",
        "agents": 5,
        "rounds": 1,
    },
    {
        "model": "google/gemma-3-27b-it",
        "model_label": "MULTI",
        "agents": 5,
        "rounds": 2,
    },
    {
        "model": "google/gemma-3-27b-it",
        "model_label": "MULTI",
        "agents": 5,
        "rounds": 5,
    },
]
