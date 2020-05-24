'''
app.main.py
'''
from fastapi import FastAPI
from .routers import V1

app = FastAPI(
	title="Poland Running Api",
	description=(
		"Api, which shows running events in Poland"
	),
	version="0.0",
	docs_url="/docs",
)


# ##############
# routing
# ##############
app.include_router(V1,prefix="", tags=["v1"])


