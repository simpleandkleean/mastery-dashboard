# Mastery Dashboard - FastAPI + Riot Games API

Este proyecto es un backend desarrollado con **FastAPI** que se conecta a la **API de Riot Games** para recuperar información sobre los puntos de maestría de campeones de *League of Legends*. Está pensado como proyecto de aprendizaje y demostración, no para producción.

---

## Componentes principales

### 1. Riot Client
- Módulo encargado de conectarse a la **API de Riot Games**.  
- Gestiona la autenticación mediante tu **propio token** de Riot Developer Portal.  
- Maneja errores y respuestas de la API de forma controlada.

### 2. Data Dragon
- Permite precargar los archivos estáticos de Riot (**campeones, imágenes, nombres, etc.**).  
- Los routers pueden acceder a estos datos sin necesidad de consultar constantemente la API.  
- Evita subir los más de 11.000 archivos al repositorio gracias a la carga por enlace y cache local.

### 3. Routers
- **Champion**  
  Recupera información estática de los campeones usando:
  - Nombre
  - Key
  - ID  
  Además incluye título e imagen del campeón.

- **Mastery**  
  Recupera los puntos de maestría de un campeón:  
  - Por **ID** directamente desde la API de Riot.  
  - Por **nombre** mediante un endpoint interno que traduce el nombre a ID usando los datos precargados de Data Dragon.

---

## Requisitos
- Tener una cuenta en el **Riot Developer Portal** y generar un token de desarrollador.
- Python 3.10+ (u otra versión compatible con FastAPI).
- FastAPI y dependencias listadas en `requirements.txt`.

---

## Advertencias
- Este proyecto es **solo con fines de aprendizaje**.  
- No es apto para producción: la API de Riot requiere **una key de producción** para uso profesional.  
- Se recomienda **no subir tokens privados** al repositorio.  
- Al ser datos estáticos, es mejor recuperarlos directamente desde el **Riot Developer Portal**, y usar los endpoints solo para datos dinámicos.

---

## Instalación y uso
1. Clonar el repositorio:

```bash
git clone https://github.com/TU_USUARIO/mastery-dashboard.git
cd mastery-dashboard
