# Contributing to GitHub Architect Tool Server

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing Requirements](#testing-requirements)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)

## 🤝 Code of Conduct

### Our Pledge

We are committed to providing a friendly, safe, and welcoming environment for all contributors.

### Expected Behavior

- Use welcoming and inclusive language
- Be respectful of differing viewpoints and experiences
- Gracefully accept constructive criticism
- Focus on what is best for the community
- Show empathy towards other community members

## 💡 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce**
- **Expected vs actual behavior**
- **Environment details** (OS, Python version, etc.)
- **Logs and screenshots** (if applicable)

### Suggesting Features

Feature requests are welcome! Please provide:

- **Clear use case**: Why is this feature needed?
- **Proposed solution**: How should it work?
- **Alternatives considered**: What other approaches did you think about?
- **Additional context**: Mockups, examples, etc.

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Add tests**
5. **Update documentation**
6. **Submit a pull request**

## 🛠️ Development Setup

### Prerequisites

- Python 3.11+
- Git
- GitHub account

### Setup Steps

1. **Clone your fork**
```bash
git clone https://github.com/YOUR_USERNAME/OpenWebui-GitHub-Integration.git
cd OpenWebui-GitHub-Integration
```

2. **Run setup script**
```bash
./scripts/setup_dev.sh
source venv/bin/activate
```

3. **Create a branch**
```bash
git checkout -b feature/your-feature-name
```

4. **Make your changes**
```bash
# Edit files
# Add tests
# Update documentation
```

5. **Run tests**
```bash
pytest
```

6. **Commit your changes**
```bash
git add .
git commit -m "feat: add your feature description"
```

## 📏 Coding Standards

### Python Style Guide

We follow [PEP 8](https://pep8.org/) with some modifications:

- **Line length**: 100 characters (enforced by Black)
- **Import ordering**: Managed by isort
- **Type hints**: Required for all function signatures
- **Docstrings**: Required for all public functions/classes

### Code Formatting

Use the provided tools:

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Lint code
ruff check src/ tests/

# Type checking
mypy src/
```

### Commit Message Format

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Test updates
- `chore`: Build/tooling changes

**Examples:**
```
feat(api): add repository health analysis endpoint

fix(auth): resolve token validation issue

docs(readme): update installation instructions
```

## 🧪 Testing Requirements

### Test Coverage

- **Minimum coverage**: 80%
- **New features**: Must include tests
- **Bug fixes**: Must include regression tests

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/unit/test_validators.py

# Run integration tests
pytest tests/integration/
```

### Writing Tests

```python
# tests/unit/test_example.py
import pytest

class TestExample:
    def test_feature(self):
        """Test description."""
        # Arrange
        expected = "result"
        
        # Act
        actual = function_under_test()
        
        # Assert
        assert actual == expected
```

## 🔄 Pull Request Process

### Before Submitting

1. **Update documentation** if needed
2. **Add tests** for new functionality
3. **Run all tests** and ensure they pass
4. **Run linting tools** (Black, Ruff, MyPy)
5. **Update CHANGELOG.md** if applicable

### PR Checklist

- [ ] Code follows style guidelines
- [ ] Self-reviewed code
- [ ] Added/updated tests
- [ ] All tests pass
- [ ] Added/updated documentation
- [ ] No new warnings introduced
- [ ] Checked for security issues

### Review Process

1. **Automated checks** must pass (CI/CD)
2. **Code review** by at least one maintainer
3. **All feedback** must be addressed
4. **Approval required** before merging

### After Approval

- Maintainers will merge your PR
- Delete your feature branch
- Pull the latest main branch

## 🐛 Issue Reporting

### Security Issues

**DO NOT** create public issues for security vulnerabilities. Instead:

1. Email: security@example.com
2. Provide detailed description
3. Include steps to reproduce
4. Suggest a fix if possible

### Bug Reports

Use the bug report template and include:

- **Environment details**
- **Steps to reproduce**
- **Expected behavior**
- **Actual behavior**
- **Logs and screenshots**

### Feature Requests

Use the feature request template and include:

- **Problem statement**
- **Proposed solution**
- **Use cases**
- **Alternatives considered**

## 📞 Getting Help

- **Documentation**: Check the [docs/](../docs/) folder
- **Discussions**: Use [GitHub Discussions](https://github.com/ian-morgan99/OpenWebui-GitHub-Integration/discussions)
- **Issues**: Search [existing issues](https://github.com/ian-morgan99/OpenWebui-GitHub-Integration/issues)

## 🙏 Recognition

Contributors will be recognized in:

- **CONTRIBUTORS.md** file
- **Release notes**
- **Project README**

Thank you for contributing! 🎉
