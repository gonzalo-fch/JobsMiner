# JobsMiner

## 🎯 Objetivo

El objetivo de este proyecto es construir un dataset de ofertas laborales en el área de ingeniería de software, a partir de plataformas de empleo online, con el fin de analizar posteriormente el perfil profesional más demandado.

---

## 🌐 Fuente de Datos

Se seleccionaron dos plataformas de empleo orientadas a trabajos tecnológicos remotos:

* **RemoteOK API**: https://remoteok.com/api
* **Remotive API**: https://remotive.com/api/remote-jobs

### 🔎 Justificación

Ambas plataformas ofrecen acceso directo a sus datos mediante API pública, lo que permite:

* Evitar técnicas de web scraping
* Obtener datos estructurados en formato JSON
* Reducir complejidad técnica y riesgos legales

Por esta razón, se decidió utilizar **APIs como mecanismo principal de recolección de datos**.

---

## ⚙️ Proceso de Extracción

Se desarrollaron dos scripts en Python que realizan:

1. Solicitud HTTP a la API
2. Validación de respuesta
3. Limpieza y transformación de datos
4. Almacenamiento en formato JSON

### 🔒 Control de solicitudes

Se implementó una clase `RequestLimiter` para limitar la cantidad de requests y evitar sobrecargar la API.

---

## 🧹 Estructura del Dataset

Cada registro corresponde a una oferta laboral e incluye los siguientes atributos:

| Atributo  | Descripción                          |
| --------- | ------------------------------------ |
| id        | Identificador único del trabajo      |
| titulo    | Nombre del cargo                     |
| empresa   | Nombre de la empresa                 |
| ubicacion | Ubicación o modalidad                |
| categoria | Área del trabajo (Remotive)          |
| tipo      | Tipo de contrato                     |
| tags      | Tecnologías o habilidades requeridas |
| salario   | Rango salarial (si disponible)       |
| url       | Enlace a la oferta                   |
| fecha     | Fecha de publicación                 |

### 🧠 Justificación de atributos

Estos atributos permiten analizar:

* Tecnologías más demandadas
* Tipos de trabajo (remoto, full-time, etc.)
* Distribución de salarios
* Requisitos del mercado laboral

---

## 📁 Dataset

El dataset generado se almacena en archivos JSON:

* `remote_jobs.json`
* `remotive_jobs.json`

Cada archivo contiene múltiples registros de ofertas laborales.

✔ Se incluyen al menos **50 registros completos**, cumpliendo con el requisito de la tarea.

---

## ▶️ Cómo ejecutar el proyecto

### 1. Instalar dependencias

```bash
pip install requests
```

### 2. Ejecutar scripts

```bash
python remoteok_script.py
python remotive_script.py
```

### 3. Resultado

Los archivos JSON se guardarán automáticamente en el escritorio del usuario.

---

## 📌 Consideraciones Técnicas

* Se utilizó Python por su simplicidad en consumo de APIs
* Se trabajó con JSON como formato estándar
* No fue necesario web scraping
* Se manejaron posibles errores de conexión y límites de requests

---

## 🚀 Posibles mejoras

* Unificar ambos datasets en uno solo
* Normalizar tecnologías (ej: "JS" → "JavaScript")
* Agregar más fuentes de datos
* Exportar a CSV o base de datos
* Automatizar recolección periódica

---

## 📎 Conclusión

El uso de APIs permitió obtener un dataset estructurado, consistente y suficientemente rico para realizar análisis posteriores sobre el perfil del ingeniero de software más demandado en el mercado laboral.

---
