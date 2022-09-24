import pandas as pd

dictionary_data = {0: [{'panelId': 74, 'x': 1049, 'y': 173, 'o': 300, 'shapeType': 0}, {'panelId': 75, 'x': 974, 'y': 129, 'o': 120, 'shapeType': 0}, {'panelId': 76, 'x': 899, 'y': 173, 'o': 60, 'shapeType': 0}, 
{'panelId': 77, 'x': 824, 'y': 129, 'o': 0, 'shapeType': 0}, {'panelId': 78, 'x': 749, 'y': 173, 'o': 180, 'shapeType': 0}, {'panelId': 79, 'x': 674, 'y': 129, 'o': 0, 'shapeType': 0}, {'panelId': 80, 'x': 599, 'y': 173, 'o': 60, 'shapeType': 0}, 
{'panelId': 81, 'x': 524, 'y': 129, 'o': 120, 'shapeType': 0}, {'panelId': 82, 'x': 449, 'y': 173, 'o': 300, 'shapeType': 0}, {'panelId': 83, 'x': 374, 'y': 129, 'o': 240, 'shapeType': 0}, {'panelId': 84, 'x': 299, 'y': 173, 'o': 60, 'shapeType': 0}, 
{'panelId': 85, 'x': 224, 'y': 129, 'o': 240, 'shapeType': 0}, {'panelId': 87, 'x': 149, 'y': 173, 'o': 180, 'shapeType': 0}, {'panelId': 88, 'x': 74, 'y': 129, 'o': 120, 'shapeType': 0}, {'panelId': 90, 'x': 74, 'y': 43, 'o': 180, 'shapeType': 0}, 
{'panelId': 91, 'x': 149, 'y': 0, 'o': 240, 'shapeType': 0}, {'panelId': 92, 'x': 224, 'y': 43, 'o': 300, 'shapeType': 0}, {'panelId': 93, 'x': 299, 'y': 0, 'o': 240, 'shapeType': 0}, 
{'panelId': 94, 'x': 374, 'y': 43, 'o': 60, 'shapeType': 0}, {'panelId': 95, 'x': 449, 'y': 0, 'o': 0, 'shapeType': 0}, {'panelId': 96, 'x': 524, 'y': 43, 'o': 60, 'shapeType': 0}, 
{'panelId': 97, 'x': 599, 'y': 0, 'o': 0, 'shapeType': 0}, {'panelId': 98, 'x': 674, 'y': 43, 'o': 300, 'shapeType': 0}, {'panelId': 99, 'x': 749, 'y': 0, 'o': 0, 'shapeType': 0}, {'panelId': 100, 'x': 824, 'y': 43, 'o': 180, 'shapeType': 0}, 
{'panelId': 101, 'x': 899, 'y': 0, 'o': 0, 'shapeType': 0}, {'panelId': 102, 'x': 974, 'y': 43, 'o': 180, 'shapeType': 0}, {'panelId': 89, 'x': 0, 'y': 173, 'o': 60, 'shapeType': 0}], 1: [{'panelId': 69, 'x': 1199, 'y': 43, 'o': 180, 'shapeType': 0}, 
{'panelId': 70, 'x': 1124, 'y': 0, 'o': 120, 'shapeType': 0}, {'panelId': 71, 'x': 1049, 'y': 43, 'o': 300, 'shapeType': 0}, {'panelId': 72, 'x': 974, 'y': 0, 'o': 0, 'shapeType': 0}, {'panelId': 73, 'x': 899, 'y': 43, 'o': 60, 'shapeType': 0}, {'panelId': 74, 'x': 824, 'y': 0, 'o': 120, 'shapeType': 0}, 
{'panelId': 75, 'x': 749, 'y': 43, 'o': 300, 'shapeType': 0}, {'panelId': 76, 'x': 674, 'y': 0, 'o': 0, 'shapeType': 0}, {'panelId': 77, 'x': 599, 'y': 43, 'o': 60, 'shapeType': 0}, {'panelId': 78, 'x': 524, 'y': 0, 'o': 240, 'shapeType': 0}, 
{'panelId': 79, 'x': 449, 'y': 43, 'o': 300, 'shapeType': 0}, {'panelId': 80, 'x': 374, 'y': 0, 'o': 0, 'shapeType': 0}, 
{'panelId': 81, 'x': 299, 'y': 43, 'o': 180, 'shapeType': 0}, {'panelId': 9, 'x': 224, 'y': 0, 'o': 0, 'shapeType': 0}, {'panelId': 10, 'x': 149, 'y': 43, 'o': 60, 'shapeType': 0}, {'panelId': 11, 'x': 74, 'y': 0, 'o': 0, 'shapeType': 0}, {'panelId': 16, 'x': 0, 'y': 43, 'o': 300, 'shapeType': 0}], 
2: [{'panelId': 44, 'x': 1349, 'y': 43, 'o': 60, 'shapeType': 0}, {'panelId': 45, 'x': 1274, 'y': 0, 'o': 120, 'shapeType': 0}, {'panelId': 46, 'x': 1199, 'y': 43, 'o': 60, 'shapeType': 0}, {'panelId': 15, 'x': 1124, 'y': 0, 'o': 240, 'shapeType': 0}, {'panelId': 19, 'x': 1049, 'y': 43, 'o': 180, 'shapeType': 0}, 
{'panelId': 18, 'x': 974, 'y': 0, 'o': 120, 'shapeType': 0}, {'panelId': 17, 'x': 899, 'y': 43, 'o': 300, 'shapeType': 0}, {'panelId': 47, 'x': 824, 'y': 0, 'o': 120, 'shapeType': 0}, {'panelId': 48, 'x': 749, 'y': 43, 'o': 180, 'shapeType': 0}, 
{'panelId': 49, 'x': 674, 'y': 0, 'o': 240, 'shapeType': 0}, {'panelId': 50, 'x': 599, 'y': 43, 'o': 60, 'shapeType': 0}, {'panelId': 51, 'x': 524, 'y': 0, 'o': 240, 'shapeType': 0}, {'panelId': 52, 'x': 449, 'y': 43, 'o': 300, 'shapeType': 0}, {'panelId': 53, 'x': 374, 'y': 0, 'o': 240, 'shapeType': 0}, 
{'panelId': 54, 'x': 299, 'y': 43, 'o': 300, 'shapeType': 0}, {'panelId': 55, 'x': 224, 'y': 0, 'o': 0, 'shapeType': 0}, {'panelId': 56, 'x': 149, 'y': 43, 'o': 300, 'shapeType': 0}, {'panelId': 57, 'x': 74, 'y': 0, 'o': 120, 'shapeType': 0}, {'panelId': 58, 'x': 0, 'y': 43, 'o': 180, 'shapeType': 0}], 
3: [{'panelId': 38, 'x': 1499, 'y': 43, 'o': 180, 'shapeType': 0}, {'panelId': 37, 'x': 1424, 'y': 0, 'o': 120, 'shapeType': 0}, {'panelId': 36, 'x': 1349, 'y': 43, 'o': 180, 'shapeType': 0}, {'panelId': 88, 'x': 1274, 'y': 0, 'o': 120, 'shapeType': 0}, {'panelId': 89, 'x': 1199, 'y': 43, 'o': 180, 'shapeType': 0}, 
{'panelId': 90, 'x': 1124, 'y': 0, 'o': 240, 'shapeType': 0}, {'panelId': 91, 'x': 1049, 'y': 43, 'o': 180, 'shapeType': 0}, {'panelId': 17, 'x': 974, 'y': 0, 'o': 120, 'shapeType': 0}, {'panelId': 13, 'x': 899, 'y': 43, 'o': 180, 'shapeType': 0}, {'panelId': 12, 'x': 824, 'y': 0, 'o': 120, 'shapeType': 0}, 
{'panelId': 11, 'x': 749, 'y': 43, 'o': 180, 'shapeType': 0}, {'panelId': 10, 'x': 674, 'y': 0, 'o': 0, 'shapeType': 0}, {'panelId': 92, 'x': 599, 'y': 43, 'o': 300, 'shapeType': 0}, {'panelId': 93, 'x': 524, 'y': 0, 'o': 240, 'shapeType': 0}, {'panelId': 94, 'x': 449, 'y': 43, 'o': 300, 'shapeType': 0}, 
{'panelId': 18, 'x': 374, 'y': 0, 'o': 240, 'shapeType': 0}, {'panelId': 95, 'x': 299, 'y': 43, 'o': 300, 'shapeType': 0}, {'panelId': 96, 'x': 224, 'y': 0, 'o': 240, 'shapeType': 0}, {'panelId': 41, 'x': 149, 'y': 43, 'o': 60, 'shapeType': 0}, {'panelId': 45, 'x': 74, 'y': 0, 'o': 0, 'shapeType': 0}, 
{'panelId': 97, 'x': 0, 'y': 43, 'o': 300, 'shapeType': 0}], 4: [{'panelId': 56, 'x': 1649, 'y': 43, 'o': 300, 'shapeType': 0}, {'panelId': 57, 'x': 1574, 'y': 0, 'o': 0, 'shapeType': 0}, {'panelId': 58, 'x': 1499, 'y': 43, 'o': 180, 'shapeType': 0}, {'panelId': 59, 'x': 1424, 'y': 0, 'o': 240, 'shapeType': 0}, 
{'panelId': 60, 'x': 1349, 'y': 43, 'o': 60, 'shapeType': 0}, {'panelId': 61, 'x': 1274, 'y': 0, 'o': 0, 'shapeType': 0}, {'panelId': 62, 'x': 1199, 'y': 43, 'o': 180, 'shapeType': 0}, {'panelId': 63, 'x': 1124, 'y': 0, 'o': 0, 'shapeType': 0}, {'panelId': 64, 'x': 1049, 'y': 43, 'o': 300, 'shapeType': 0},
 {'panelId': 65, 'x': 974, 'y': 0, 'o': 0, 'shapeType': 0}, {'panelId': 66, 'x': 899, 'y': 43, 'o': 300, 'shapeType': 0},
 {'panelId': 67, 'x': 824, 'y': 0, 'o': 240, 'shapeType': 0}, 
{'panelId': 68, 'x': 749, 'y': 43, 'o': 180, 'shapeType': 0}, 
{'panelId': 69, 'x': 674, 'y': 0, 'o': 240, 'shapeType': 0}, {'panelId': 70, 'x': 599, 'y': 43, 'o': 60, 'shapeType': 0}, {'panelId': 71, 'x': 524, 'y': 0, 'o': 240, 'shapeType': 0}, {'panelId': 72, 'x': 449, 'y': 43, 'o': 300, 'shapeType': 0},
 {'panelId': 73, 'x': 374, 'y': 0, 'o': 240, 'shapeType': 0}, {'panelId': 74, 'x': 299, 'y': 43, 'o': 180, 'shapeType': 0}, {'panelId': 75, 'x': 224, 'y': 0, 'o': 0, 'shapeType': 0}, {'panelId': 76, 'x': 150, 'y': 43, 'o': 300, 'shapeType': 0}, {'panelId': 77, 'x': 74, 'y': 0, 'o': 240, 'shapeType': 0},
  {'panelId': 78, 'x': 0, 'y': 43, 'o': 300, 'shapeType': 0}], 5: [{'panelId': 69, 'x': 824, 'y': 0, 'o': 300, 'shapeType': 0}, {'panelId': 71, 'x': 824, 'y': 86, 'o': 120, 'shapeType': 0}, {'panelId': 78, 'x': 749, 'y': 129, 'o': 60, 'shapeType': 0}, {'panelId': 70, 'x': 749, 'y': 216, 'o': 240, 'shapeType': 0}, 
  {'panelId': 64, 'x': 674, 'y': 259, 'o': 300, 'shapeType': 0}, {'panelId': 68, 'x': 674, 'y': 346, 'o': 120, 'shapeType': 0}, {'panelId': 85, 'x': 599, 'y': 389, 'o': 180, 'shapeType': 0}, {'panelId': 59, 'x': 599, 'y': 476, 'o': 120, 'shapeType': 0}, {'panelId': 79, 'x': 524, 'y': 519, 'o': 60, 'shapeType': 0}, 
  {'panelId': 73, 'x': 524, 'y': 606, 'o': 120, 'shapeType': 0}, {'panelId': 80, 'x': 449, 'y': 649, 'o': 300, 'shapeType': 0}, {'panelId': 61, 'x': 449, 'y': 736, 'o': 0, 'shapeType': 0}, {'panelId': 33, 'x': 374, 'y': 779, 'o': 60, 'shapeType': 0}, {'panelId': 72, 'x': 374, 'y': 866, 'o': 240, 'shapeType': 0}, 
  {'panelId': 67, 'x': 299, 'y': 909, 'o': 300, 'shapeType': 0}, {'panelId': 63, 'x': 299, 'y': 995, 'o': 240, 'shapeType': 0}, {'panelId': 62, 'x': 224, 'y': 1039, 'o': 300, 'shapeType': 0}, {'panelId': 17, 'x': 224, 'y': 1125, 'o': 120, 'shapeType': 0}, 
{'panelId': 65, 'x': 149, 'y': 1169, 'o': 180, 'shapeType': 0},
 {'panelId': 66, 'x': 149, 'y': 1255, 'o': 0, 'shapeType': 0}, {'panelId': 75, 'x': 74, 'y': 1299, 'o': 180, 'shapeType': 0}, {'panelId': 77, 'x': 74, 'y': 1385, 'o': 0, 'shapeType': 0}, 
{'panelId': 31, 'x': 0, 'y': 1428, 'o': 300, 'shapeType': 0}], 
6: [{'panelId': 70, 'x': 749, 'y': 43, 'o': 60, 'shapeType': 0}, {'panelId': 52, 'x': 749, 'y': 129, 'o': 240, 'shapeType': 0}, {'panelId': 53, 'x': 674, 'y': 173, 'o': 300, 'shapeType': 0}, {'panelId': 54, 'x': 674, 'y': 259, 'o': 0, 'shapeType': 0}, {'panelId': 55, 'x': 599, 'y': 303, 'o': 60, 'shapeType': 0}, {'panelId': 56, 'x': 599, 'y': 389, 'o': 240, 'shapeType': 0}, {'panelId': 57, 'x': 524, 'y': 433, 'o': 60, 'shapeType': 0}, {'panelId': 58, 'x': 524, 'y': 519, 'o': 240, 'shapeType': 0}, {'panelId': 59, 'x': 449, 'y': 562, 'o': 180, 'shapeType': 0}, {'panelId': 17, 'x': 449, 'y': 649, 'o': 240, 'shapeType': 0}, {'panelId': 18, 'x': 374, 'y': 692, 'o': 300, 'shapeType': 0}, {'panelId': 60, 'x': 374, 'y': 779, 'o': 120, 'shapeType': 0}, {'panelId': 61, 'x': 299, 'y': 822, 'o': 60, 'shapeType': 0}, {'panelId': 62, 'x': 299, 'y': 909, 'o': 120, 'shapeType': 0}, {'panelId': 63, 'x': 225, 'y': 952, 'o': 60, 'shapeType': 0}, {'panelId': 64, 'x': 224, 'y': 1039, 'o': 240, 'shapeType': 0}, {'panelId': 65, 'x': 149, 'y': 1082, 'o': 60, 'shapeType': 0}, {'panelId': 66, 'x': 149, 'y': 1169, 'o': 240, 'shapeType': 0}, {'panelId': 67, 'x': 74, 'y': 1212, 'o': 300, 'shapeType': 0}, {'panelId': 68, 'x': 74, 'y': 1299, 'o': 240, 'shapeType': 0}, {'panelId': 71, 'x': 0, 'y': 1342, 'o': 60, 'shapeType': 0}], 7: [{'panelId': 75, 'x': 674, 'y': 43, 'o': 180, 'shapeType': 0}, 
{'panelId': 60, 'x': 674, 'y': 129, 'o': 240, 'shapeType': 0}, {'panelId': 61, 'x': 599, 'y': 173, 'o': 60, 'shapeType': 0}, {'panelId': 62, 'x': 599, 'y': 259, 'o': 0, 'shapeType': 0}, {'panelId': 63, 'x': 524, 'y': 303, 'o': 180, 'shapeType': 0}, {'panelId': 64, 'x': 524, 'y': 389, 'o': 240, 'shapeType': 0}, {'panelId': 65, 'x': 449, 'y': 433, 'o': 180, 'shapeType': 0}, {'panelId': 66, 'x': 449, 'y': 519, 'o': 120, 'shapeType': 0}, {'panelId': 67, 'x': 374, 'y': 562, 'o': 180, 'shapeType': 0}, {'panelId': 68, 'x': 374, 'y': 649, 'o': 0, 'shapeType': 0}, {'panelId': 69, 'x': 299, 'y': 692, 'o': 60, 'shapeType': 0}, {'panelId': 70, 'x': 299, 'y': 779, 'o': 120, 'shapeType': 0}, {'panelId': 71, 'x': 224, 'y': 822, 'o': 300, 'shapeType': 0}, {'panelId': 72, 'x': 224, 'y': 909, 'o': 240, 'shapeType': 0}, {'panelId': 73, 'x': 149, 'y': 952, 'o': 300, 'shapeType': 0}, {'panelId': 74, 'x': 149, 'y': 1039, 'o': 240, 'shapeType': 0}, {'panelId': 76, 'x': 74, 'y': 1082, 'o': 180, 'shapeType': 0}, {'panelId': 78, 'x': 74, 'y': 1169, 'o': 240, 'shapeType': 0}, {'panelId': 79, 'x': 0, 'y': 1212, 'o': 180, 'shapeType': 0}], 8: [{'panelId': 69, 'x': 599, 'y': 0, 'o': 300, 'shapeType': 0}, {'panelId': 59, 'x': 599, 'y': 86, 'o': 240, 'shapeType': 0}, {'panelId': 60, 'x': 524, 'y': 129, 'o': 60, 'shapeType': 0}, {'panelId': 131, 'x': 524, 'y': 216, 'o': 120, 'shapeType': 0}, {'panelId': 38, 'x': 449, 'y': 259, 'o': 300, 'shapeType': 0}, {'panelId': 37, 'x': 449, 'y': 346, 'o': 0, 'shapeType': 0},
 {'panelId': 61, 'x': 374, 'y': 389, 'o': 300, 'shapeType': 0}, {'panelId': 62, 'x': 374, 'y': 476, 'o': 120, 'shapeType': 0}, {'panelId': 63, 'x': 299, 'y': 519, 'o': 60, 'shapeType': 0}, {'panelId': 65, 'x': 299, 'y': 606, 'o': 240, 'shapeType': 0}, {'panelId': 66, 'x': 224, 'y': 649, 'o': 180, 'shapeType': 0}, {'panelId': 67, 'x': 224, 'y': 736, 'o': 240, 'shapeType': 0}, {'panelId': 22, 'x': 149, 'y': 779, 'o': 60, 'shapeType': 0}, 
{'panelId': 21, 'x': 149, 'y': 866, 'o': 240, 'shapeType': 0}, {'panelId': 20, 'x': 74, 'y': 909, 'o': 300, 'shapeType': 0}, {'panelId': 19, 'x': 74, 'y': 995, 'o': 0, 'shapeType': 0}, {'panelId': 68, 'x': 0, 'y': 1039, 'o': 300, 'shapeType': 0}], 9: [{'panelId': 39, 'x': 524, 'y': 43, 'o': 60, 'shapeType': 0}, {'panelId': 98, 'x': 524, 'y': 129, 'o': 120, 'shapeType': 0}, {'panelId': 76, 'x': 449, 'y': 173, 'o': 300, 'shapeType': 0}, {'panelId': 77, 'x': 449, 'y': 259, 'o': 0, 'shapeType': 0}, {'panelId': 78, 'x': 374, 'y': 303, 'o': 180, 'shapeType': 0}, {'panelId': 79, 'x': 374, 'y': 389, 'o': 240, 'shapeType': 0}, {'panelId': 80, 'x': 299, 'y': 433, 'o': 60, 'shapeType': 0}, {'panelId': 81, 'x': 299, 'y': 519, 'o': 240, 'shapeType': 0}, {'panelId': 82, 'x': 224, 'y': 562, 'o': 180, 'shapeType': 0}, {'panelId': 83, 'x': 224, 'y': 649, 'o': 240, 'shapeType': 0}, {'panelId': 84, 'x': 149, 'y': 692, 'o': 180, 'shapeType': 0}, {'panelId': 85, 'x': 149, 'y': 779, 'o': 240, 'shapeType': 0}, {'panelId': 86, 'x': 74, 'y': 822, 'o': 180, 'shapeType': 0}, {'panelId': 87, 'x': 74, 'y': 909, 'o': 240, 'shapeType': 0}, {'panelId': 88, 'x': 149, 'y': 952, 'o': 60, 'shapeType': 0}, {'panelId': 10, 'x': 224, 'y': 909, 'o': 0, 'shapeType': 0}, {'panelId': 89, 'x': 224, 'y': 822, 'o': 180, 'shapeType': 0}, {'panelId': 90, 'x': 299, 'y': 779, 'o': 120, 'shapeType': 0}, {'panelId': 91, 'x': 299, 'y': 692, 'o': 300, 'shapeType': 0}, {'panelId': 92, 'x': 374, 'y': 649, 'o': 0, 'shapeType': 0}, {'panelId': 93, 'x': 374, 'y': 562, 'o': 60, 'shapeType': 0}, {'panelId': 94, 'x': 449, 'y': 519, 'o': 120, 'shapeType': 0}, {'panelId': 95, 'x': 449, 'y': 433, 'o': 60, 'shapeType': 0}, {'panelId': 96, 'x': 524, 'y': 389, 'o': 0, 'shapeType': 0}, {'panelId': 97, 'x': 524, 'y': 303, 'o': 300, 'shapeType': 0}, {'panelId': 55, 'x': 599, 'y': 259, 'o': 120, 'shapeType': 0}, {'panelId': 75, 'x': 599, 'y': 173, 'o': 180, 'shapeType': 0}, 
{'panelId': 100, 'x': 0, 'y': 952, 'o': 180, 'shapeType': 0}]}

