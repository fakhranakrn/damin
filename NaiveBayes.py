import numpy as np
import pandas as pd
# import csv

# def loadData(file):
# 	data = []
# 	with open(file) as csv_file:
# 		csv_reader = csv.reader(csv_file, delimiter=',')
# 		line_count=0
# 		for row in csv_reader:
# 			data.append(row)
# 	return data

def loadData():
	data = pd.read_csv("breast-cancer.csv" ,delimiter =',')
	return data

def class_prob(data):
    c1,c2 = 0,0
    for i in data["class"]:
        if i == "yes":
            c1+=1
        else:
            c2+=2
    rec_class = {
        "yes" : c1,
        "no" : c2
    }

    return rec_class

def age_prob(data):
    rec_age = {
        "10-19y" : 0,
        "20-29y" : 0,
        "30-39y" : 0,
        "40-49y" : 0,
        "50-59y" : 0,
        "60-69y" : 0,
        "70-79y" : 0,
        "80-89y" : 0,
        "90-99y" : 0,
        "10-19n" : 0,
        "20-29n" : 0,
        "30-39n" : 0,
        "40-49n" : 0,
        "50-59n" : 0,
        "60-69n" : 0,
        "70-79n" : 0,
        "80-89n" : 0,
        "90-99n" : 0
    }
    
    for i in (data):
        if (data["age"] == "10-19" and data["class"] == "yes"):
            rec_age["10-19y"]  += 1
        if (data["age"] == "10-19" and data["class"] == "no"):
            rec_age["10-19n"] += 1
        
        if (data["age"] == "20-29" and data["class"] == "yes"):
            rec_age["20-29y"] += 1
        if (data["age"] == "20-29" and data["class"] == "no"):
            rec_age["10-19n"] += 1

        if (data["age"] == "10-19" and data["class"] == "yes"):
            rec_age["10-19y"] += 1
        if (data["age"] == "10-19" and data["class"] == "no"):
            rec_age["10-19n"] += 1

        if (data["age"] == "10-19" and data["class"] == "yes"):
            rec_age["10-19y"] += 1
        if (data["age"] == "10-19" and data["class"] == "no"):
            rec_age["10-19n"] += 1

        if (data["age"] == "10-19" and data["class"] == "yes"):
            rec_age["10-19y"] += 1
        if (data["age"] == "10-19" and data["class"] == "no"):
            rec_age["10-19n"] += 1

        if (data["age"] == "10-19" and data["class"] == "yes"):
            rec_age["10-19y"] += 1
        if (data["age"] == "10-19" and data["class"] == "no"):
            rec_age["10-19n"] += 1

        if (data["age"] == "10-19" and data["class"] == "yes"):
            rec_age["10-19y"] += 1
        if (data["age"] == "10-19" and data["class"] == "no"):
            rec_age["10-19n"] += 1

        cla = class_prob(data)

        return rec_age
    
# print(age_prob(loadData()))

def menopause_prob(data):
    rec_meno = {
        "premeno_y" : 0,
        "premeno_n" : 0,

        "ge40_y" : 0,
        "ge40_n" : 0,

        "lt40_y" : 0,
        "lt40_n" : 0
    }

    for i in data:
        if (data["menopause"] == "premeno" and data["class"] == "yes"):
            rec_meno["premeno_y"] += 1
        if (data["menopause"] == "premeno" and data["class"] == "no"):
            rec_meno["premeno_n"] += 1

        if (data["menopause"] == "ge40" and data["class"] == "yes"):
            rec_meno["ge40_y"] += 1
        if (data["menopause"] == "ge40" and data["class"] == "no"):
            rec_meno["ge40_n"] += 1

        if (data["menopause"] == "lt40" and data["class"] == "yes"):
            rec_meno["lt40_y"] += 1
        if (data["menopause"] == "lt40" and data["class"] == "no"):
            rec_meno["lt40_n"] += 1

    return rec_meno

