TASKS = {
    1: {
        "id": 1,
        "name": "Summarize",
        "description": "Summarize the given text",
        "num_inputs": 1,
        "input_info": ["your text here"],
        "prompt_template": "Please provide a concise summary of the following text: {}"
    },
    2: {
        "id": 2,
        "name": "Translate",
        "description": "Translate the given text to some language",
        "num_inputs": 2,
        "input_info": ["target language", "your text here"],
        "prompt_template": "Please translate this text to {}: {}"
    },
    3: {
        "id": 3,
        "name": "Explain Code",
        "description": "Explain a piece of code",
        "num_inputs": 2,
        "input_info": ["language", "code"],
        "prompt_template": """I have some {} code that I need help understanding. Could you please explain what the following code does in simple terms?:
                ```{}```
            Please explain each line of code and what it is doing in plain chinese that is easy for me to understand. Focus on explaining the overall logic and flow of the code rather than just describing each line syntactically."""
    },
    4: {
        "id": 4,
        "name": "Add Comments to Code",
        "description": "Add comments to code",
        "num_inputs": 2,
        "input_info": ["language", "code"],
        "prompt_template": """请帮我为下面的{}代码添加注释。
        ```{}```.尽可能详细地解释每一段代码的功能和作用,以及关键变量、函数等的含义。添加的注释应该完全符合最新的代码规范，"""
    }
}
