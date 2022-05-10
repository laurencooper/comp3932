from molotov import scenario


_API = "http://34.105.139.200"



@scenario(weight=100)
async def scenario_two(session):
    async with session.get(_API) as resp:
        assert resp.status == 200, resp.status