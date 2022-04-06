from pyrogram import Client
from pyrogram import filters
import asyncio
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
from requests import get
import os

api_id =  os.environ.get('API_ID', None)
api_hash = os.environ.get('API_HASH', None)
bot_token = os.environ.get('BOT_TOKEN', None)
coc_api_token = os.environ.get('COC_API_TOKEN', None)

headers = {
	'Accept': 'application/json',
	'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImIzYThmZDUzLTk2MTMtNGZjZi05NjQxLWY5YzI5NDQ5ZWQyYyIsImlhdCI6MTY0OTI2NzkxNywic3ViIjoiZGV2ZWxvcGVyL2ZjZmQ3ZTg1LWM4ZTgtNjc4MS00N2Y0LWFiNDg5MTcwNjAyYyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE3Ni4yMzQuOC40MiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.ZNSmJaAFEAroIixXbDzU1b714B_ONy3Jvdbj-TqC0gj0ztnMYPJOs1NAO_6_yK-yWGZ7SQ62CcNhndzBvviouQ'
}

app = Client(
    "lambdasession",
    api_id=19068625, api_hash="69c2a6d36060b1e333348ccfad6ca768", bot_token="5190654615:AAGqMxd148_h_e7e3iJFXYrb98nz_c_sqOo"
)	

@app.on_message(filters.command("start"))
async def start(client, message):
    await client.send_message(message.chat.id, f"""Hey, şu an çalışıyorum.
""", reply_markup=InlineKeyboardMarkup(
			[
            	[
                InlineKeyboardButton(
                "Sahibim",
                url="https://t.me/sergeantlambda"
                )],
                [
                InlineKeyboardButton("Github Repo", url="https://github.com/lambda-stock/Telegram-Clash-of-Clans-API-Bot")
                ]
			]))

@app.on_message(filters.command("coc"))
async def json(client, message):
	tag = message.command[1]
	response = requests.get(f"""https://api.clashofclans.com/v1/players/%23{tag}""", headers=headers)
	user_json = response.json()
	await client.send_message(message.chat.id, f"""
	𝕆𝕪𝕦𝕟𝕔𝕦: {user_json["name"]}
𝔹𝕖𝕝𝕖𝕕𝕚𝕪𝕖 𝔹𝕚𝕟𝕒𝕤𝕚: {user_json["townHallLevel"]}
𝕊𝕖𝕧𝕚𝕪𝕖: {user_json["expLevel"]}
𝕂𝕦𝕡𝕒: {user_json["trophies"]}
𝕊𝕒𝕧𝕒𝕤 𝕐𝕚𝕝𝕕𝕚𝕫𝕝𝕒𝕣𝕚: {user_json["warStars"]}
𝕂𝕒𝕫𝕒𝕟𝕚𝕝𝕒𝕟 𝕊𝕒𝕧𝕒𝕤𝕝𝕒𝕣: {user_json["attackWins"]}
𝕂𝕒𝕫𝕒𝕟𝕚𝕝𝕒𝕟 𝔻𝕖𝕗𝕒𝕟𝕤: {user_json["defenseWins"]}
""")

@app.on_message(filters.command("getmyip"))
async def json(client, message):
	ip = get("https://api.ipify.org").text
	await client.send_message(message.chat.id, f"""```{ip}```""")
	
app.run()