from django.shortcuts import render, redirect
from .forms import SalaryForm
from .ml.predict import predict_from_dict
import os
from openai import OpenAI
from django.conf import settings
from dotenv import load_dotenv
import markdown

# Asegúrate de fijar OPENAI_API_KEY en las variables de entorno o .env

def home(request):
    if request.method == "POST":
        form = SalaryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Normalizamos nombres de columnas si hace falta:
            input_dict = {
                "age": data["age"],
                "workclass": data["workclass"],
                "education": data["education"],
                "education.num": data["education_num"] if "education_num" in data else data.get("education_num"),
                "education_num": data["education_num"],
                "marital.status": data["marital_status"],
                "occupation": data["occupation"],
                "relationship": data["relationship"],
                "race": data["race"],
                "sex": data["sex"],
                "capital.gain": data["capital_gain"],
                "capital.loss": data["capital_loss"],
                "hours.per.week": data["hours_per_week"],
                "native.country": data["native_country"]
            }

            # map keys to dataset column names expected by the pipeline
            # Ajusta si tu pipeline espera nombres sin puntos.
            # Aquí asumimos columnas sin puntos: education_num, capital_gain, hours_per_week, native_country, etc.
            mapped = {
                "age": data["age"],
                "workclass": data["workclass"],
                "education": data["education"],
                "education.num": data["education_num"],
                "education_num": data["education_num"],
                "marital.status": data["marital_status"],
                "marital_status": data["marital_status"],
                "occupation": data["occupation"],
                "relationship": data["relationship"],
                "race": data["race"],
                "sex": data["sex"],
                "capital.gain": data["capital_gain"],
                "capital_gain": data["capital_gain"],
                "capital.loss": data["capital_loss"],
                "capital_loss": data["capital_loss"],
                "hours.per.week": data["hours_per_week"],
                "hours_per_week": data["hours_per_week"],
                "native.country": data["native_country"],
                "native_country": data["native_country"]
            }

            # Prepare input for model: pick the keys that your trained pipeline expects.
            # Aquí asumiré que el pipeline fue entrenado con columnas sin puntos:
            model_input = {
                "age": mapped["age"],
                "workclass": mapped["workclass"],
                "education": mapped["education"],
                "education.num": mapped["education_num"],
                "marital.status": mapped["marital_status"],
                "occupation": mapped["occupation"],
                "relationship": mapped["relationship"],
                "race": mapped["race"],
                "sex": mapped["sex"],
                "capital.gain": mapped["capital_gain"],
                "capital.loss": mapped["capital_loss"], 
                "hours.per.week": mapped["hours_per_week"], 
                "native.country": mapped["native_country"]
            }

            # Ajusta keys según como estuvieron en tu CSV. Lo importante: coincide con entrenamiento.
            # Llamamos al predict
            try:
                pred, prob = predict_from_dict(model_input)
            except Exception as e:
                return render(request, "salaryapp/result.html", {
                    "error": str(e),
                    "form": form
                })

            # Llamada a OpenAI para sugerencias
            suggestions = call_openai_suggestions(model_input, pred)

            return render(request, "salaryapp/result.html", {
                "prediction": pred,
                "prob": round(prob, 3),
                "suggestions": suggestions,
                "form": form
            })
    else:
        form = SalaryForm()

    return render(request, "salaryapp/form.html", {"form": form})


def call_openai_suggestions(input_data, prediction):
    """
    Llama a la API de OpenAI para pedir sugerencias prácticas para mejorar salario.
    Se espera que OPENAI_API_KEY esté en las variables de entorno.
    """
    _ = load_dotenv('openAI.env')

    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get('openAI_api_key'),
    )

    prompt = (
        "Eres un asesor laboral. Un modelo clasificó a esta persona como "
        f"'{prediction}'. Aquí están sus datos: {input_data}. "
        "Proporciona 4 sugerencias practiceas y accionables (máx 3 frases cada una) "
        "para mejorar las probabilidades de que esta persona llegue a un salario >50K. "
        "Sé concreto: cambios en educación, habilidades, horas, sectores, negociación salarial, "
        "o roles a buscar. Devuelve la respuesta en formato de lista numerada."
    )

    try:

        model="gpt-4o-mini"
        messages=[
            {"role": "system", "content": "Eres un asistente profesional que da consejos laborales."},
            {"role": "user", "content": prompt}
        ]
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=1000,
            temperature=0.5
        )

        texto = response.choices[0].message.content
        texto_formateado = markdown.markdown(texto)
        return texto_formateado
    except Exception as e:
        return [f"Error llamando a OpenAI: {e}"]
