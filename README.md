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
> Descargar Java 17+ (en el caso de este proyecto, 21). <a target="_blank" href="https://www.oracle.com/es/java/technologies/downloads/">Enlace para la descarga.</a> Para comprobar si está instalado correctamente puedes ejecutar java --version en tu terminal<br>
> Descargar el .jar de Lavalink. Accede a <a target="_blank" href="https://github.com/lavalink-devs/Lavalink/releases">Releases</a> y descarga el .jar (está en assets). Importante, añade ese .jar al directorio donde descargues este proyecto.<br>
> Copia el <a target="_blank" href="https://github.com/lavalink-devs/Lavalink/">application.yml de ejemplo de Lavalink</a> y añádelo al directorio del bot. Configúralo a tu gusto (recomendación: cambia la password y cámbiala, no es necesario si ejecutas en localhost pero igualmente es un segundo, no hace daño y es un extra de seguridad.<br><br>
> Dependencias de python:<br>
> pip install python-decouple<br>
> pip install requests<br>
> py -3 -m pip install -U discord.py<br><br>
> Finalmente crear un .env y añadir en una línea BOT_TOKEN='<-Tu token va aqui->' y en otra PASSWORD='<-Contraseña en tu application.yml (si no modificaste el archivo: youshallnotpass->'

> [!TIP]
> Para obtener una lista completa en tu servidor usa -help<br><br>
> SECCIÓN DE MÚSICA:<br>
> aleatorio     Modo aleatorio para las canciones que hay en la cola<br>
> borrar        Borro la canción con índice indicado. Consulta el número con ºcola.<br>
> cola [numero] Lista de las siguientes canciones.<br>
> nightcore     Activa/desactiva filtro nightcore.<br>
> p [cancion]   Reproduzco la canción que me pidas.<br>
> pausa         Pausar o reproducir la música (cambia el estado en el que esté).<br>
> saltar        Para la canción actual.<br>
> vete          Desconecta al usuario.<br><br>
> SECCIÓN DE COMANDOS DE TEXTO<br>
> hola          Te saludo<br>
> tula          Te digo cuánto te mide la tula hoy<br>
> sabiduria     Te doy la motivación que necesitas hoy<br>
> disney        Te enseño qué personaje de Disney eres hoy<br>
> valorant      Te enseño qué personaje de Valorant eres hoy<br>
> rick          Te enseño qué personaje de Rick y Morty eres hoy<br>
> mtg           Te enseño qué carta de MTG eres hoy<br>