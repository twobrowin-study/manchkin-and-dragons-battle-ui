import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

from sqlalchemy import select, update

from loguru import logger

from provider import Provider
from db_model import FightToUi

provider = Provider()

app = FastAPI()

app.mount('/static', StaticFiles(directory='src/static'))

@app.get('/horde')
async def horde(request: Request) -> JSONResponse:
    async with provider.db_session() as session:
        fight_to_ui_sel = await session.execute(select(FightToUi))
        fight_to_ui = fight_to_ui_sel.scalar_one()

        responce = JSONResponse({
            'horde_name':         fight_to_ui.horde_name         if fight_to_ui.horde_name         is not None else '',
            'horde_level':        fight_to_ui.horde_level        if fight_to_ui.horde_level        is not None else '',
            'horde_health':       fight_to_ui.horde_health       if fight_to_ui.horde_health       is not None else '',
            'horde_constitution': fight_to_ui.horde_constitution if fight_to_ui.horde_constitution is not None else '',
            'horde_strength':     fight_to_ui.horde_strength     if fight_to_ui.horde_strength     is not None else '',
            'horde_dexterity':    fight_to_ui.horde_dexterity    if fight_to_ui.horde_dexterity    is not None else '',
            'horde_wisdom':       fight_to_ui.horde_wisdom       if fight_to_ui.horde_wisdom       is not None else '',
            'horde_bi':           fight_to_ui.horde_bi,
            'horde_color':        fight_to_ui.horde_color,
        })

        await session.execute(update(FightToUi).values(horde_bi=None, horde_color=None))

        await session.commit()

        return responce

@app.get('/alliance')
async def alliance(request: Request) -> JSONResponse:
    async with provider.db_session() as session:
        fight_to_ui_sel = await session.execute(select(FightToUi))
        fight_to_ui = fight_to_ui_sel.scalar_one()

        responce = JSONResponse({
            'alliance_name':         fight_to_ui.alliance_name         if fight_to_ui.alliance_name         is not None else '',
            'alliance_level':        fight_to_ui.alliance_level        if fight_to_ui.alliance_level        is not None else '',
            'alliance_health':       fight_to_ui.alliance_health       if fight_to_ui.alliance_health       is not None else '',
            'alliance_constitution': fight_to_ui.alliance_constitution if fight_to_ui.alliance_constitution is not None else '',
            'alliance_strength':     fight_to_ui.alliance_strength     if fight_to_ui.alliance_strength     is not None else '',
            'alliance_dexterity':    fight_to_ui.alliance_dexterity    if fight_to_ui.alliance_dexterity    is not None else '',
            'alliance_wisdom':       fight_to_ui.alliance_wisdom       if fight_to_ui.alliance_wisdom       is not None else '',
            'alliance_bi':           fight_to_ui.alliance_bi,
            'alliance_color':        fight_to_ui.alliance_color,
        })

        await session.execute(update(FightToUi).values(alliance_bi=None, alliance_color=None))

        await session.commit()

        return responce

if __name__ == '__main__':
    logger.info('Starting now...')
    try:
        uvicorn.run(
            app        = 'main:app',
            host       = '0.0.0.0',
            port       = 8080,
            reload     = False,
            log_config = f'src/log_conf.yaml'
        )
    except (KeyboardInterrupt, SystemExit):
        logger.info('Done! Have a great day!')