def node_prob(data):
    rec_node = {
        "nodyes_y" : 0,
        "nodyes_n" : 0,
        "nodno_y" : 0,
        "nodno_n" : 0
    }

    if (data["node_caps"] == "yes" and data["class"] == "yes"):
        rec_node["nodyes_y"] += 1
    if (data["node_caps"] == "yes" and data["class"] == "no"):
        rec_node["nodyes_n"] += 1

    if (data["node_caps"] == "no" and data["class"] == "yes"):
        rec_node["nodno_y"] += 1
    if (data["node_caps"] == "no" and data["class"] == "no"):
        rec_node["nodno_n"] += 1


    return rec_node

def deg_prob(data):
    rec_deg = {
        "1y" : 0,
        "1n" : 0,
        "2y" : 0,
        "2n" : 0,
        "3y" : 0,
        "3n" : 0
    }

    if (data["deg_malig"] == "1" and data["class"] == "yes"):
        rec_deg["1y"] += 1
    if (data["deg_malig"] == "1" and data["class"] == "no"):
        rec_deg["1n"] += 1

    if (data["deg_malig"] == "2" and data["class"] == "yes"):
        rec_deg["2y"] += 1
    if (data["deg_malig"] == "2" and data["class"] == "no"):
        rec_deg["2n"] += 1

    if (data["deg_malig"] == "3" and data["class"] == "yes"):
        rec_deg["3y"] += 1
    if (data["deg_malig"] == "3" and data["class"] == "no"):
        rec_deg["3n"] += 1

    return rec_deg

def breast_prob(data):
    rec_breast = {
        "left_y" : 0,
        "left_n" : 0,
        "right_y" : 0,
        "right_n" : 0
    }

    if (data["breast"] == "left" and data["class"] == "yes"):
        rec_breast["left_y"] += 1
    if (data["breast"] == "left" and data["class"] == "no"):
        rec_breast["left_n"] += 1

    if (data["breast"] == "right" and data["class"] == "yes"):
        rec_breast["right_y"] += 1
    if (data["breast"] == "right" and data["class"] == "no"):
        rec_breast["right_n"] += 1

    return rec_breast

def quad_prob(data):
    rec_quad = {
        "leftlow_y" : 0,
        "leftlow_n" : 0,
        "leftup_y" : 0,
        "leftup_n" : 0,
        "rightlow_y" : 0,
        "rightlow_n" : 0,
        "rightup_y" : 0,
        "rightup_n" : 0,
        "central_y" : 0,
        "central_n" : 0
    }

    if (data["breast"] == "left_low" and data["class"] == "yes"):
        rec_breast["leftlow_y"] += 1
    if (data["breast"] == "left_low" and data["class"] == "no"):
        rec_breast["leftlow_n"] += 1

    if (data["breast"] == "left_up" and data["class"] == "yes"):
        rec_breast["leftup_y"] += 1
    if (data["breast"] == "left_up" and data["class"] == "no"):
        rec_breast["leftup_n"] += 1

    if (data["breast"] == "right_low" and data["class"] == "yes"):
        rec_breast["rightlow_y"] += 1
    if (data["breast"] == "right_low" and data["class"] == "no"):
        rec_breast["rightlow_n"] += 1

    if (data["breast"] == "right_up" and data["class"] == "yes"):
        rec_breast["rightup_y"] += 1
    if (data["breast"] == "right_up" and data["class"] == "no"):
        rec_breast["rightup_n"] += 1

    if (data["breast"] == "central" and data["class"] == "yes"):
        rec_breast["central_y"] += 1
    if (data["breast"] == "central" and data["class"] == "no"):
        rec_breast["central_n"] += 1

    return rec_quad

def irradiant_prob(data):
    rec_rad = {
        "radyes_y" : 0,
        "radyes_n" : 0,
        "radno_y" : 0,
        "radno_n" : 0
    }

    if (data["irradiant"] == "yes" and data["class"] == "yes"):
        rec_node["radyes_y"] += 1
    if (data["irradiant"] == "yes" and data["class"] == "no"):
        rec_node["radyes_n"] += 1

    if (data["irradiant"] == "no" and data["class"] == "yes"):
        rec_node["radno_y"] += 1
    if (data["irradiant"] == "no" and data["class"] == "no"):
        rec_node["radno_n"] += 1

    return rec_rad