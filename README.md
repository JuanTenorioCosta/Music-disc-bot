# Music-disc-bot
 Bot de música para Discord (Lavalink + Wavelink)

> [!IMPORTANT]
> Para ejecutar:<br>
> Primero iniciar el servidor: <br>
> java -jar Lavalink.jar <br>
> Una vez el servidor está iniciado: <br>
> py -3 main.py

> [!WARNING]
> Dependencias: <br>
> <a target="_blank" href="https://github.com/PythonistaGuild/Wavelink?tab=readme-ov-file#installation">Página de Wavelink de GitHub </a> Seguir instrucciones del install en función de tu S.O.<br>
> Descargar Java 17+ (en el caso de este proyecto, 21). Enlace: <a target="_blank" href="https://www.oracle.com/es/java/technologies/downloads/"></a> Para comprobar si está instalado correctamente puedes ejecutar java --version en tu terminal<br>
> Descargar el .jar de Lavalink. Accede a <a target="_blank" href="https://github.com/lavalink-devs/Lavalink/releases">Releases</a> y descarga el .jar (está en assets). Importante, añade ese .jar al directorio donde descargues este proyecto.<br>
> Copia el <a target="_blank" href="https://github.com/lavalink-devs/Lavalink/">application.yml de ejemplo de Lavalink</a>. Configúralo a tu gusto.<br><br>
> Dependencias de python:<br>
> pip install python-decouple<br>
> pip install requests<br>
> py -3 -m pip install -U discord.py<br><br>
> Finalmente crear un .env y añadir en una línea BOT_TOKEN='<-Tu token va aqui->' y en otra PASSWORD='<-Contraseña de tu application.yml (si usaste la de ejemplo: youshallnotpass->'

> [!TIP]
> Comandos de texto usando º al principio:<br>
> play <-cancion->: Reproduce la canción que le indiques<br>
> skip: Salta la canción actual<br>
> nightcore: Activa el modo nightcore para la canción actual. Lo puedes desactivar volviendo a introducir el mismo comando.<br>
> pausa | dale: Sirven para pausar y reproducir la canción.<br>
> vete | dc: El bot se desconecta.<br>
> comandos | ayuda: El bot devuelve un mensaje explicando los comandos disponibles