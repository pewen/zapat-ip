# Zapat-IP

**Zapat-IP** es una zapatilla eléctrica IP de software y hardware libre, para controlar artículos electrónicos (TV, aire acondicionado, luces, etc.) desde cualquier lugar.

**Área temática: Internet of Things (IoT).**

## Objetivos
* Desarrollar una primera aplicación con las placas Intel Galileo.
* Entender los conceptos básicos de [Internet of Things (IoT)](https://en.wikipedia.org/wiki/Internet_of_Things)
* Aprender!

## Características
###Software
* Linux para sistemas embebidos [Yocto Proyect](https://www.yoctoproject.org/).
* [Servidor REST (REpresentational State Transfer)](https://en.wikipedia.org/wiki/Representational_state_transfer) implementado en Python.
* Application Programming Interface (API): permite ampliar el uso de acuerdo a nuevas necesidades/ideas/proyectos de la comunidad.
* Cliente web estándar [HTML5](https://en.wikipedia.org/wiki/HTML5) y [JavaScript](https://en.wikipedia.org/wiki/JavaScript). El usuario no necesita instalar ninguna aplicación adicional en el dispositivo, se accede mediante el browser.
* Accesible desde cualquier dispositivo (PC, notebook, smart-phone, etc).
* Networking: [IPv6](https://en.wikipedia.org/wiki/IPv6)
* Certificado [SSL](https://en.wikipedia.org/wiki/Transport_Layer_Security) para conexiones seguras.
* Autenticación vía [OAuth2](https://en.wikipedia.org/wiki/OAuth)

###Hardware
* [Intel Gallileo](https://www-ssl.intel.com/content/www/us/en/do-it-yourself/galileo-maker-quark-board.html).
* Sensores de corriente y voltaje por cada enchufe.
* Banco de relees para controlar cada enchufe.
* Diseño del chasis con impresión 3D.

###Aplicaciones
* Prender y apagar individualmente cada uno de los enchufes.
* Planificar (mediante un calendario) encendidos y apagados.
* Monitorear gráficamente el consumo y el voltaje.
* Avisos mediante twitter/whatsapp de alarmas de sobre consumo y eventos configurables por el usuario.
* Uso del API para implementar fácilmente nuevas ideas/proyectos.
 

## API

|      HTTP request*    |             Acción                        |
|-----------------------|-------------------------------------------|
|  GET   /api/plugs     | Información de todos los enchufes         |
|  GET   /api/plugs/:id | Información de un enchufe particular (id) |
|  PUT   /api/plugs/:id | Cambiar el nombre del enchufe             |
|  PUT   /api/plugs/:id | Cambiar el estado (On/Off) del enchufe    |
|  POST  /api/plugs/:id | Crea una alarmar para un enchufe          |
| DELETE /api/plugs/:id | Borra una alarma                          |

*URIs relativas a http://example.com

#### Licencia
El código está licenciado bajo [MIT](https://github.com/pewen/zapat-ip/blob/master/LICENSE).

La documentación bajo

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Zapat-IP</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/pewen/zapat-ip" rel="dct:source">https://github.com/pewen/zapat-ip</a>.
