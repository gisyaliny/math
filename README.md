# Mathematical Foundations & Advanced Topics

A comprehensive Jupyter Book covering mathematical concepts from linear algebra to advanced mathematics, with a focus on statistical learning and regularization techniques.

## 📚 Contents

This repository contains interactive Jupyter notebooks organized into the following main sections:

### 📖 Linear Algebra
- **Chapter 1: Interpretation** - Fundamental concepts and geometric interpretations
- **Chapter 2: Matrix Operations** - Essential matrix computations and properties

### 🚀 Advanced Mathematics
- **Chapter 1: Limits and Continuity** - Foundation of calculus and mathematical analysis
- **Chapter 2: Differential and Derivative** - Introduction to derivatives and basic rules
- **Chapter 3: L'Hôpital's Rule** - Techniques for evaluating indeterminate limits

### 🔧 Foundation
- **Regularization** - Comprehensive guide to regularization techniques
  - Ridge Regression (岭回归)
  - Lasso Regression (套索回归)
  - Elastic Net (弹性网络)
  - Bayesian perspective and bias-variance tradeoff

### 🌐 Spatial Learning
- **L1: Spatial Analysis Intro** - Spatial statistics fundamentals
- **L2: Maps** - Visualization and mapping techniques
- **L3: Exploratory Data Analysis** - Spatial data exploration
- **L4: Spatial Autocorrelation** - Global spatial correlation measures
- **L5: Global Spatial Autocorrelation** - Advanced global spatial statistics
- **L6: Visualizing Spatial Autocorrelation** - Visual methods for spatial autocorrelation
- **L7: LISA** - Local Indicators of Spatial Association
- **L8: Other Local Statistics** - Additional local spatial measures
- **L9: Multivariate LISA** - Multivariate local spatial analysis

## 🛠 Technologies

- **Jupyter Book** - Interactive educational content platform
- **Python** - Primary programming language
- **Numpy, Scikit-learn, Matplotlib** - Scientific computing and visualization
- **Jupyter Notebooks** - Interactive computational documents

## 📋 Requirements

```
jupyterbook>=0.12
jupyter>=1.0
numpy
scipy
scikit-learn
matplotlib
pandas
```

See `requirements.txt` for detailed dependencies.

## 🚀 Getting Started

### Build the Book

To build the Jupyter Book locally:

```bash
jupyter-book build .
```

### Deploy

The repository includes automated build and deployment scripts:

- **Windows**: Run `build_and_deploy.bat`
- **Python**: Run `python publish.py`

### View Online

The book is published at: [Math Notes](https://gisyaliny.github.io/math)

## 📁 Repository Structure

```
.
├── docs/
│   ├── LinearAlgebra/          # Linear algebra chapters
│   ├── AdvanceMath/            # Advanced mathematics chapters
│   ├── Foundation/             # Foundational concepts
│   └── st_learning_anselin/    # Spatial learning and local statistics
├── _toc.yml                    # Table of contents configuration
├── _config.yml                 # Jupyter Book configuration
├── requirements.txt            # Python dependencies
├── index.md                    # Book homepage
├── build_and_deploy.bat        # Windows build script
└── publish.py                  # Publishing script
```

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📝 Code of Conduct

Please review our [Code of Conduct](CONDUCT.md) before contributing.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 👤 Author

- **Author**: gisyaliny

## 🔗 Links

- **GitHub Repository**: https://github.com/gisyaliny/math
- **Published Book**: https://gisyaliny.github.io/math
- **Issues & Discussions**: https://github.com/gisyaliny/math/issues

## 📌 Notes

This repository uses Jupyter Book to create interactive, online educational content. Each chapter is a self-contained Jupyter notebook that can be run interactively or viewed as static HTML.

For questions or suggestions, please open an issue on GitHub.
