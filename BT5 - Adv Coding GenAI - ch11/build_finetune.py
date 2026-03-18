from openai import OpenAI

client = OpenAI()

MODEL = "gpt-4o-mini-2024-07-18"

# 1. Upload file
upload = client.files.create(
    file=open("fine_tuning.jsonl", "rb"),
    purpose="fine-tune"
)

file_id = upload.id
print("Uploaded file:", file_id)

# 2. Tạo job fine-tune
job = client.fine_tuning.jobs.create(
    training_file=file_id,
    model=MODEL
)

print("Job ID:", job.id)

# 3. Sau khi train xong -> dùng model
response = client.chat.completions.create(
    model='ft:gpt-4o-2024-08-06:pazpaz-the-coder::AsQxSdQL',
    messages=[
        {
            "role": "user",
            "content": "Write a Python function that finds the maximum value in a list. Return code only."
        }
    ]
)

print(response.choices[0].message.content)