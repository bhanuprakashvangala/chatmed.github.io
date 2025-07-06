import torch
from transformers import BioGptForCausalLM, BioGptTokenizer

class ChatMedBot:
    def __init__(self):
        self.tokenizer = BioGptTokenizer.from_pretrained("microsoft/biogpt")
        self.model = BioGptForCausalLM.from_pretrained("microsoft/biogpt")

    def get_response(self, user_input):
        inputs = self.tokenizer.encode(user_input + " </s>", return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=100, num_return_sequences=1)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
