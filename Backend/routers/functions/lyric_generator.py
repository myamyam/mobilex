import os

from fastapi import APIRouter

from llm.chat import build
from llm.store import LLMStore
from models.lyric_generator import InputModel, OutputModel

# Configure API router
router = APIRouter(
    tags=['functions'],
)

# Configure metadata
NAME = os.path.basename(__file__)[:-3]

# Configure resources
store = LLMStore()

###############################################
#                   Actions                   #
###############################################


@router.post(f'/func/{NAME}')
async def call_lyric_generator(model: InputModel) -> OutputModel:
    # Create a LLM chain
    chain = build(
        name=NAME,
        llm=store.get(model.llm_type),
    )
    input=f'''
        #About Player
        *Player name: {model.player_name}
        *Team name: {model.team_name}
        *Play style: {model.play_style}
        '''
    output=chain.invoke({
        'input_context': input,
    })
    
    return OutputModel(
        output=output,
    )
