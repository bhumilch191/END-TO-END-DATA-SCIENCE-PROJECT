# 💡 Customer Churn Prediction

A complete end-to-end machine learning web application built with **Flask** to predict customer churn. The model is trained using a dataset sourced from **Kaggle**, and the application supports predictions via both **manual form input** and **CSV file upload**.

This project is packaged using **PEP 621**-style `pyproject.toml` and runs in a dedicated **Conda environment** for reproducibility.

---

## 📸 Screenshots

![Home Page](screenshots/home.png)
![Result Table](screenshots/result.png)

---

## ✨ Features

* 🔮 Predict customer churn using trained ML model
* 📁 Upload CSV files for batch predictions
* 🧾 Download prediction results as CSV
* 📱 Mobile-responsive design
* 📦 Packaged with `pyproject.toml`
* ✅ Environment reproducibility with `conda`

---

## 🛠️ Technologies Used

* Python 3.8
* Flask
* Pandas, NumPy, Scikit-learn
* HTML, CSS, JavaScript (Vanilla)
* Conda (for environment)
* pyproject.toml (for packaging)

---

## 📁 Dataset

* Dataset Source: [Kaggle - Customer Churn Dataset](https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn)
* Dataset Source: [Kaggle - Customer Churn Dataset](https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn)
* You may need a Kaggle account to download the dataset.

---



---

## 🧪 Prerequisites

* Python 3.8
* Python 3.8
* Conda installed
* Git installed

---

## ⚙️ Installation

### 1. Clone the Repository

```windows CMD
git clone https://github.com/bhumilch191/END-TO-END-DATA-SCIENCE-PROJECT.git
cd customer-churn-prediction
```

### 2. Set up the Conda Environment

```Windows CMD
conda create -p churn_env python==3.8 -y
```
For activation use terminal suggestions.

### 3. Install Dependencies

```Windows CMD
pip install -r requirements.txt
```

Or using the pyproject standard:

```Windows CMD
pip install .
```

### 4. Setup Environment Variables

```bash
cp .env.example .env
# Edit `.env` and add your own secret key
```

### 5. Run the App

```bash
python application.py
```

Then go to your browser: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🔐 Environment Variables

Create a `.env` file and add:

```env
SECRET_KEY=your-secret-key-here
```

---

## 📦 Packaging & Dependency Management

This project uses `pyproject.toml` (PEP 621) for packaging and metadata.

Install the project:

```bash
pip install .
```

Freeze dependencies for deployment:

```bash
pip freeze > requirements.txt
```

---

## ✅ Usage

1. Start the server
2. Open the app in browser
3. Use the form or upload CSV to make predictions
4. Download results using the provided button

---

## 🐛 Known Issues

* Only CSV format is supported for uploads
* No authentication system yet
* Currently supports only binary classification (Exited / Not Exited)

---

## 🤝 Contributing

Pull requests are welcome. Before making changes, please create an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## 🤞 Acknowledgments

* [Kaggle](https://www.kaggle.com/) for dataset
* Flask Documentation
* Scikit-learn contributors

---

## 🧑‍💻 Author

**Bhumil Chauhan**
[LinkedIn](https://www.linkedin.com/in/bhumil-chauhan-01a147245/) • [GitHub](https://github.com/bhumilch191)
[LinkedIn](https://www.linkedin.com/in/bhumil-chauhan-01a147245/) • [GitHub](https://github.com/bhumilch191)