#print(dictionary_data[0][0]['panelId'])

#Creates a list of lists that contain the panelIds
panel_ids = []
for i in dictionary_data:
    panel_ids.append([])
    #print(dictionary_data[i])
    for j in dictionary_data[i]:
        #print(j['panelId'])
        panel_ids[i].append(j['panelId'])

#print(panel_ids)
#Figure out how to split up first row and last row!!!!!!!!!!!!!!!!!!!!!
#Splits up the first row into 2 rows
first_row = panel_ids[0][0:14]
first_row.append(panel_ids[0][27])
#print(first_row)

zero_row = panel_ids[0][14:27]
#print(zero_row)

#Add new list of lists for the first two rows 
panel_ids.pop(0)
panel_ids.insert(0, first_row)
panel_ids.insert(0,zero_row)

#print(panel_ids)

#Splits up last row into two rows
nine_row = panel_ids[10][0:14] 
nine_row.append(panel_ids[10][27])

ten_row = panel_ids[10][14:27]
#print(ten_row)

#Add new list of lists for last two rows
panel_ids.pop(10)
panel_ids.insert(10, nine_row)
panel_ids.insert(10, ten_row)

#print(panel_ids)

#Creates a new dictionary that contains the row and panel Ids
panel_id_dict = {}

for i in range(12):
    panel_id_dict[i] = panel_ids[i]

#print(panel_id_dict[0][0:14])

#print(panel_id_dict)
#print(panel_id_dict[0][4])
        

