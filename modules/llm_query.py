from llama_cpp import Llama

llm = Llama(model_path="./models/llama-pro-8b-instruct.Q4_K_M.gguf", n_ctx=2048)

def get_command_from_llm(text):
    prompt = f"You are a helpful assistant. Convert the following user request into a bash command:\n\n{text}\n\nCommand:"
    result = llm(prompt, max_tokens=100)
    return result["choices"][0]["text"].strip()
