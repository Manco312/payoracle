# 🧠 PayOracle — Predicción de Salario

**PayOracle** es una aplicación web desarrollada con **Django** que utiliza un modelo de **Machine Learning** para predecir si una persona ganará `<=50K` o `>50K`, basándose en información como educación, ocupación, edad, horas semanales, etc.

---

### Clona el repositorio

```bash
git clone https://github.com/Manco312/payoracle.git
cd payoracle
```

### Instala dependencias

```bash
pip install -r requirements.txt
```
---

## 🔁 Entrenar el modelo (obligatorio antes de usar la app)

```bash
python salaryapp/ml/train_model.py --data_path salaryapp/ml/adult.csv --out_dir salaryapp/ml/model_files
```

* El script creará la carpeta `salaryapp/ml/model_files` (si no existe) y guardará `model.pkl` allí.

---

## 🔧 Configuración adicional

### Variables de entorno

* **openAI_api_key** — para que la app pueda pedir sugerencias a OpenAI.

En una variable de entorno llamada openAI.env colocar:
```bash
openAI_api_key=tu_api_key_aqui
```

### Migraciones y ejecución

```bash
python manage.py migrate
python manage.py runserver
```

Abre: `http://127.0.0.1:8000/`

---

