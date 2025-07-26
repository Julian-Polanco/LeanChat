# -*- coding: utf-8 -*-
"""
Base de Conocimiento para LeanChat, el asistente de INGE LEAN S.A.S.
"""

SYSTEM_PROMPT = """
Eres LeanChat, el asistente inteligente y amable de INGE LEAN S.A.S., una empresa pereirana líder en ingeniería. Tu misión es brindar información precisa, eficiente y profesional sobre nuestros servicios en software, hardware, automatización industrial, inteligencia artificial y mantenimiento.

Tu personalidad es:
- **Profesional y Confiable:** Proporciona información experta y veraz.
- **Eficiente y Directo:** Responde de forma concisa, yendo al punto.
- **Amigable y Cercano:** Usa un lenguaje accesible y un tono servicial, mostrando empatía cuando sea necesario.
- **Orientado a Soluciones:** Guía al usuario hacia la mejor respuesta o el siguiente paso, ofreciendo ayuda proactiva.
- **Innovador:** Refleja la vanguardia tecnológica de INGE LEAN.

Cuando saludes, hazlo de manera cordial y ofrece tu ayuda. Si no entiendes una pregunta, solicita al usuario que la reformule o sugiérele contactar a un especialista. Tu objetivo es optimizar la experiencia del cliente y la eficiencia de la atención.
"""

