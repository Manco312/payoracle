from django import forms

# Para mantenerlo práctico incluimos los campos principales del dataset Adult.
WORKCLASS_CHOICES = [
    ("Private","Private"), ("Self-emp-not-inc","Self-emp-not-inc"),
    ("Self-emp-inc","Self-emp-inc"), ("Federal-gov","Federal-gov"),
    ("Local-gov","Local-gov"), ("State-gov","State-gov"),
    ("Without-pay","Without-pay"), ("Never-worked","Never-worked")
]

EDUCATION_CHOICES = [
    ("Bachelors","Bachelors"), ("Some-college","Some-college"),
    ("11th","11th"), ("HS-grad","HS-grad"), ("Prof-school","Prof-school"),
    ("Assoc-acdm","Assoc-acdm"), ("Assoc-voc","Assoc-voc"), ("9th","9th"),
    ("7th-8th","7th-8th"), ("12th","12th"), ("Masters","Masters"),
    ("1st-4th","1st-4th"), ("10th","10th"), ("Doctorate","Doctorate"),
    ("5th-6th","5th-6th"), ("Preschool","Preschool")
]

MARITAL_CHOICES = [
    ("Never-married","Never-married"), ("Married-civ-spouse","Married-civ-spouse"),
    ("Divorced","Divorced"), ("Married-spouse-absent","Married-spouse-absent"),
    ("Separated","Separated"), ("Widowed","Widowed")
]

OCCUPATION_CHOICES = [
    ("Tech-support","Tech-support"), ("Craft-repair","Craft-repair"),
    ("Other-service","Other-service"), ("Sales","Sales"), ("Exec-managerial","Exec-managerial"),
    ("Prof-specialty","Prof-specialty"), ("Handlers-cleaners","Handlers-cleaners"),
    ("Machine-op-inspct","Machine-op-inspct"), ("Adm-clerical","Adm-clerical"),
    ("Farming-fishing","Farming-fishing"), ("Transport-moving","Transport-moving"),
    ("Priv-house-serv","Priv-house-serv"), ("Protective-serv","Protective-serv"),
    ("Armed-Forces","Armed-Forces")
]

RELATIONSHIP_CHOICES = [
    ("Wife","Wife"), ("Own-child","Own-child"), ("Husband","Husband"),
    ("Not-in-family","Not-in-family"), ("Other-relative","Other-relative"),
    ("Unmarried","Unmarried")
]

RACE_CHOICES = [("White","White"), ("Black","Black"), ("Asian-Pac-Islander","Asian-Pac-Islander"),
                ("Amer-Indian-Eskimo","Amer-Indian-Eskimo"), ("Other","Other")]

NATIVE_COUNTRY_CHOICES = [
    ("United-States","United-States"), ("Mexico","Mexico"), ("Philippines","Philippines"),
    ("Germany","Germany"), ("Canada","Canada"), ("India","India"), ("China","China"),
    ("Other","Other")
]

SEX_CHOICES = [("Male","Male"), ("Female","Female")]

class SalaryForm(forms.Form):
    age = forms.IntegerField(min_value=16, max_value=120, initial=30)
    workclass = forms.ChoiceField(choices=WORKCLASS_CHOICES)
    education = forms.ChoiceField(choices=EDUCATION_CHOICES)
    education_num = forms.IntegerField(min_value=1, max_value=16, label="education.num")
    marital_status = forms.ChoiceField(choices=MARITAL_CHOICES)
    occupation = forms.ChoiceField(choices=OCCUPATION_CHOICES)
    relationship = forms.ChoiceField(choices=RELATIONSHIP_CHOICES)
    race = forms.ChoiceField(choices=RACE_CHOICES)
    sex = forms.ChoiceField(choices=SEX_CHOICES)
    capital_gain = forms.IntegerField(min_value=0, initial=0)
    capital_loss = forms.IntegerField(min_value=0, initial=0)
    hours_per_week = forms.IntegerField(min_value=1, max_value=100, initial=40)
    native_country = forms.ChoiceField(choices=NATIVE_COUNTRY_CHOICES)
