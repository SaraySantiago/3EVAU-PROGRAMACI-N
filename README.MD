
# COMENTARIOS DE LA LECTURA



# Sinergias elegidas para dar soporte con sistemas:

- trío de comunicación web (client-server architecture, http/https, APIs)
- API moderna (rest API, graphQL, API gateways)
  
# ÁREAS CLAVE EN EL DESARROLLO DE APLICACIONES MODERNAS.

¿CÓMO PUEDEN FUNCIONAR DE MANERA CONJUNTA PARA OFRECER UNA ARQUITECTURA ROBUSTA Y ESALABLE?

1. TRÍO DE COMUNICACIÓN WEB: Es la base de la mayoría de aplicaciones web modernas y está diseñado para permitir que los clientes se comuniquen con servidores remotos a través de internet, se interrelacionan así:
   - Arquitectura cliente-servidor: Es el patrón de las aplicaciones web. El cliente (un navegador o aplicación movil) realiza solicitudes al servidor, el cual procesa la solicitud y devuelve los datos o realiza una acción específica. Esta separación facilita la escalabilidad y el mantenimiento.
   - HTTP/HTTPS: El Protocolo de Transferencia de Hipertexto (HTTP) es el método utilizado por los clientes para comunicarse con los servidores. HTTPS es la versión segura de HTTP, que cifra los datos para evitar que terceros intercepten la comunicación.
   - APIs (Interfaz de Programación de Aplicaciones): Las APIs permiten la comunicación entre diferentes sistemas. Son fundamentales para conectar el cliente con el servidor y, a menudo, las aplicaciones modernas utilizan APIs RESTful o GraphQL para manejar solicitudes y respuestas de manera eficiente. Las APIs proporcionan un punto de entrada para que los clientes obtengan datos o realicen operaciones, sin tener que conocer detalles sobre la implementación interna del servidor.

2. API MODERNA: Las APIs modernas han evolucionado significativamente para manejar las necesidades de aplicaciones más complejas y con mayores demandas de rendimiento y flexibilidad. Algunas de las principales tecnologías que mencionas incluyen:

- REST API: REST (Representational State Transfer) es un conjunto de principios arquitectónicos para crear servicios web escalables. Es la forma más común de API y funciona sobre HTTP. Una de sus grandes ventajas es su simplicidad y flexibilidad. Con REST, los clientes realizan solicitudes HTTP (GET, POST, PUT, DELETE, etc.) a URLs específicas y el servidor devuelve respuestas generalmente en formato JSON.
- GraphQL: Es una alternativa moderna a REST. En lugar de tener múltiples puntos finales (endpoints) para acceder a distintos tipos de datos, GraphQL permite a los clientes especificar exactamente qué datos necesitan, lo que reduce la cantidad de información innecesaria que se envía a través de la red. Esta flexibilidad permite a los desarrolladores crear interfaces más dinámicas y personalizadas. Aunque GraphQL tiene muchas ventajas, también tiene una mayor complejidad en la implementación y requiere un enfoque más cuidadoso para evitar sobrecargar el servidor.
- API Gateways: En aplicaciones más grandes, los API Gateways son esenciales. Un API Gateway actúa como un punto de entrada único para todas las solicitudes del cliente. Se encarga de redirigir las solicitudes a los servicios correctos en la arquitectura de microservicios, gestionar la autenticación y autorización, realizar balanceo de carga, y hasta gestionar el versionado de las APIs. También puede hacer caché de respuestas, reducir la latencia y mejorar la eficiencia.

# LA INTEGRACIÓN ENTRE ESTAS TECNOLOGÍAS PUEDE OFRECER UN SOPORTE SÓLIDO Y EFICIENTE PARA SISTEMAS MODERNOS:

