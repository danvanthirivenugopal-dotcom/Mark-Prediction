import pandas as pd
from sklearn.linear_model import LinearRegression
import tkinter as tk

# Load dataset from CSV
data = pd.read_csv(r"C:\Users\Acer\OneDrive\Documents\Project\Mark Prediction\data.txt")
# Split input and output
X = data[['study_hours']]
y = data['mark']

# Train model
model = LinearRegression()
model.fit(X, y)

# Prediction function
def predict_marks():
    try:
        hours = float(entry.get())

        # Check range
        if hours < 0 or hours > 12:
            result_label.config(text="Enter hours between 0 and 12")
            return

        prediction = model.predict([[hours]])[0]

        # Limit marks between 1 and 100
        prediction = max(1, min(100, prediction))

        result_label.config(text=f"Predicted Marks: {prediction:.2f}")

    except:
        result_label.config(text="Please enter a valid number")
# GUI Window
window = tk.Tk()
window.title("Study Hours vs Marks Predictor")
window.geometry("300x200")

label = tk.Label(window, text="Enter Study Hours")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Predict Marks", command=predict_marks)
button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()