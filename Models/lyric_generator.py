from typing import Literal

from pydantic import BaseModel, Field

MAX_LENGTH = 3

class InputModel(BaseModel):
    word: str = Field(
        alias='player_name',
        description='응원가에 들어갈 선수 이름을 입력하세요',
        default='김현준',
        # min_length=MAX_LENGTH,
        # max_length=MAX_LENGTH,
        # pattern=rf'^[a-z|가-힣]{{{MAX_LENGTH}}}$',
    )
    team_name: str = Field(
        description='응원가에 들어갈 팀이름을 입력하세요',
        default='삼성',
        # min_length=MAX_LENGTH,
        # max_length=MAX_LENGTH,
        # pattern=rf'^[a-z|가-힣]{{{MAX_LENGTH}}}$',
    )
    play_style: Literal[
        '안타',
        '홈런',
        '달리기',
    ] = Field(
        default='안타',
    )
    llm_type: Literal['chatgpt', 'huggingface'] = Field(
        alias='Large Language Model Type',
        description='사용할 LLM 종류',
        default='chatgpt',
    )


class OutputModel(BaseModel):
    output: str = Field(
        description='응원가 가사',
    )