- Escalabilidad: Las arquitecturas cliente-servidor y las APIs facilitan la distribución de la carga de trabajo, ya sea utilizando un solo servidor o un conjunto de microservicios distribuidos. Las APIs permiten la expansión modular de la aplicación sin comprometer el rendimiento.
- Flexibilidad: Al combinar REST API o GraphQL con un API Gateway, puedes adaptarte a diferentes necesidades de los clientes, permitiendo acceso flexible y seguro a los datos o servicios.
- Seguridad: El uso de HTTPS garantiza que las comunicaciones entre clientes y servidores sean seguras. Además, el API Gateway puede gestionar la autenticación y autorización, asegurando que solo los usuarios o sistemas correctos puedan acceder a ciertos recursos.
- Desempeño: Con un buen diseño de API (sea REST o GraphQL) y un API Gateway eficiente, puedes mejorar el desempeño de la red, minimizar la latencia y hacer que el sistema sea más eficiente en términos de recursos.

# ESTA INTEGRACIÓN TAMBIÉN CONLLEVA GRANDES DESAFÍOS:

- Complejidad de Gestión de Microservicios: Si usas microservicios, las APIs y los API Gateways se vuelven esenciales, pero también incrementan la complejidad en términos de gestión, monitoreo y despliegue.
- Seguridad en GraphQL: Aunque GraphQL ofrece mucha flexibilidad, también abre el potencial para ataques como "denegación de servicio" si no se controla adecuadamente lo que los usuarios pueden consultar. Implementar límites y validaciones es crucial.
- Escalabilidad del API Gateway: En sistemas de alto tráfico, el API Gateway puede convertirse en un cuello de botella si no se gestiona adecuadamente. Es importante planificar la infraestructura detrás de este componente.

# ¿CÓMO PODEMOS ASEGURAR UNA COMUNICACIÓN SEGURA ENTRE CLIENTE-SERVIDOR?

La seguridad es crucial en las comunicaciones web. El uso de HTTPS es
fundamental para cifrar los datos entre el cliente y el servidor. Además, la implementación de autenticación y autorización (por ejemplo, OAuth, JWT) ayuda a garantizar que solo usuarios o servicios autorizados accedan a los recursos.

- TÉCNICA: Usar certificados SSL/TLS para HTTPS.
- AUTENTICACIÓN: JWT o OAuth 2.0 para gestionar sesiones seguras. 


# ¿CUÁL ES LA MEJOR OPCIÓN: REST O GRAPHQL PARA MI API?

Depende de las necesidades de tu aplicación y los requisitos del cliente.

- REST: Es ideal si tienes endpoints fijos y las consultas del cliente son relativamente sencillas y bien definidas. Es más fácil de implementar y consumir, pero puede resultar en un mayor uso de ancho de banda cuando se requieren datos adicionales que el cliente no necesita.

- GraphQL: Es ideal si tu aplicación requiere mucha flexibilidad en cuanto a qué datos obtener, especialmente si los clientes pueden necesitar diferentes conjuntos de datos (evitando la sobrecarga o subcarga de información). Es más eficiente en términos de uso de red y permite consultas más complejas.

# ¿CÓMO REDUCIMOS LA LATENCIA EN LAS COMUNICACIONES ENTRE SERVICIOS?

La latencia puede ser un problema crítico, especialmente en arquitecturas distribuidas.

1. API Gateway: Puede ayudar a minimizar la latencia, ya que gestiona de manera eficiente las solicitudes entre microservicios y optimiza los flujos de tráfico. 
2. Optimización de las consultas: Evita consultas demasiado complejas o que involucren múltiples servicios. En su lugar, usa técnicas como denormalización o event sourcing para reducir la necesidad de consultas complejas.

# ¿QUÉ HACER CUANDO UN SERVICIO FALLA O SE DESCONECTA?

La resiliencia y la tolerancia a fallos son esenciales en sistemas distribuidos.

1. Circuit Breakers: Implementa un circuit breaker para que, cuando un servicio falle, el sistema no siga enviando solicitudes y cause más daños.
2. Retries y Exponential Backoff: Reintentar solicitudes fallidas con un exponential backoff (retraso creciente entre intentos) para no sobrecargar el servicio.
3. Fallbacks: Ofrecer respuestas alternativas o "de degradación" cuando un servicio no esté disponible.