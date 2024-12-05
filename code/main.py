import data_preparation as dp

dyslexic = ["1009", "1021", "1038", "1082", "1113", "1115", "1134", "1166", "1174", "1300", "1312", "1349", "1350", "1405", "1417", "1421", "1459", "1476", "1571", "1582", "1591", "1626", "1693", "1729", "1744", "1760", "1858", "1859", "1869", "1879", "1903", "1913", "1929", "1993", "1996"]
non_dyslexic = ["1003", "1016", "1019", "1033", "1040", "1058", "1065", "1073", "1075", "1090", "1095", "1109", "1145", "1160", "1169", "1186", "1187", "1189", "1209", "1235", "1254", "1255", "1257", "1258", "1263", "1271", "1274", "1284", "1314", "1318", "1322", "1345", "1377", "1380", "1398"]

text_type = {
    'syllables' : '_T1_Syllables',
    'meaningful' : '_T4_Meaningful_Text',
    'pseudo' : '_T5_Pseudo_Text'
}

image_path = {
    'syllables' : 'essential_dataset\\images\\s7_stimuli_t1.jpg',
    'meaningful' : 'essential_dataset\\images\\s7_stimuli_t4.jpg',
    'pseudo' : 'essential_dataset\\images\\s7_stimuli_t5.jpg'
}

df = dp.generateData(subject=dyslexic[0], text_type=text_type['syllables'])
dp.plotScatter(df=df, image_path=image_path['syllables'])
