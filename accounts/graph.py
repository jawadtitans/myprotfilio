import matplotlib.pyplot as plt

fpr = [0.00, 0.00, 0.20, 0.20, 0.40, 0.60, 0.60, 0.80, 0.80, 1.00]
tpr = [0.20, 0.40, 0.40, 0.60, 0.60, 0.60, 0.80, 0.80, 1.00, 1.00]

plt.plot(fpr, tpr, marker='o')
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.title('ROC Curve')
plt.grid(True)
plt.show()
