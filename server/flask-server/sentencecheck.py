from RunOnce.perplexitymodel import GPT2PPL
model = GPT2PPL(device="cpu")

print("Please enter your sentence: (Press Enter twice to start processing)")
contents = []
while True:
    line = input()
    if len(line) == 0:
        break
    contents.append(line)
sentence = "\n".join(contents)

model(sentence)