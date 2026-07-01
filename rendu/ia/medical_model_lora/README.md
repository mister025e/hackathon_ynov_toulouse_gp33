# 🏥 Adaptateur LoRA Médical Expérimental
Ce dossier contient la configuration de l'adaptateur LoRA (PEFT) pour le modèle médical expérimental basé sur `microsoft/Phi-3.5-mini-instruct`.

## Configuration de l'adaptateur (LoRA)
* **Modèle de base** : `microsoft/Phi-3.5-mini-instruct`
* **Type PEFT** : LORA
* **Rang (r)** : 8
* **Alpha** : 16
* **Target Modules** : `qkv_proj`, `o_proj`, `gate_up_proj`, `down_proj`
* **Dropout** : 0.05
* **Type de tâche** : CAUSAL_LM

## Comment charger et utiliser ce modèle directement en Python

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

base_model_name = "microsoft/Phi-3.5-mini-instruct"
adapter_path = "./rendu/ia/medical_model_lora"

# 1. Charger le Tokenizer et le modèle de base
tokenizer = AutoTokenizer.from_pretrained(base_model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    base_model_name,
    torch_dtype=torch.float16,
    device_map="auto",
    trust_remote_code=True
)

# 2. Charger les poids de l'adaptateur LoRA médical
model = PeftModel.from_pretrained(model, adapter_path)
print("✅ Modèle médical expérimental avec adaptateur LoRA chargé !")
```
