# Mathematical Foundations & Advanced Topics

A comprehensive Jupyter Book covering mathematical concepts from linear algebra to advanced mathematics, with a focus on statistical learning and regularization techniques.

## 📚 Contents

This repository contains interactive Jupyter notebooks organized into the following main sections:

### 📖 Linear Algebra
- **Chapter 1: Interpretation** - Fundamental concepts and geometric interpretations
- **Chapter 2: Matrix Operations** - Essential matrix computations and properties

### 🚀 Advanced Mathematics
- **Chapter 1: Limits and Continuity** - Foundation of calculus and mathematical analysis

### 🔧 Foundation
- **Regularization** - Comprehensive guide to regularization techniques
  - Ridge Regression (岭回归)
  - Lasso Regression (套索回归)
  - Elastic Net (弹性网络)
  - Bayesian perspective and bias-variance tradeoff

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
│   └── Foundation/             # Foundational concepts
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
