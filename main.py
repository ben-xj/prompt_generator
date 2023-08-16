# 导入所需的模块和类
from fastapi import FastAPI
from pydantic import BaseModel
from tasks import TASKS

# 创建 FastAPI 应用实例
app = FastAPI()


# 定义输入数据的模型，继承自 pydantic 的 BaseModel
class PromptInput(BaseModel):
    task_id: int  # 任务的ID号，整数类型
    inputs: list[str]  # 输入的参数列表，每个元素是字符串类型


# 定义一个 GET 路由，用于获取所有任务
@app.get("/api/tasks")
async def get_tasks():
    return TASKS


# 定义一个 POST 路由，用于生成任务提示
@app.post("/api/generate-prompt")
async def generate_prompt(input: PromptInput):
    task = TASKS.get(input.task_id)  # 根据输入的任务ID查找对应的任务

    if not task:
        return {"error": "Invalid task ID"}  # 如果找不到对应的任务，返回错误信息

    # 使用输入的参数来格式化任务的提示模板，生成完整的提示
    prompt = task["prompt_template"].format(*input.inputs)

    # 返回生成的提示
    return {
        "prompt": prompt
    }