KNOWLEDGE_BASE = {
    "informacion_general": {
        "question": "¿Qué tipo de soluciones ofrece Inge Lean?",
        "patterns": ["qué servicios ofrecen", "qué hacen", "soluciones de Inge Lean", "a qué se dedican"],
        "answer": "En INGE LEAN S.A.S. ofrecemos soluciones a medida en software, hardware, automatización industrial, inteligencia artificial y mantenimiento. Nuestro objetivo es impulsar la eficiencia y competitividad de procesos industriales y comerciales."
    },
    "control_electrico": {
        "question": "¿Qué es Control Eléctrico y qué servicios brindan?",
        "patterns": ["control eléctrico", "diseño de tableros", "circuitos eléctricos", "levantamiento de planos"],
        "answer": "En Control Eléctrico, ofrecemos soluciones para optimizar la producción. Esto incluye el diseño e implementación de circuitos y tableros eléctricos, levantamiento de planos y desarrollo de tableros de maniobra y control."
    },
    "telemetria": {
        "question": "¿Qué es la Telemetría y cómo funciona en Inge Lean?",
        "patterns": ["qué es telemetría", "sensores en la nube", "seguimiento de temperatura", "alertas de telemetría"],
        "answer": "Nuestra solución de Telemetría permite sincronizar sensores (como temperatura y humedad) en la nube, con seguimiento en tiempo real. Genera alertas vía correo o Telegram y ofrece historiales de datos exportables en formatos como CSV, PDF y XLS."
    },
    "datalogger": {
        "question": "¿Qué es un Datalogger y para qué se usa?",
        "patterns": ["qué es un datalogger", "equipo para capturar datos", "usos de datalogger"],
        "answer": "Un Datalogger es un equipo que captura y almacena datos de diferentes sensores (temperatura, humedad, etc.) para su análisis. Se utiliza ampliamente en la industria, transporte, agricultura y laboratorios para monitorear condiciones."
    },
    "integracion_m2m": {
        "question": "¿Qué significa Integración M2M?",
        "patterns": ["qué es M2M", "Machine to Machine", "interconexión digital"],
        "answer": "La Integración M2M (Machine to Machine) es la comunicación directa entre máquinas. Permite la interconexión digital a través de un servidor para que equipos de producción y control de calidad intercambien información a nivel industrial."
    },
    "software": {
        "question": "¿Qué servicios de Software ofrece Inge Lean?",
        "patterns": ["desarrollo de software", "apps móviles", "análisis de datos", "cloud computing", "machine learning"],
        "answer": "En Software, creamos programas de procesos, desarrollos especializados para producción, aplicaciones móviles, análisis de datos, y soluciones de Cloud Computing y Machine Learning."
    },
    "capacitaciones": {
        "question": "¿Inge Lean ofrece capacitaciones?",
        "patterns": ["cursos", "entrenamientos", "acompañamiento", "capacitación Inge Lean"],
        "answer": "Sí, ofrecemos capacitaciones y acompañamiento en cada uno de nuestros servicios. Brindamos conocimientos, herramientas y habilidades para que nuestros clientes puedan interactuar eficientemente en su entorno laboral."
    },
    "ubicacion": {
        "question": "¿Dónde se ubica Inge Lean?",
        "patterns": ["dirección", "ubicación", "dónde están", "localización"],
        "answer": "Nuestra sede principal está en la Calle 29 N. 10-23, barrio La Victoria, en Pereira, Risaralda, Colombia."
    },
    "contacto": {
        "question": "¿Cuál es el contacto de Inge Lean?",
        "patterns": ["teléfono de contacto", "correo electrónico", "email Inge Lean", "contactar a Inge Lean", "números telefónicos", "whatsapp"],
        "answer": "Puedes contactarnos a través de varios canales: \n- **WhatsApp:** [+57 304 326 2538](https://api.whatsapp.com/send/?phone=573043262538) \n- **Correo principal:** contacto@ingelean.com \n- **Correo comercial:** comercial@ingelean.com \n- **Teléfonos:** (+57) 321 594-2872 y (+57) 304 326-2538. \n- **Nuestra web:** www.ingelean.com. \nTambién puedes encontrarnos en nuestras redes sociales."
    },
    "proyectos_realizados": {
        "question": "¿Qué tipo de proyectos realiza Inge Lean?",
        "patterns": ["proyectos que han hecho", "ejemplos de proyectos", "trabajos realizados"],
        "answer": "Realizamos una amplia gama de proyectos, incluyendo automatización industrial, diseño de tableros eléctricos, sistemas embebidos, integración M2M, repotencialización de maquinaria, marquillado, domótica, y el desarrollo de máquinas especializadas como dosificadoras e inyectoras."
    },
    "experiencia": {
        "question": "¿Cuál es la experiencia de Inge Lean en el mercado?",
        "patterns": ["cuánto tiempo llevan", "desde cuándo existen", "experiencia de la empresa"],
        "answer": "Somos una empresa pereirana constituida en 2013. Contamos con un equipo de profesionales altamente calificados y experimentados, comprometidos con la calidad y el alto desempeño en cada proyecto."
    },
    "electronica": {
        "question": "¿Qué servicios ofrece en Electrónica?",
        "patterns": ["electrónica", "automatismos electrónicos", "microcontroladores IOT"],
        "answer": "En Electrónica, integramos automatismos con desarrollo electrónico a medida y programamos microcontroladores, incluyendo aquellos orientados al Internet de las Cosas (IoT)."
    },
    "mecanica": {
        "question": "¿Qué servicios ofrece en Mecánica?",
        "patterns": ["mecánica", "diseño 3D", "fabricación de piezas", "estructuras para máquinas"],
        "answer": "Nuestros servicios de Mecánica incluyen diseño e impresión de piezas en 3D, levantamiento de sólidos, planos de piezas, fabricación de componentes metalmecánicos y estructuras para maquinaria."
    },
    "proceso_propuesta": {
        "question": "¿Cómo es el proceso antes de una propuesta de proyecto?",
        "patterns": ["proceso de propuesta", "cómo trabajan antes de un proyecto", "identificación de detalles"],
        "answer": "Antes de presentar una propuesta, realizamos un proceso riguroso: verificamos la información proporcionada por el cliente, identificamos todos los detalles técnicos, completamos la información necesaria, describimos el alcance del trabajo, especificamos los costos y revisamos los términos y condiciones para asegurar una ejecución exitosa."
    },
    "proyectos_recientes": {
        "question": "¿Qué proyectos recientes han realizado?",
        "patterns": ["últimos proyectos", "novedades de proyectos", "proyectos recientes"],
        "answer": "Algunos de nuestros proyectos recientes más destacados incluyen soluciones de Domótica, una máquina dosificadora de maní, desarrollo de tarjetas con tecnología NFC, y nuestros productos de telemetría como el Termohigrómetro DMP–TH22B, DMP Lab IoT y DMP Lab Industry."
    },
    "ingelean_plus": {
        "question": "¿Qué es IngeLeanPlus?",
        "patterns": ["ingelean plus", "ingelean+", "plataforma ingelean"],
        "answer": "IngeLeanPlus es nuestro ecosistema de soluciones y plataforma diseñada para potenciar las operaciones de nuestros clientes. Ofrece herramientas versátiles y avanzadas para optimizar procesos, desde el análisis de datos en tiempo real hasta la gestión eficiente de recursos. Es el futuro de la eficiencia y la innovación."
    },
    "redes_sociales": {
        "question": "¿Cuáles son las redes sociales de Inge Lean?",
        "patterns": ["redes sociales", "facebook", "linkedin", "instagram", "youtube"],
        "answer": "¡Claro! Puedes seguirnos en nuestras redes sociales para estar al día de nuestros proyectos y novedades:\n- **Facebook:** [facebook.com/Inge.lean](https://www.facebook.com/Inge.lean)\n- **LinkedIn:** [linkedin.com/in/inge-lean](https://www.linkedin.com/in/inge-lean-979526303/)\n- **Instagram:** [instagram.com/inge.lean](https://www.instagram.com/inge.lean/)\n- **YouTube:** [youtube.com/channel/UCn-g4TkGdHqI8pmIXnqUEbA](https://www.youtube.com/channel/UCn-g4TkGdHqI8pmIXnqUEbA)"
    }
}

def get_knowledge_base_text():
    """
    Convierte la base de conocimiento en un texto plano para ser usado en el prompt.
    """
    kb_text = "Aquí tienes la base de conocimiento sobre la empresa:\n\n"
    for key, value in KNOWLEDGE_BASE.items():
        kb_text += f"- Pregunta: {value['question']}\n"
        kb_text += f"  Respuesta: {value['answer']}\n\n"
    return kb_text
