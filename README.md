# Trabajo Práctico N°2- Modelo de Prediccion de Lluvia en Australia
## AA1-TUIA-2025C1-Aranda-Cicoria-Ricci
Este repositorio contiene el desarrollo del segundo trabajo práctico de la materia **Aprendizaje Automático 1** de la **Tecnicatura en Inteligencia Artificial**. El objetivo desarrollar un modelo predictivo que permita anticipar si **lloverá al día siguiente** (`RainTomorrow`) en distintas regiones de Australia, utilizando datos meteorológicos históricos.

---

### Estructura del notebook

El notebook principal se encuentra en el archivo `TP-clasificacion-AA1.ipynb` y está organizado de la siguiente manera:

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

---

### Requisitos para reproducir

Este proyecto fue desarrollado con Python 3.12 y las siguientes bibliotecas principales:
- `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`
- `category_encoders`
- `scikit-learn`: para preprocesamiento, modelado y evaluación
- `imbalanced-learn`: para tratamiento del desbalance (SMOTE, RandomOverSampler)

---
