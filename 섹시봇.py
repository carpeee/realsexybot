import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("물렁이랑")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content == "!연애운":
        await message.channel.send(random.choice(["좃망", "그럭저럭", "성공", "거울좀 봐", "오늘부터 1일"]))
    elif message.content == "!남친":
        await message.channel.send(random.choice(["리모", "하람", '메로나', "너구리", "CU"]))
    elif message.content == "!여친":
        await message.channel.send(random.choice(["노바", "물렁이", 'CU', "너구리", "낙지", "섹시봇"]))
    elif message.content == "!오늘의운세":
        await message.channel.send(random.choice(["나쁨", "매우나쁨", '보통', "좋음", "매우좋음"]))
    elif message.content == "!경쟁전":
        await message.channel.send(random.choice(["짐", "짐", '짐', "이김", "무승부", "짐", "짐", "짐", "짐"]))
    elif message.content == "!거울":
        await message.channel.send(random.choice(["거울을 보니 오랑우탄이 있었다.", "거울을 보니 요다가 있었다.", "거울을 보니 박보검이 있었다.", "거울을 보니 은희가 있었다.", "거울을 보니 거울이 깨져버렸다.", "거울을 보니 탈모가 되어있었다."]))
    elif message.content == "!자판기":
        await message.channel.send(random.choice(["돈을 넣었더니 아무것도 나오지 않았다.", "돈을 넣었더니 변기물이 나왔다.", "돈을 넣었더니 걸레빤물이 나왔다.", "돈을 넣었더니 음료수가 나왔다.", "돈을 넣었더니 뜨거운 우유가 나왔다.", "돈을 넣었더니 델몬트 포도주스가 나왔다."]))
    elif message.content == "!게임":
        await message.channel.send(random.choice(["롤", "배그(steam)", "옵치", "배그(kakao)", "휴먼 폴 플랫", "레인보우 식스"]))
    elif message.content ==("!안녕"):
        await message.channel.send(random.choice(["조까", "꺼져"]))
    elif message.content ==("!주사위"):
        await message.channel.send(random.choice(["1", "2", "3", "4", "5", "6"]))

    elif message.content ==("!물렁이소환"):
        await message.channel.send("경쟁중이니 다이아 가면 연락합니다(평생 안옴)")
    elif message.content ==("!대리문의"):
        await message.channel.send("문화상품권 10000원 지불 후 물렁이 또는 haram에게 문의")
    elif message.content ==("!물렁한서버"):
        await message.channel.send("※물렁한 서버 서비스 종료 안내※ 2019년 11월 25일부터 개설된 물렁한 서버는 오늘 이후로 서비스가 종료됨을 알려드립니다. 방장이 개병신같은 새끼라 서버운영에 큰 어려움을 겪어 서비스 종료를 결정하게 되었습니다. 지금까지 물렁한 서버를 좆같이 여겨주신 분들께 감사의 말씀을 전하며 새로운 서버인 sex haram에서 만나뵙도록 하겠습니다. https://discord.gg/fGnrBTu")
    elif message.content ==("!시우소환"):
        await message.channel.send("공부하는 척 하는중")
    elif message.content ==("!물렁이바보"):
        await message.channel.send("정답입니다. 상금으로 세훈이의 멜로디언과 키스를 드립니다!")
    elif message.content ==("!하고싶어"):
        await message.channel.send("하앙하앙")
    elif message.content ==("!리모서버"):
        await message.channel.send("오늘은 휴일입니다(사실 항상 휴일임)")
    elif message.content ==("!요다소환"):
        await message.channel.send("씹빵새끼")
    elif message.content ==("!정숙이의말씀"):
        await message.channel.send("내말을 귓등으로도 안들으면 성범죄자가 되는거야")
    elif message.content ==("!노바소환"):
        await message.channel.send("!안뇽하세요! 옵치랑 공부빼고 다 잘하는 째훈이에용!")
    elif message.content ==("!후원"):
        await message.channel.send("섹시봇을 위해 기부해주세요ㅠㅠ 컴터가 못버텨요..!송금")
    elif message.content ==("!낙지소환"):
        await message.channel.send("일간베스트 특별회원 방성현입니다")
    elif message.content ==("!너구리소환"):
        await message.channel.send("라면 끓이는중")
    elif message.content ==("!OSIB"):
        await message.channel.send("Oh Sibal It`s Bokgui")
    elif message.content == ("!osib"):
        await message.channel.send("Oh Sibal It`s Bokgui")
    elif message.content ==("!이이잉"):
        await message.channel.send("앗살라말라이꿈")
    elif message.content ==("!섹스"):
        await message.channel.send("하앙 너무 조앙")
    elif message.content ==("!송금"):
        await message.channel.send("SC제일은행 47116134112856")
    elif message.content ==("!ㅗ"):
        await message.channel.send("조까 씨발 어머니 만수무강")
    elif message.content ==("?"):
        await message.channel.send("물음표 작작좀 ^^ -물렁이-")
    elif message.content ==("!착한유다연씨"):
        await message.channel.send("흐즈므르그 흤드!!")
    elif message.content ==("!유다연명대사"):
        await message.channel.send("여보세요? 여보세요? 아 뭐야~! 여보세요! ㅠㅠ")
    elif message.content ==("!ㅅㅂ"):
        await message.channel.send("수박")
    elif message.content ==("!시발"):
        await message.channel.send("여성의 성기를 비하하는 표현")
    elif message.content ==("!씨발"):
        await message.channel.send("여성의 성기를 비하하는 표현")
    elif message.content ==("ㅗ"):
        await message.channel.send("빠큐 ^^")
    elif message.content ==("안녕"):
        await message.channel.send("반가워")
    elif message.content ==("!물렁이"):
        await message.channel.send("이름 : 물렁이 나이 : 15세 성별 : 알 수 없음")
    elif message.content ==("!하람소환"):
        await message.channel.send("천재딜러 하람입니당")
    elif message.content ==("!섹시봇소환"):
        await message.channel.send("I`am so sexy.")
    elif message.content ==("!레꼬단"):
        await message.channel.send("https://discord.gg/R5XQ3tS")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
