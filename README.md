![Python](https://img.shields.io/badge/Python-3.11-blue)

![scikit-learn](https://img.shields.io/badge/scikit--learn-Latest-orange)

![License](https://img.shields.io/badge/License-MIT-green)

![Status](https://img.shields.io/badge/Status-In%20Development-yellow)
# Penguin Species Classification

Sistema de clasificación de especies de pingüinos mediante técnicas de Aprendizaje Automático utilizando el **Palmer Penguins Dataset Extended**.

El objetivo de este proyecto es desarrollar y evaluar modelos de clasificación capaces de identificar automáticamente la especie de un pingüino a partir de características morfológicas y ecomorfológicas. Además de representar un problema clásico de clasificación supervisada, este proyecto sirve como una demostración práctica de metodologías de Ciencia de Datos que posteriormente pueden extrapolarse a otros dominios, como la acuicultura y la industria camaronera.

---

# Objetivo

Desarrollar un modelo de aprendizaje automático capaz de clasificar con alta precisión las especies de la familia *Spheniscidae* a partir de características morfológicas y ecomorfológicas, priorizando el desempeño predictivo del sistema.

---

# Dataset

El proyecto utiliza el **Palmer Penguins Dataset Extended**, un conjunto de datos ampliamente utilizado para tareas de clasificación supervisada.

La variable objetivo corresponde a la **especie del pingüino**, mientras que las variables predictoras incluyen diferentes características morfológicas y ecológicas de cada individuo.

---

# Tecnologías

- Python
- UV
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn
- Jupyter Notebook
- Git
- GitHub

---

# Estructura del proyecto

```text
penguin-species-classification/

│
├── README.md
├── pyproject.toml
├── uv.lock
├── .gitignore
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   ├── predict.py
│   └── utils.py
│
├── models/
│
├── reports/
│
├── images/
│
└── .venv/
```

---

# Flujo del proyecto

```text
Dataset
    │
    ▼
Análisis Exploratorio de Datos (EDA)
    │
    ▼
Diseño del Pipeline de Preprocesamiento
    │
    ▼
Entrenamiento de Modelos
    │
    ▼
Evaluación
    │
    ▼
Selección del Modelo Final
```

---

# Instalación

Clona el repositorio:

```bash
git clone https://github.com/Micklevar/penguin-species-classification.git
```

Accede al directorio del proyecto:

```bash
cd penguin-species-classification
```

Instala las dependencias mediante **uv**:

```bash
uv sync
```

---

# Ejecución

Una vez instaladas las dependencias, el entrenamiento del modelo podrá ejecutarse mediante:

```bash
python src/train.py
```

> **Nota:** Esta sección podrá actualizarse conforme evolucione el proyecto.

---

# 🚧 Estado del proyecto

Actualmente el proyecto se encuentra en fase de desarrollo.

Próximas etapas:

- Análisis exploratorio de datos (EDA).
- Construcción del pipeline de preprocesamiento.
- Entrenamiento y comparación de modelos de clasificación.
- Evaluación mediante métricas de desempeño.
- Selección del modelo con mejor capacidad de generalización.

---