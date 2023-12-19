import os
import openai


def call_openai_chat_completion(prompt):
    # Set up OpenAI API credentials
    

    # Define the completion parameters
    completion_parameters = {
        'model': 'gpt-4',
        'messages':prompt
    }

    # Call the OpenAI Chat Completion endpoint
    response = openai.chat.completions.create(**completion_parameters)

    # Extract the generated completion from the response
    completion = response.choices[0].message.content.strip()

    return completion

file_path = './A-cross/A-cross_04_SIRT.cpp'
with open(file_path, 'r') as file:
    file_content = file.read()
    print(file_content)

# messages=[
#     {"role": "system", "content": "You are an assistant designed to insert a bug into a given code, following a statement."},
#     {"role": "user", "content": file_content},
#     {"role": "user", "content": "Delete if, else, else if, for or while"},
# ]
# messages=[
#     {"role": "system", "content": "You are an assistant designed to insert one bug into a given code, following a statement."},
#     {"role": "user", "content": file_content},
#     # {"role": "user", "content": "Delete one if, else, else if, for or while"},
#     {"role": "user", "content": "Insert one if, else, else if, for or while"},
# ]
# messages=[
#     {"role": "system", "content": "You are an assistant designed to insert one bug into a given code, following a statement. Return just the new version of the program code, without any other statement. The programming language is cpp."},
#     {"role": "user", "content": file_content},
#     # {"role": "user", "content": "Delete one if, else, else if, for or while"},
#     {"role": "user", "content": "Insert one if, else, else if, for or while"},
# ]
messages=[
    {"role": "system", "content": "You are an assistant designed to insert one bug into a given code, following a statement. Return just the new version of the program code, without any other statement. The programming language is cpp."},
    {"role": "user", "content": file_content},
    # {"role": "user", "content": "Delete one if, else, else if, for or while"},
    # {"role": "user", "content": "Replace one if, else, else if, for or while"},
    {"role": "user", "content": "Insert return"},
]

print(call_openai_chat_completion(messages))

# # Traverse through all directories and files
# for root, dirs, files in os.walk('.'):
#     for file in files:
#         file_path = os.path.join(root, file)
#         call_openai_chat_completion(file_path)
