from typing import Literal

from pydantic import BaseModel, Field


class InputModel(BaseModel):
    word: str = Field(
        alias='Lyrics',
        description='응원가에 들어갈 가사를 입력하세요',
        default='',
    )
    Style: Literal[
        '중독성 있는',
        '신나는',
        '벅찬',
        '웅장한',   
    ] = Field(
        default='중독성 있는',
    )
    llm_type: Literal['chatgpt', 'huggingface'] = Field(
        alias='Large Language Model Type',
        description='사용할 LLM 종류',
        default='huggingface',
    )

class OutputModel(BaseModel):
    output: str= Field(
        description='응원가',
    )
