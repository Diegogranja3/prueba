# Diario Inteligente con IA

Version de prueba: https://prueba-frontend-xqga.onrender.com/
***Si aparece Ocurrió un error al procesar con IA.  es probable que ya no haya mas solicitudes gratuitas ***

Una aplicación web tipo diario personal con inteligencia artificial integrada que enriquece las entradas del usuario.

#Requisitos previos
- Python 3.8+
- Node.js 16+
- Cuenta en [Google AI Studio](https://aistudio.google.com/) para la API Key
   
# Instrucciones para ejecutarse
- Clonar el proyecto
    git clone https://github.com/tu-usuario/tu-repo.git
- Instalar las dependencias necesarias (backend/requeriments.txt)
    fastapi==0.116.0
    pydantic==2.11.7
    python-dotenv==1.1.1
    SQLAlchemy==2.0.41
    uvicorn[standard]==0.24.0
    google-generativeai==0.8.3
- Abrir una terminal dentro de la carpeta backend y ejecutar
    uvicorn main:app --reload
- Abrir una terminal dentro de la carpeta frontend y ejecutar
    npm run dev
- Generar una API key para Gemini en Google studio AI
- Ingresar la API key en un archivo .env con el siguiente formato
    GEMINI_API_KEY= tu_api_key
- El programa deberia funcionar

# Características
- Un usuario puede guardar sus ideas y posteriormente editarlas
- Un usuario puede filtrar entre las ideas existentes
- Un usuario puede eliminar notas ya existentes
- Un usuario puede decidir si quiere retroalimentacion de una IA o no


# Tecnologías

- [FastAPI](https://fastapi.tiangolo.com/) — Backend en Python
- [Vue.js](https://vuejs.org/) — Frontend interactivo
- [Axios](https://axios-http.com/) — Comunicación entre frontend y backend
- [SQLite](https://www.sqlite.org/index.html) — Base de datos local
- [Tailwind CSS](https://tailwindcss.com/) — Estilos modernos 

# Mi proceso con inteligencia artificial
  IAs utilizadas
  - Chatgpt
  - Deepseek
  - Claude

Ejemplos de prompts: 
- Convierte esta seccion del codigo que funciona con un puerto localhost con la url del backend para hacerlo deployable
- Genera el endpoint con fastapi y la llamada de axios al mismo para usar la ia de google
- Genera un prompt para gemini en el que de la menor cantidad de informacion innecesaria
- Revisa esta seccion de codigo y busca optimizarlo

Reflexion:
Definitivamente el uso de las IAs fueron indispensables para terminar este proyecto en menos de 15 horas, por su puesto que se puede mejorar,
tuve que hacerlo todo el mismo dia porque estare ausente el dia de mañana, pero con esto demuestro que todo es posible con un poco de ayuda

Mayor desafio:
Yo nunca habia hecho un deploy de una aplicacion web, de hecho el proyecto que tengo ahora mismo conlleva eso y si no hubiera sido por esta 
prueba probablemente hubiera estado en un problema grave, asi que agradezco la oportunidad de trabajar en esta prueba tecnica




