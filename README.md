# API de Gestión de Estudiantes

API REST construida con Flask para realizar operaciones CRUD en la base de datos de alumnos.

## Instrucciones de Instalación y Ejecución

1.  **Clonar el repositorio:**

    git clone `https://github.com/tu-usuario/api-estudiantes.git`
    cd api-estudiantes

2.  **Crear y activar un entorno virtual:**

    virtualenv .venv
    source .venv/Scripts/activate

3.  **Instalar dependencias:**

    pip install -r requirements.txt

4.  **Generar la base de datos:**

    python estudiante.py

5.  **Iniciar la API:**

    python main.py

La API estará disponible en `http://127.0.0.1:5000`.


### EXAMEN FINAL - PARTE TEÓRICA

1. Para qué se puede usar Python en lo que respecta a datos. Dar 5 casos y explicar brevemente:

    1. Análisis de Datos: Usando librerías como Pandas y NumPy, se puede limpiar, transformar, filtrar y analizar grandes volúmenes de datos para encontrar patrones o insights.

    2. Visualización de Datos: Con librerías como Matplotlib y Seaborn, se pueden crear gráficos de barras, líneas o mapas de calor para presentar los resultados del análisis de una forma fácil de entender.

    3. Machine Learning: Con Scikit-learn, TensorFlow o PyTorch, se pueden construir modelos predictivos para tareas como clasificación de clientes, predicción de ventas o reconocimiento de imágenes.

    4. Extracción de Datos Web Scraping: Usando Beautiful Soup o Scrapy, se puede extraer información automáticamente de páginas web para crear bases de datos como los precios de productos y hasta noticias.

    5. Ingeniería de Datos (ETL): Python se usa para construir procesos de Extracción, Transformación y Carga que mueven y procesan datos entre diferentes sistemas por ejemplo de una base de datos a un data warehouse.


2. ¿Cómo se diferencian Flask de Django? Argumentar.

La principal diferencia es su filosofía: Flask es un micro-framework minimalista y Django es un framework con baterías incluidas.

    - Flask:

    Minimalista y flexible: Te da lo esencial como las rutas y plantillas y tú decides qué librerías adicionales usar para la base de datos (SQLAlchemy), formularios (WTForms), etc.

    Control total: es ideal para proyectos pequeños, APIs, o cuando quieres tener control total sobre las herramientas y la estructura.

    - Django:

    Completo y estructurado: Viene con todo lo que necesitas de fábrica: un ORM para la base de datos, un panel de administrador, sistema de autenticación, etc.

    Te obliga a seguir una estructura de proyecto específica, lo que acelera el desarrollo de aplicaciones grandes y complejas al seguir un estándar.


3. ¿Qué es un API? Explicar en sus propias palabras.

Un API (Interfaz de Programación de Aplicaciones) es como el camarero de un restaurante.

Tú (una aplicación) no puedes entrar a la cocina (el servidor o la base de datos) a prepararte la comida (los datos). En su lugar, le pides al camarero (el API) lo que quieres del menú (los endpoints disponibles). El camarero lleva tu pedido a la cocina, y te trae de vuelta el plato listo (la respuesta con los datos).

Es un contrato que demuestra cómo dos programas se pueden comunicar, especificando qué peticiones se pueden hacer y qué respuestas se van a recibir.

4. ¿Cuál es la principal diferencia entre REST y WebSockets?

La principal diferencia es el tipo y duración de la conexión.

REST: Es como enviar una carta. El cliente hace una petición, el servidor responde, y la conexión se cierra. Cada interacción es independiente. Es ideal para operaciones CRUD donde no se necesita comunicación constante.

WebSockets: Es como una llamada telefónica. El cliente y el servidor abren una conexión persistente que se mantiene abierta. Ambos pueden enviarse datos en cualquier momento sin tener que hacer una nueva petición. Es ideal para aplicaciones en tiempo real como chats, videojuegos online o dashboards que se actualizan al instante.

5. Describir un ejemplo de API comercial y como funciona - usar otros ejemplos no vistos en el curso.

API de Stripe para pagos online.

Es una API que permite a cualquier sitio web o aplicación aceptar pagos con tarjeta de crédito de forma segura, sin tener que manejar directamente los datos sensibles de la tarjeta.

La tienda online "MiTienda.com" integra la API de Stripe en su página de pago.

Cuando un cliente introduce los datos de su tarjeta y hace clic en "Pagar", esa información no se envía al servidor de "MiTienda.com", sino que viaja de forma segura y encriptada directamente a los servidores de Stripe.

Stripe procesa el pago y devuelve a "MiTienda.com" una respuesta: "éxito" o "fallo".

Si el pago fue exitoso, "MiTienda.com" le muestra al cliente un mensaje de confirmación. La tienda nunca vio ni almacenó el número de la tarjeta, delegando toda la seguridad y el procesamiento a Stripe a través de su API.
