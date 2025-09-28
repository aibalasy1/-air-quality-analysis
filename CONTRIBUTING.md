# Contributing to Air Quality Analysis Project

Thank you for your interest in contributing to this air quality analysis research project! 🌬️

## 🤝 How to Contribute

### Types of Contributions Welcome

1. **🔬 Research Enhancements**
   - Novel time series analysis methods
   - Advanced feature engineering techniques
   - Alternative machine learning approaches
   - Statistical model improvements

2. **📊 Data Contributions**
   - Additional air quality datasets
   - Extended meteorological data
   - Cross-regional validation data
   - Historical pollution records

3. **💻 Code Improvements**
   - Performance optimizations
   - Code documentation
   - Bug fixes and error handling
   - Unit test development

4. **📚 Documentation**
   - Tutorial improvements
   - Method explanations
   - Usage examples
   - Academic references

## 🚀 Getting Started

### 1. Fork the Repository
```bash
git clone https://github.com/aibalasy1/air-quality-analysis.git
cd air-quality-analysis
```

### 2. Create a Development Environment
```bash
python -m venv air_quality_dev
source air_quality_dev/bin/activate  # Windows: air_quality_dev\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt  # If available
```

### 3. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
# or  
git checkout -b docs/your-documentation-update
```

## 📋 Development Guidelines

### Code Standards
- **PEP 8**: Follow Python style guidelines
- **Type Hints**: Use type annotations for functions
- **Docstrings**: Document all functions and classes
- **Comments**: Explain complex algorithms and data transformations

### Example Code Style
```python
from typing import Tuple, Optional
import pandas as pd
import numpy as np

def calculate_lag_features(
    df: pd.DataFrame, 
    target_column: str, 
    lag_days: list[float]
) -> pd.DataFrame:
    """
    Calculate lag features for time series analysis.
    
    Args:
        df: Input dataframe with datetime index
        target_column: Column name for which to calculate lags
        lag_days: List of lag periods in days
        
    Returns:
        DataFrame with additional lag feature columns
        
    Example:
        >>> df_with_lags = calculate_lag_features(df, 'CO', [1, 6])
    """
    df_copy = df.copy()
    
    for lag in lag_days:
        lag_periods = int(lag * 8)  # 3-hour intervals per day
        col_name = f"{target_column}_lag_{lag}"
        df_copy[col_name] = df_copy[target_column].shift(lag_periods)
    
    return df_copy
```

### Notebook Standards
- Clear markdown headers and explanations
- Well-commented code cells
- Proper data visualization with titles and labels
- Summary conclusions for each analysis section

## 🧪 Testing

### Running Tests
```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html
```

### Adding Tests
Create test files in the `tests/` directory:
```python
import pytest
import pandas as pd
from src.preprocessing import calculate_lag_features

def test_calculate_lag_features():
    # Create test data
    test_df = pd.DataFrame({
        'datetime': pd.date_range('2023-01-01', periods=100, freq='3H'),
        'CO': np.random.normal(50, 10, 100)
    })
    
    # Test lag calculation
    result = calculate_lag_features(test_df, 'CO', [1])
    
    assert 'CO_lag_1' in result.columns
    assert len(result) == len(test_df)
```

## 📖 Documentation

### Updating Documentation
- Update README.md for new features
- Add docstrings to new functions
- Include usage examples
- Update CHANGELOG.md

### Academic Documentation
For research contributions:
- Cite relevant literature
- Explain methodology changes
- Provide statistical validation
- Include performance comparisons

## 🐛 Bug Reports

### Before Submitting
1. Check existing issues
2. Search documentation
3. Test with latest version
4. Prepare minimal reproduction example

### Bug Report Template
```markdown
**Describe the Bug**
Clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Load data with '...'
2. Run function '....'
3. See error

**Expected Behavior**
What you expected to happen.

**Environment**
- OS: [e.g. Windows 10, macOS, Ubuntu]
- Python version: [e.g. 3.9.0]
- Package versions: [paste output of `pip freeze`]

**Additional Context**
Add any other context about the problem.
```

## 🆕 Feature Requests

### Feature Request Template
```markdown
**Feature Description**
Clear description of the proposed feature.

**Research Justification**
Why this feature would improve the analysis.

**Implementation Ideas**
Potential approaches or algorithms.

**Related Work**
Academic papers or existing implementations.
```

## 📊 Data Contributions

### Data Quality Standards
- Documented data sources
- Clear variable definitions
- Known data quality issues
- Appropriate temporal resolution
- Geographic metadata

### Data Privacy
- No personal identifying information
- Aggregated environmental measurements only
- Compliance with data sharing agreements
- Proper attribution to data sources

## 🔄 Pull Request Process

### Before Submitting
1. Update documentation
2. Add/update tests
3. Ensure code passes all tests
4. Update CHANGELOG.md
5. Rebase on latest main branch

### Pull Request Template
```markdown
**Description**
Brief description of changes.

**Type of Change**
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

**Testing**
- [ ] All tests pass
- [ ] New tests added
- [ ] Manual testing completed

**Academic Impact**
How does this change improve the research?

**Checklist**
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No merge conflicts
```

## 📚 Resources

### Useful References
- [Time Series Analysis in Python](https://www.statsmodels.org/stable/tsa.html)
- [Environmental Data Analysis](https://pandas.pydata.org/docs/)
- [Scientific Python Ecosystem](https://scipy.org/)

### Academic Guidelines
- Follow reproducible research practices
- Use version control for all changes
- Document data sources and methods
- Validate results statistically

## 💬 Community

### Getting Help
- GitHub Issues for technical problems
- GitHub Discussions for research questions
- Email maintainer for collaboration opportunities

### Code of Conduct
- Be respectful and inclusive
- Focus on constructive feedback
- Help newcomers learn
- Acknowledge contributions of others

Thank you for contributing to advancing air quality research! 🌍