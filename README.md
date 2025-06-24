# Trabajo Práctico N°2- Modelo de Prediccion de Lluvia en Australia
## AA1-TUIA-2025C1-Aranda-Cicoria-Ricci
Este repositorio contiene el desarrollo del segundo trabajo práctico de la materia **Aprendizaje Automático 1** de la **Tecnicatura en Inteligencia Artificial**. El objetivo desarrollar un modelo predictivo que permita anticipar si **lloverá al día siguiente** (`RainTomorrow`) en distintas regiones de Australia, utilizando datos meteorológicos históricos.

---

### Estructura del repositorio

```
├── docker/                      # Archivos para deployment con Docker
│   ├── Dockerfile               # Instrucciones de build & run
│   ├── README.md                # Documentación Docker
│   ├── inferencia.py            # Script de inferencia
│   ├── requirements.txt         # Librerías para inferencia
│   ├── pipeline.pkl             # Pipeline serializado (joblib)
│   └── transformadores/         # Módulos custom para preprocesado
├── TP-clasificacion-AA1.ipynb  # Notebook principal de modelado
├── MLOps.ipynb             # Notebook de deployment y  Docker
├── weatherAUS.csv           # Dataset original de Australia
├── coordenadas_aus.csv          # Coordenadas para clustering geográfico
├── README.md                    # Este archivo
```

### Notebook principal (`TP-clasificacion-AA1.ipynb`)

- **Contexto**: presentación del problema, descripción de variables y librerías utilizadas.
- **Carga y análisis exploratorio del dataset**.
- **Preprocesamiento de datos**:
  - Segmentación temporal
  - Imputación jerárquica de valores faltantes
  - Detección y tratamiento de outliers
  - Codificación y escalado de variables
- **Modelado**:
  - Entrenamiento con regresión logística
  - Evaluación del modelo mediante métricas
- **Tratamiento del desbalance**:
  - Aplicación de técnicas como **Oversampling** y **SMOTE**
  - Comparación entre matrices de confusión
- **Modelo Base**
- **Optimización de Hiperparámetros**
- **Explicabilidad**
- **AutoML**
- **Redes Neuronales**:
  - Modelado
  - Optimizacion de Hiperparametros
  - Explicabilidad
- **Comparacion de modelos**

---

### Notebook de MLOps (`MLOps.ipynb`)
Contiene el flujo para:
  - Serializar el pipeline con joblib
  - Docker
  - Demostración de inferencia en batch y de un ejemplo puntual
    
---

### Deployment con Docker

Toda la información para construir y ejecutar la imagen Docker está en docker/README.md.

---

### Modelo utilizado

- **Regresión Logística** (`LogisticRegression` de scikit-learn)

---

### Métricas de evaluación

Se utilizaron las siguientes métricas para evaluar el rendimiento del modelo:

- **Recall**
- **Precision**
- **F1 Score**

Además, se visualizó la **matriz de confusión** y la **curva ROC** para evaluar el comportamiento del modelo frente al desbalance de clases.

---

### Dataset
  - `weatherAUS.csv`: registros meteorológicos de Australia (últimos 10 años).
  - `coordenadas_aus.csv`: coordenadas geográficas para clustering

---

### Requisitos para reproducir

Este proyecto fue desarrollado con Python 3.11 y las siguientes bibliotecas principales:
- `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`
- `category_encoders`: para codificación de variables categóricas
- `scikit-learn`: para preprocesamiento, modelado y evaluación
- `imbalanced-learn`: para tratamiento del desbalance (SMOTE, RandomOverSampler)
- `optuna`: para optimización automática de hiperparámetros
- `shap`: para interpretación de modelos de machine learning
- `pycaret`: para automatización del flujo de trabajo de machine learning

---

