from pydantic import BaseModel, Field

class HelloWorldResponse(BaseModel):
    language: str = Field(..., description="Programming language name")
    code: str = Field(..., description="Executable Hello World code")
    explanation: str = Field(..., description="Explanation of the code")
