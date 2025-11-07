# 🧠 PayOracle — Predicción de Salario

**PayOracle** es una aplicación web desarrollada con **Django** que implementa un modelo de **Machine Learning** entrenado sobre el conjunto de datos *Adult Census Income* (UCI Repository).
Su objetivo es **predecir si una persona tendrá un salario anual mayor o menor a $50,000 USD**, con base en variables como edad, nivel educativo, ocupación, estado civil y horas trabajadas por semana.

Además de la predicción, **PayOracle** ofrece una **probabilidad asociada a la estimación** y **sugerencias personalizadas** generadas mediante la API de **OpenAI**, que ayudan al usuario a identificar posibles factores de mejora para alcanzar un salario superior.

---

## 📋 Propósito del proyecto

El propósito principal de este proyecto es **combinar técnicas de aprendizaje automático y desarrollo web** para construir una herramienta accesible y práctica de apoyo a la toma de decisiones en el ámbito laboral.
PayOracle busca demostrar cómo los modelos predictivos pueden integrarse dentro de un entorno web para ofrecer **servicios inteligentes basados en datos reales**.

---

## ⚙️ Instalación y ejecución

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/Manco312/payoracle.git
cd payoracle
```

### 2️⃣ Instalar dependencias

```bash
pip install -r "requirements.txt"
```

---

## 🔁 Entrenamiento del modelo (requerido antes de usar la app)

Si el archivo `model.pkl` no se encuentra en la carpeta `salaryapp/ml/model_files`, debes entrenar el modelo ejecutando:

```bash
python salaryapp/ml/train_model.py --data_path salaryapp/ml/adult.csv --out_dir salaryapp/ml/model_files
```

**POR DEFECTO ESTE ARCHIVO YA VIENE PRESENTE AL CLONAR EL PROYECTO, POR TANTO NO ES NECESARIO HACER ESTE PROCESO SI NO HAS BORRADO EL ARCHIVO**

---

## ⚙️ Configuración adicional

### Variables de entorno

Para habilitar las sugerencias generadas por IA, define una variable de entorno con tu clave de OpenAI:

Archivo `.env` o `openAI.env`:

```bash
openAI_api_key=tu_api_key_aqui
```

---

## 🚀 Ejecución del servidor Django

Aplica las migraciones y ejecuta el servidor local:

```bash
python manage.py migrate
python manage.py runserver
```

Luego abre tu navegador en:
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 📦 Dependencias

Django
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
imbalanced-learn
openai
python-dotenv
markdown

---

## 📊 Resultados esperados

* **Predicción automática** del rango salarial (`<=50K` o `>50K`) para un usuario con base en sus características.
* **Probabilidad de acierto** de la predicción.
* **Recomendaciones personalizadas** generadas por IA para mejorar el nivel salarial.
* Interfaz web limpia, moderna e intuitiva que facilita la interacción entre usuario y modelo.

---

## 👨‍💻 Autores

Proyecto desarrollado por:

* **Juan José Gómez Vélez**
* **Luciana Hoyos Pérez**
* **Santiago Manco Maya**