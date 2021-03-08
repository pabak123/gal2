import discord
from urllib.request import urlopen, Request
from captcha.image import ImageCaptcha
import os
import asyncio
from discord import Client
from bs4 import BeautifulSoup
import requests
import urllib
import urllib.request
import openpyxl
import random
import time


everyone = False
client = discord.Client()


@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game('상갈아 도움을 쳐보세요!')
    await client.change_presence(status=discord.Status.online)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="상갈아 도움"))


        

@client.event
async def on_message(message):
    global selcolor
    if message.content.startswith('상갈아 핑'):
        await message.delete()
        embed = discord.Embed(description=f"", colour=discord.Colour(0x594841))
        embed.set_author(name=f"현재 핑은 {int((client.latency * 1000))}'ms 입니다.")
        await message.channel.send(embed=embed)

    if message.content.startswith('상갈아 뮤트'):
        if message.author.guild_permissions.manage_messages:
            reason = message.content[30:]

            if reason == '':
                reason = 'None'
            else:
                pass

            await message.delete()
            await message.channel.set_permissions(message.mentions[0], read_messages=True, send_messages=False)

            embed1 = discord.Embed(title='', description=(f'**사유 : ** ``{reason}``'))
            embed1.set_author(name=f'{message.mentions[0].name} 님을 뮤트 하였습니다.',
                              icon_url=(client.get_user(int(message.mentions[0].id)).avatar_url))
            await message.channel.send(embed=embed1)

    if message.content == '상갈아 실검' or message.content == '상갈아 실시간검색어':
        url = 'http://issue.zum.com/'
        req = Request(url)
        html = urllib.request.urlopen(req)
        soup = BeautifulSoup(html, "html.parser")

        s = soup.find_all('div', {'class': 'cont'})

        rank = 1
        data = []
        for title in s:
            tt = title.find('span', {'class': 'word'}).text
            data.append(f'**{rank}**. {tt}')
            rank += 1
            if rank > 10:
                break

        dat = str(data)
        dat = dat.replace("'", "")
        dat = dat.replace(", ", "\n")
        dat = dat[1:-1]
        embed = discord.Embed(title='줌 실시간 검색어 순위', description=dat, colour=0x19CE60)
        await message.channel.send(embed=embed)

            
    if message.content.startswith('상갈아 언뮤트'):
        if message.author.guild_permissions.manage_messages:
            await message.delete()
            await message.channel.set_permissions(message.mentions[0], read_messages=True, send_messages=True)

            embed1 = discord.Embed(title='', description=(''))
            embed1.set_author(name=f'{message.mentions[0].name} 님을 언뮤트 하였습니다.',
                              icon_url=(client.get_user(int(message.mentions[0].id)).avatar_url))
            await message.channel.send(embed=embed1)

    if message.content.startswith('상갈아 일과시간표'):

        embed = discord.Embed(title="2021년 상갈중학교 일과 시간표", description="", url="", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_image(url="https://cdn.discordapp.com/attachments/808236879924297750/816158619875016704/KakaoTalk_20210302_095652516.png")
        embed.set_footer(text="Made by K.G") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.            
            
    if message.content.startswith('!청소'):
        try:
            # 메시지 관리 권한 있을시 사용가능
            if message.author.guild_permissions.manage_messages:
                amount = message.content[4:]
                await message.delete()
                await message.channel.purge(limit=int(amount))
                message = await message.channel.send(embed=discord.Embed(title='🧹 메시지 ' + str(amount) + '개 삭제됨', colour=discord.Colour.green()))
                await asyncio.sleep(2)
                await message.delete()
            else:
                await message.channel.send('``명령어 사용권한이 없습니다.``')
        except:
            pass
    
    if message.content.startswith('상갈아 시간표'):
    
        embed = discord.Embed(title="각반의 시간표를 확인하시려면 아래 이모지를 클릭해주세요!", description="✌️:1반 🤏:2반 ✋:3반 ✍️:4반 👐:5반 🤚:6반", url="http://컴시간학생.kr/", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_footer(text="시간표 업데이트는 매주 월요일마다 갱신됩니다!") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("✌️")
        await msg.add_reaction("🤏")
        await msg.add_reaction("✋")
        await msg.add_reaction("✍️")
        await msg.add_reaction("👐")
        await msg.add_reaction("🤚")

    if message.content.startswith('page1sigan'):
        await message.delete()
        embed = discord.Embed(title="3-1반 시간표", description="", url="http://컴시간학생.kr/", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_image(url="https://cdn.discordapp.com/attachments/791458709976383538/815172954802487346/e28905914108d9bd.png")
        embed.set_footer(text="✌️:1반 🤏:2반 ✋:3반 ✍️:4반 👐:5반 🤚:6반") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("🤏")
        await msg.add_reaction("✋")
        await msg.add_reaction("✍️")
        await msg.add_reaction("👐")
        await msg.add_reaction("🤚")

    if message.content.startswith('page2sigan'):
        await message.delete()
        embed = discord.Embed(title="3-2반 시간표", description="", url="http://컴시간학생.kr/", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_image(url="https://cdn.discordapp.com/attachments/791458709976383538/815173786529431584/3-2.png")
        embed.set_footer(text="✌️:1반 🤏:2반 ✋:3반 ✍️:4반 👐:5반 🤚:6반") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("✌️")
        await msg.add_reaction("✋")
        await msg.add_reaction("✍️")
        await msg.add_reaction("👐")
        await msg.add_reaction("🤚")

    if message.content.startswith('page3sigan'):
        await message.delete()
        embed = discord.Embed(title="3-3반 시간표", description="", url="http://컴시간학생.kr/", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_image(url="https://cdn.discordapp.com/attachments/791458709976383538/815174385350344704/3-3.png")
        embed.set_footer(text="✌️:1반 🤏:2반 ✋:3반 ✍️:4반 👐:5반 🤚:6반") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("✌️")
        await msg.add_reaction("🤏")
        await msg.add_reaction("✋")
        await msg.add_reaction("✍️")
        await msg.add_reaction("👐")
        await msg.add_reaction("🤚")

    if message.content.startswith('page4sigan'):
        await message.delete()
        embed = discord.Embed(title="3-4반 시간표", description="", url="http://컴시간학생.kr/", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_image(url="https://cdn.discordapp.com/attachments/791458709976383538/815173786529431584/3-2.png")
        embed.set_footer(text="✌️:1반 🤏:2반 ✋:3반 ✍️:4반 👐:5반 🤚:6반") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("✌️")
        await msg.add_reaction("🤏")
        await msg.add_reaction("✋")
        await msg.add_reaction("✍️")
        await msg.add_reaction("👐")
        await msg.add_reaction("🤚")

    if message.content.startswith('page5sigan'):
        await message.delete()
        embed = discord.Embed(title="3-5반 시간표", description="", url="http://컴시간학생.kr/", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_image(url="https://cdn.discordapp.com/attachments/791458709976383538/815852014416298015/3-5.png")
        embed.set_footer(text="✌️:1반 🤏:2반 ✋:3반 ✍️:4반 👐:5반 🤚:6반") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("✌️")
        await msg.add_reaction("🤏")
        await msg.add_reaction("✋")
        await msg.add_reaction("✍️")
        await msg.add_reaction("👐")
        await msg.add_reaction("🤚")

    if message.content.startswith('page6sigan'):
        await message.delete()
        embed = discord.Embed(title="3-6반 시간표", description="", url="http://컴시간학생.kr/", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_image(url="https://cdn.discordapp.com/attachments/791458709976383538/815853097649045535/3-6.png")
        embed.set_footer(text="✌️:1반 🤏:2반 ✋:3반 ✍️:4반 👐:5반 🤚:6반") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("✌️")
        await msg.add_reaction("🤏")
        await msg.add_reaction("✋")
        await msg.add_reaction("✍️")
        await msg.add_reaction("👐")
        await msg.add_reaction("🤚")
        
        
    if message.content.startswith("상갈아 인증"): #명령어 /인증
        a = ""
        Captcha_img = ImageCaptcha()
        for i in range(6):
            a += str(random.randint(0, 9))

        name = str(message.author) + ".png"
        Captcha_img.write(a, name)

        await message.channel.send(f"""{message.author.mention} 아래 숫자를 10초 내에 입력해주세요. """)
        await message.channel.send(file=discord.File(name))

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check) # 제한시간 10초
        except:
            await message.channel.purge(limit=3)
            chrhkEmbed = discord.Embed(title='❌ 인증실패', color=0xFF0000)
            chrhkEmbed.add_field(name='닉네임', value=message.author, inline=False)
            chrhkEmbed.add_field(name='이유', value='시간초과', inline=False)
            await message.channel.send(embed=chrhkEmbed)
            print(f'{message.author} 님이 시간초과로 인해 인증을 실패함.')
            return

        if msg.content == a:
            role = discord.utils.get(message.guild.roles, name="상갈동 인간들")
            await message.channel.purge(limit=4)
            tjdrhdEmbed = discord.Embed(title='인증성공', color=0x04FF00)
            tjdrhdEmbed.add_field(name='닉네임', value=message.author, inline=False)
            tjdrhdEmbed.add_field(name='5초후 인증역할이 부여됩니다.', value='** **', inline=False)
            tjdrhdEmbed.set_thumbnail(url=message.author.avatar_url)
            await message.channel.send(embed=tjdrhdEmbed)
            await message.author.add_roles(role)
        else:
            await message.channel.purge(limit=4)
            tlfvoEmbed = discord.Embed(title='❌ 인증실패', color=0xFF0000)
            tlfvoEmbed.add_field(name='닉네임', value=message.author, inline=False)
            tlfvoEmbed.add_field(name='이유', value='잘못된 숫자', inline=False)
            await message.channel.send(embed=tlfvoEmbed)
            print(f'{message.author} 님이 잘못된 숫자로 인해 인증을 실패함.')

    if message.content.startswith("집합"):
        await message.channel.send("네")


    if message.content.startswith("상갈아 출근"):
        try:
            # 메시지 관리 권한 있을시 사용가능
            if message.author.guild_permissions.manage_messages:
                embed = discord.Embed(color=0x80E12A)
                channel = 793347285719056404
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 출퇴근 알림', value='관리자가 출근하였습니다.')
                # embed.set_image(url="")
                await client.get_channel(int(channel)).send(embed=embed)
        except:
            pass

    if message.content.startswith('상갈아 한강온도'):
        json = requests.get('http://hangang.dkserver.wo.tc/').json()
        temp = json.get("temp") # 한강온도
        time = json.get("time") # 측정시간

        embed = discord.Embed(title='💧 한강온도', description=f'{temp}°C', colour=discord.Colour.blue())
        embed.set_footer(text=f'{time}에 측정됨')

        await message.channel.send(embed=embed)

    if message.content.startswith("상갈아 퇴근"):
        try:
            if message.author.guild_permissions.manage_messages:
                embed = discord.Embed(color=0xFF0000)
                channel = 793347285719056404
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 출퇴근 알림', value='관리자가 퇴근하였습니다.')
                # embed.set_image(url="")
                await client.get_channel(int(channel)).send(embed=embed)
        except:
            pass

    if message.content.startswith('상갈아 코로나'):
        url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        datecr = soup.find('span', {'class': 't_date'})  # 기준날짜
        # print(f'기준일: {datecr.string}')

        totalcovid = soup.select('dd.ca_value')[0].text  # 누적 확진자수
        # print(f'누적 확진자: {totalcovid} 명')

        todaytotalcovid = soup.select('p.inner_value')[0].text  # 당일 확진자수 소계
        # print(f'확진자 소계: {todaytotalcovid} 명')

        todaydomecovid = soup.select('p.inner_value')[1].text  # 당일 국내발생 확진자수
        # print(f'국내발생: {todaydomecovid} 명')

        todayforecovid = soup.select('p.inner_value')[2].text  # 당일 해외유입 확진자수
        # print(f'해외유입: {todayforecovid} 명')

        totalca = soup.select('dd.ca_value')[2].text  # 누적 격리해제
        # print(f'누적 격리해제: {totalca} 명')

        todayca = soup.select('span.txt_ntc')[0].text  # 당일 격리해제
        # print(f'격리해제: {todayca} 명')

        totalcaing = soup.select('dd.ca_value')[4].text  # 누적 격리중
        # print(f'누적 격리중: {totalcaing}')

        todaycaing = soup.select('span.txt_ntc')[1].text  # 당일 격리중
        # print(f'격리중: {todaycaing} 명')

        totaldead = soup.select('dd.ca_value')[6].text  # 누적 사망자
        # print(f'누적 사망자: {totaldead} 명')

        todaydead = soup.select('span.txt_ntc')[2].text  # 당일 사망자
        # print(f'사망자: {todaydead} 명')

        covidembed = discord.Embed(title='코로나19 국내 발생현황', description="", color=0xFF0F13, url='http://ncov.mohw.go.kr/')
        covidembed.add_field(name='🦠 확진환자', value=f'{totalcovid}({todaytotalcovid}) 명'
                                                   f'\n\n국내발생: {todaydomecovid} 명\n해외유입: {todayforecovid} 명',
                             inline=False)
        covidembed.add_field(name='😷 격리중', value=f'{totalcaing}({todaycaing}) 명', inline=False)
        covidembed.add_field(name='🆓 격리해제', value=f'{totalca}({todayca}) 명', inline=False)
        covidembed.add_field(name='💀 사망자', value=f'{totaldead}({todaydead}) 명', inline=False)
        covidembed.set_footer(text=datecr.string)
        await message.channel.send(embed=covidembed)

    if message.content.startswith('상갈아 청소'):
        try:
            # 메시지 관리 권한 있을시 사용가능
            if message.author.guild_permissions.manage_messages:
                amount = message.content[4:]
                await message.delete()
                await message.channel.purge(limit=int(amount))
                message = await message.channel.send(embed=discord.Embed(title='🧹 메시지 ' + str(amount) + '개 삭제됨', colour=discord.Colour.green()))
                await asyncio.sleep(2)
                await message.delete()
            else:
                await message.channel.send('``명령어 사용권한이 없습니다.``')
        except:
            pass
    
    if message.content.startswith('상갈아 실검'):
        json = requests.get('https://www.naver.com/srchrank?frm=main').json()
        ranks = json.get("data")
        data = []
        for r in ranks:
            rank = r.get("rank")
            keyword = r.get("keyword")
            if rank > 10:
                break
            data.append(f'**{rank}**위 {keyword}')

        dat = str(data)
        dat = dat.replace("'","")
        dat = dat.replace(", ","\n")
        dat = dat[1:-1]
        print(dat)
        embed = discord.Embed(title= '네이버 실시간 검색어 순위', description=(dat),colour=0x19CE60)
        await message.channel.send(embed=embed)
    
    if message.content.startswith('상갈아 도움'):
        embed = discord.Embed(title="상갈이의 명령어", description="상갈이에 대해 더 잘 알고 싶다고요? 아래 내용을 잘봐보세요!", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name="상갈아 코로나", value="현재 코로나의 상태를 실시간으로 정보를 받아서 보여줘요!", inline=True)
        embed.add_field(name="상갈아 실검", value="사이트 네이버에서 실검 정보를 받아와 직접 보여줘요!", inline=True)
        embed.add_field(name="상갈아 한강온도", value="한강온도를 직접 재 줘요! 혹시.. 자살하시려는 건 아니죠?", inline=True)
        embed.add_field(name="상갈아배워", value="띄어쓰기를 하지않고 붙여서 써주세요! 그래야 상갈이가 배운답니다!", inline=True)
        embed.add_field(name="상갈아 핑", value="현재 당신이 사용중인 Discord API 서버와의 연결 대기시간을 보여줘요!", inline=True)
        embed.add_field(name="상갈아 n반", value="월요일날 시간표를 보여줘요! 보통 변경될일이 있으면 알아서 바꿔요!", inline=True)
        embed.add_field(name="상갈아 인물", value="**상갈이 2021 신기능** | 애들에 TMI를 알려드려요! ", inline=True)
        embed.set_footer(text="상갈") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.

    if message.content.startswith('상갈아 인물'):
        embed = discord.Embed(title="상갈이 준비중", description="상갈이가 본 명령어를 준비중이에요! 기다리세요", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_footer(text="상갈") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.

    if message.content.startswith('상갈아 2반'):
        embed = discord.Embed(title="상갈이 준비중", description="상갈이가 본 명령어를 준비중이에요! 기다리세요", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_footer(text="상갈") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.

    if message.content.startswith('상갈아 3반'):
        embed = discord.Embed(title="상갈이 준비중", description="상갈이가 본 명령어를 준비중이에요! 기다리세요", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_footer(text="상갈") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.

    if message.content.startswith('상갈아 4반'):
        embed = discord.Embed(title="상갈이 준비중", description="상갈이가 본 명령어를 준비중이에요! 기다리세요", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_footer(text="상갈") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.

    if message.content.startswith('상갈아 5반'):
        embed = discord.Embed(title="상갈이 준비중", description="상갈이가 본 명령어를 준비중이에요! 기다리세요", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_footer(text="상갈") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.

    if message.content.startswith('상갈아 6반'):
        embed = discord.Embed(title="상갈이 준비중", description="상갈이가 본 명령어를 준비중이에요! 기다리세요", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_footer(text="상갈") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.

    if message.content.startswith('상갈아 줌주소 1반'):
        embed = discord.Embed(title="상갈이가 알려주는 줌주소", description="줌을 보다 편히 입장하세요!", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name="조회/종례", value="https://us02web.zoom.us/j/85772423415?pwd=R0srQy9STmJWaHZNOWtsMkxFS3N5QT09", inline=True)
        embed.add_field(name="수학", value="https://us02web.zoom.us/j/88915247038?pwd=cXgyQlN2ZHQwWGsydm95b21VY0tKdz09", inline=True)
        embed.add_field(name="과학", value="https://zoom.us/j/5136450756?pwd=QmIrTldmTTRJMHZITWJEWU9ieE1QZz099", inline=True)
        embed.add_field(name="국어(김윤정t)", value="https://zoom.us/j/92498370772?pwd=eWdCUVBCblU1ejBzMGRzd1h6UmFyUT09", inline=True)
        embed.add_field(name="기가", value="https://zoom.us/j/3604918739?pwd=QTduMEkxckxoOFV1VGU1Z3NVUFBWQT09", inline=True)
        embed.add_field(name="도덕", value="https://us02web.zoom.us/j/88390726789?pwd=NDliUU1PK1ArbkFPYjF5ZmY5cDJUdz09#success", inline=True)
        embed.add_field(name="중국어", value="https://us02web.zoom.us/j/86959104812?pwd=QVU1clhyZVppWjlpdS9XQzhMdjYyZz09", inline=True)
        embed.add_field(name="역사", value="https://zoom.us/j/5993983414?pwd=SWxpYlJMUzZiWVhEN0o4bXVoRkllUT09", inline=True)
        embed.set_footer(text="상갈") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.

    if message.content.startswith('상갈아 시간표 1반'):
        embed = discord.Embed(title="상갈이의 시간표", description="상갈이가 1반의 시간표를 알려줘요!", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_image(url="https://cdn.discordapp.com/attachments/791458709976383538/795478429700194304/d7c3bf8990642e61.png")
        embed.set_footer(text="상갈") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.

    if message.content.startswith('!인증안내'):
        await message.delete()
        embed = discord.Embed(title="입장하는 방법", description="`상갈아 인증`을 입력하여 입장을 하세요", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_footer(text="상갈") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.

    if message.content.startswith('!노래공유안내'):
        await message.delete()
        embed = discord.Embed(title="노래 공유", description="본 채널은 자기가 추천하고 싶은 좋은 노래들을 공유하는 곳입니다.", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name="예시", value="BewhY-너에게", inline=True)
        embed.add_field(name="플랫폼", value="스포티파이 플레이리스트 링크, 유튜브 플레이리스트 링크, 스포티파이 음악 링크, 유튜브 영상 링크, 멜론, 지니뮤직등 모든 것을 지원합니다.", inline=True)
        embed.set_footer(text="상갈") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.

    if message.guild is None:
        if message.author.bot:
            return
        else:
            embed = discord.Embed(colour=discord.Colour.blue(), timestamp=message.created_at)
            embed.add_field(name='전송자', value=message.author, inline=False)
            embed.add_field(name='내용', value=message.content, inline=False)
            embed.set_footer(text=f'상갈아 디엠 <@{message.author.id}> [할말] 을 통해 답장을 보내주세요!')
            await client.get_channel(795826820318101594).send(f"`{message.author.name}({message.author.id})`", embed=embed)

    if message.content.startswith('상갈아 디엠'):
        if message.author.guild_permissions.manage_messages:
            msg = message.content[26:]
            await message.mentions[0].send(f"**{message.author.name}** 님의 답장: {msg}")
            await message.channel.send(f'`{message.mentions[0]}`에게 DM을 보냈습니다')
        else:
            return

    if message.content.startswith('상갈아 강건'):
        
        embed = discord.Embed(title="상갈위키 인물백과 '강건'", description="Namuwiki의 지원을 받아 제작되었습니다.", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name="개요", value="상갈봇 개발자다, 상갈 디스코드 아이들을 총책임하고있으며 그렇지 못한 모습도 가끔 보여준다, 가끔 미친 짓을 많이한다. 상갈 서버를 공개서버로 전환시킨다든지.. 등등", inline=True)
        embed.add_field(name="활동한 작품", value="2016 건닝맨, 2017 건닝맨, 2018 건닝맨", inline=True)
        embed.add_field(name="건닝맨", value="강건이 직접 편집하고 만든 예능이다. 상상으로 만들어서 더 화제가 된 예능. 그만큼 사건사고도 많아서 폐지됬다.", inline=True)
        embed.add_field(name="사건사고", value="1.초등학교 무단 조퇴사건, 2. 초등학교 선생님 학대논란", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/739378453895315507/806431235009675264/dad2075cf4e775fb.png")
        embed.set_footer(text="1️⃣:1번 페이지, 2️⃣:2번 페이지, 3️⃣:3번 페이지 • 1/3 페이지") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed)
        await msg.add_reaction("2️⃣")
        await msg.add_reaction("3️⃣")
        await msg.add_reaction("❌")
    
    if message.content.startswith('pageganggeonnamupage1'):
        await message.delete()
        embed = discord.Embed(title="상갈위키 인물백과 '강건'", description="Namuwiki의 지원을 받아 제작되었습니다.", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name="개요", value="상갈봇 개발자다", inline=True)
        embed.add_field(name="활동한 작품", value="2016 건닝맨, 2017 건닝맨, 2018 건닝맨", inline=True)
        embed.add_field(name="건닝맨", value="강건이 직접 편집하고 만든 예능이다. 상상으로 만들어서 더 화제가 된 예능. 그만큼 사건사고도 많아서 폐지됬다.", inline=True)
        embed.add_field(name="사건사고", value="1.학교무단조퇴사건, 2. 초등학교 선생님 학대논란, 3. 건닝맨 종영문제", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/739378453895315507/806431235009675264/dad2075cf4e775fb.png")
        embed.set_footer(text="1️⃣:1번 페이지, 2️⃣:2번 페이지, 3️⃣:3번 페이지 • 1/3 페이지") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed)
        await msg.add_reaction("2️⃣")
        await msg.add_reaction("3️⃣")
        await msg.add_reaction("❌")

    if message.content.startswith('pageganggeonnamupage2'):
        await message.delete()
        embed = discord.Embed(title="상갈위키 강건 사건파일 1번 : 학교 무단조퇴사건", description="Namuwiki의 지원을 받아 제작되었습니다.", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name="학교 무단조퇴사건", value="2016 건닝맨에서 학교에서 연을 만드는 장면에서 건이와 일부아이들은 연을 마저 제작하지 못했는데", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/791458709976383538/805038378919264286/dasdasdassda.png")
        embed.set_footer(text="1️⃣:1번 페이지, 2️⃣:2번 페이지, 3️⃣:3번 페이지 • 2/3 페이지") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("3️⃣")
        await msg.add_reaction("❌")
    
    if message.content.startswith('pageganggeonnamupage3'):
        await message.delete()
        embed = discord.Embed(title="상갈위키 강건 사건파일 2번 : 초등학교 선생님 학대논란", description="Namuwiki의 지원을 받아 제작되었습니다.", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name="초등학교 선생님 학대논란", value="2016건닝맨에서 강건이 유독 여자애들에게만 순하게 반응한다는 게 의심스러워서 여자애들처럼 반응했는데 선생님이 단단히 화가나 혼낸 사건이다.", inline=True)
        embed.add_field(name="혼낸게 왜?", value="혼낸 건 별 문제 없지만 혼낸 방식이 **아동학대**를 가정한다는 것이기 때문이다. 이 혼내는 방식은 강건 뿐만 아니라 다른 아이들에게도 사용됬다는게 밝혀져 논란이다.", inline=True)
        embed.add_field(name="선생님은?", value="말이 크게 나온 이후로 선생님 계약기간 때문에 어쩔수 없이 반 담임 선생으로 자리를 앉히진 않고 과학 전담선생님으로 하다가 계약이 종료돼 학교를 떠났다.", inline=True)
        embed.set_footer(text="1️⃣:1번 페이지, 2️⃣:2번 페이지, 3️⃣:3번 페이지 • 3/3 페이지") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")
        await msg.add_reaction("❌")

    if message.content.startswith('상갈아 장정우'):

        embed = discord.Embed(title="인물백과 '장정우'", description="본명 : 장정우 | 출생 : 2006년 11월 19일 | 사망 : 해당없음 | 국적 : 대한민국 | 신체 : 183cm 73kg A형 | 가족관계 : 부모 및 남매 | 학력 : 상갈초등학교 졸업 후 상갈중학교에 재학 중 | 종교 : 무교 | 소속 : 장정우 크루", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name="개요", value="상갈 디스코드방의 관리자 중 한명, 생각보다 꼴을 잘받으며 웬만하면 나대면 안된다.", inline=True)
        embed.set_footer(text="다음페이지는 4️⃣:1번 페이지, 5️⃣:2번 페이지, 6️⃣:3번 페이지 • 1/4 페이지") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("5️⃣")
        await msg.add_reaction("6️⃣")
        await msg.add_reaction("7️⃣")
        await msg.add_reaction("❌")

    if message.content.startswith('pagejangnamupage1'):
        await message.delete()
        embed = discord.Embed(title="인물백과 '장정우'", description="본명 : 장정우 | 출생 : 2006년 11월 19일 | 사망 : 해당없음 | 국적 : 대한민국 | 신체 : 183cm 73kg A형 | 가족관계 : 부모 및 남매 | 학력 : 상갈초등학교 졸업 후 상갈중학교에 재학 중 | 종교 : 무교 | 소속 : 장정우 크루", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name="개요", value="상갈 디스코드방의 관리자 중 한명, 생각보다 꼴을 잘받으며 웬만하면 나대면 안된다.", inline=True)
        embed.set_footer(text="다음페이지는 4️⃣:1번 페이지, 5️⃣:2번 페이지, 6️⃣:3번 페이지 • 1/4 페이지") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("5️⃣")
        await msg.add_reaction("6️⃣")
        await msg.add_reaction("7️⃣")
        await msg.add_reaction("❌")

    if message.content.startswith('pagejangnamupage2'):
        await message.delete()
        embed = discord.Embed(title="인물백과 '장정우'", description="Namuwiki의 지원을 받아 제작되었습니다.", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_image(url="https://cdn.discordapp.com/attachments/739378453895315507/805045114296336444/dasdsamaeslkjs.png")
        embed.set_footer(text="다음페이지는 4️⃣:1번 페이지, 5️⃣:2번 페이지, 6️⃣:3번 페이지 • 2/4 페이지") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("4️⃣")
        await msg.add_reaction("6️⃣")
        await msg.add_reaction("7️⃣")
        await msg.add_reaction("❌")

    if message.content.startswith('pagejangnamupage3'):
        await message.delete()
        embed = discord.Embed(title="인물백과 '장정우'", description="3.기타", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_image(url="https://cdn.discordapp.com/attachments/739378453895315507/805046613235728394/dwkdwjdnd.png")
        embed.set_footer(text="다음페이지는 4️⃣:1번 페이지, 5️⃣:2번 페이지, 6️⃣:3번 페이지 • 3/4 페이지") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("4️⃣")
        await msg.add_reaction("5️⃣")
        await msg.add_reaction("7️⃣")
        await msg.add_reaction("❌")

    if message.content.startswith('pagejangnamupage4'):
        await message.delete()
        embed = discord.Embed(title="인물백과 '장정우'", description="3.기타", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_image(url="https://cdn.discordapp.com/attachments/739378453895315507/805276715328077824/3-4.png")
        embed.set_footer(text="다음페이지는 4️⃣:1번 페이지, 5️⃣:2번 페이지, 6️⃣:3번 페이지 • 3/4 페이지") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("4️⃣")
        await msg.add_reaction("5️⃣")
        await msg.add_reaction("6️⃣")
        await msg.add_reaction("❌")

    if message.content.startswith('상갈아 신지호'):

        embed = discord.Embed(title="인물백과 '신지호'", description="수정은 개발자에게 DM하세요.", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name="개요", value="상갈 디스코드방의 관리자 중 한명, 생각보다 꼴을 잘받으며 웬만하면 나대면 안된다.", inline=True)
        embed.set_footer(text="다음페이지는 8️⃣:1번 페이지, 9️⃣:2번 페이지, 🔟:3번 페이지 • 3/4 페이지") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("8️⃣")
        await msg.add_reaction("9️⃣")
        await msg.add_reaction("🔟")
        await msg.add_reaction("❌")

    if message.content.startswith('상갈아 조예준'):

        embed = discord.Embed(title="인물백과 '조예준'", description="수정은 개발자에게 DM하세요.", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name="개요", value="본명 : 조예준 | 출생 : 2006년 11월 08일 | 사망 : 해당없음 | 국적 : 대한민국 | 신체 : 171cm(+15cm 예정) 67kg B형 | 가족관계 : 부모 및 남매 | 학력 : 용두초등학교 -> 청풍초등학교 -> 명지초등학교 졸업 후 제천동중학교 -> 상갈중으로 전학 후 재학중 (사고 많이쳐서 전학간거 아님)", inline=True)
        embed.set_footer(text="다음페이지는 🚺:1번 페이지, 🚻:2번 페이지, 🚼:3번 페이지 • 3/4 페이지") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("🚺")
        await msg.add_reaction("🚻")
        await msg.add_reaction("🚼")
        await msg.add_reaction("❌")

    if message.content.startswith('pagejodmopage1'):
        await message.delete()
        embed = discord.Embed(title="인물백과 '조예준'", description="수정은 개발자에게 DM하세요.", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name="개요", value="본명 : 조예준 | 출생 : 2006년 11월 08일 | 사망 : 해당없음 | 국적 : 대한민국 | 신체 : 171cm(+15cm 예정) 67kg B형 | 가족관계 : 부모 및 남매 | 학력 : 용두초등학교 -> 청풍초등학교 -> 명지초등학교 졸업 후 제천동중학교 -> 상갈중으로 전학 후 재학중 (사고 많이쳐서 전학간거 아님)", inline=True)
        embed.set_footer(text="다음페이지는 🚺:1번 페이지, 🚻:2번 페이지, 🚼:3번 페이지 • 3/4 페이지") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("🚺")
        await msg.add_reaction("🚻")
        await msg.add_reaction("🚼")
        await msg.add_reaction("❌")

    if message.content.startswith('pagejodmopage2'):
        await message.delete()

    if message.content.startswith('pagejodmopage3'):
        await message.delete()

    if message.content.startswith('상갈아 김영채'):
    
        embed = discord.Embed(title="인물백과 '김영채'", description="수정은 개발자에게 DM하세요.", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name="개요", value="말그대로 허접때기다. `쿠루쿠루쿠쿠루삥빵뽕`을 한번에 치기 귀찮아서 `ㅋㄹㅋㄹㅋㄹㅋㅋㄹㅃㅃ` 이런식으로 친다는 등, 말하는 거에 애교를 되게 많이 첨가하며 애들이 듣기 딱봐도 || 아 이새키는 좀 아니다.. || 할 정도로 답답해하는 놈이다.", inline=True)
        embed.add_field(name="신체", value="키 165cm, 사망 : 곧 정우의 손에 죽을 예정이다 | 45kg B형 | 가족관계 : 영훈이와 남매이며 생년이 같다. | 인성 : 영훈이가 불쌍해질 정도로 폭행을 많이 가한다. 맹현서는 한대만 때리는 데 김영채는 약한 주먹을 여러번 때려서 아프다고 한다.", inline=True)
        embed.add_field(name="번외", value="*영훈이가 잘 챙겨준다. 좋은 신랑감이다.*", inline=True)
        embed.add_field(name="스펙", value="오버워치 22렙, 전직 브론즈, 자칭 위도우 장인 || 실제로는 벌레다. ||, 연애경력이 말할수 없을 정도로 많은 남자가 거쳐갔다.", inline=False)
        embed.set_footer(text="김영채는 (검열)이라 나무위키를 쓸줄 모른다. • 1/1 페이지") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("❌")

    if message.content.startswith('상갈아 맹현서'):
        
        embed = discord.Embed(title="인물백과 '맹현서'", description="수정은 개발자에게 DM하세요.", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name="개요", value="잘못 태어난 인생패배자와 비슷한 인생을 걷고 있다. 공부란 공부는 드럽게 안하면서 롤이면 주구장창하는 **아딱**이다 *아이언딱*", inline=True)
        embed.add_field(name="스펙", value="롤 솔자랭 다 브론즈며 전 아이언인 감스트보다도 티어가 낮다. | 배그에서 조예준을 팀킬했다. | 남자애들에게 다구리를 쳐맞을 정도로 문제아다. ||우리아이가 달라졌어요 534회 출연했다. 하지만 이후에도 저 증상이다.||", inline=True)
        embed.set_footer(text="얘는 사건사고 쓰면 tmi같다고 안썼다. • 이거쓰는 거 자체가 tmi... • 1/1 페이지") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        msg = await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await msg.add_reaction("❌")

@client.event
async def on_reaction_add(reaction, user):
    if user.bot == 1: #봇이면 패스
        return None
    
    if str(reaction.emoji) == "1️⃣":
        await reaction.message.channel.send("pageganggeonnamupage1")
        await reaction.message.delete()

    if str(reaction.emoji) == "2️⃣":
        await reaction.message.channel.send("pageganggeonnamupage2")
        await reaction.message.delete()

    if str(reaction.emoji) == "3️⃣":
        await reaction.message.channel.send("pageganggeonnamupage3")
        await reaction.message.delete()

    if str(reaction.emoji) == "4️⃣":
        await reaction.message.channel.send("pagejangnamupage1")
        await reaction.message.delete()

    if str(reaction.emoji) == "5️⃣":
        await reaction.message.channel.send("pagejangnamupage2")
        await reaction.message.delete()

    if str(reaction.emoji) == "6️⃣":
        await reaction.message.channel.send("pagejangnamupage3")
        await reaction.message.delete()

    if str(reaction.emoji) == "7️⃣":
        await reaction.message.channel.send("pagejangnamupage4")
        await reaction.message.delete()

    if str(reaction.emoji) == "8️⃣":
        await reaction.message.channel.send("pagejihopage1")
        await reaction.message.delete()

    if str(reaction.emoji) == "9️⃣":
        await reaction.message.channel.send("pagejihopage2")
        await reaction.message.delete()

    if str(reaction.emoji) == "🔟":
        await reaction.message.channel.send("pagejihopage3")
        await reaction.message.delete()

    if str(reaction.emoji) == "🚺":
        await reaction.message.channel.send("pagejodmopage1")
        await reaction.message.delete()

    if str(reaction.emoji) == "🚻":
        await reaction.message.channel.send("pagejodmopage2")
        await reaction.message.delete()

    if str(reaction.emoji) == "🚼":
        await reaction.message.channel.send("pagejodmopage3")
        await reaction.message.delete()

    if str(reaction.emoji) == "✌️":
        await reaction.message.channel.send("page1sigan")
        await reaction.message.delete()

    if str(reaction.emoji) == "🤏":
        await reaction.message.channel.send("page2sigan")
        await reaction.message.delete()

    if str(reaction.emoji) == "✋":
        await reaction.message.channel.send("page3sigan")
        await reaction.message.delete()

    if str(reaction.emoji) == "✍️":
        await reaction.message.channel.send("page4sigan")
        await reaction.message.delete()

    if str(reaction.emoji) == "👐":
        await reaction.message.channel.send("page5sigan")
        await reaction.message.delete()

    if str(reaction.emoji) == "🤚":
        await reaction.message.channel.send("page6sigan")
        await reaction.message.delete()
        
    if str(reaction.emoji) == "❌":
        await reaction.message.delete()

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
