def cods_historico_creditos():
    return {
        "A30": "no credits taken/all credits paid back duly",
        "A31": "all credits at this bank paid back duly",
        "A32": "existing credits paid back duly till now",
        "A33": "delay in paying off in the past",
        "A34": "critical account/other credits existing (not at this bank)"}


def cods_proposito():
    return {
        "A40": "car(new)",
        "A41": "car(used)",
        "A42": "furniture/equipment",
        "A43": "radio/television",
        "A44": "domestic appliances",
        "A45": "repairs",
        "A46": "education",
        "A47": "vacation",
        "A48": "retraining",
        "A49": "business",
        "A410": "others"}


def cods_estado_civil_sexo():
    return {
        "A91": "male : divorced/separated",
        "A92": "female : divorced/separated/married",
        "A93": "male : single",
        "A94": "male : married/windowed",
        "A95": "female : single"}


def cods_outros_devedores():
    return {
        "A101": "no", #None,
        "A102": "co-applicant",
        "A103": "guarantor"}


def codigos_propriedade():
    return {
        "A121": "real state",
        "A122": "building society/life insurance",
        "A123": "car",
        "A124": "unknown/no property"}


def cods_planos_de_parcelamento():
    return {
        "A141": "bank",
        "A142": "stores",
        "A143": "None"}


def cods_residencia():
    return {
        "A151": "rent",
        "A152": "own",
        "A153": "for free"}


def cods_estado_emprego():
    return {
        "A171": "unemployed/unskilled-non-resident",
        "A172": "unskilled-resident",
        "A173": "skilled employee/official",
        "A174": "management/self-employed/highly qualified employee/officer"}


def cods_telefone():
    return {
        "A191": "no", # none
        "A192": "yes"}


def cods_trabalhador_estrangeiro():
    return {
        "A201": "yes",
        "A202": "no"}
		
# Mapeando variáveis contínuas

def cods_status_atual_conta_corrente():
	return {
    "A11": "< 0",
    "A12": "< 199",
    "A13": ">= 200",
    "A14": "no checking account" }

def cods_reserva_poupanca():
	return {
    "A61": "< 100",
    "A62": "< 499",
    "A63": "< 999",
    "A64": ">= 1000",
    "A65": "unknown"}

def cods_tempo_emprego():
    return {
    "A71": "unemployed",
    "A72": "< 1", # Menos de 1 ano
    "A73": "< 4", # Entre 1 ano e menos que 4 anos
    "A74": "< 7", # Entre 4 anos e menos que 7 anos
    "A75": ">= 7"} # Mais de 7 anos
